import numpy as np
from scipy.spatial import distance_matrix
import networkx as nx
import pandas as pd
import random
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import plotly.graph_objects as go
import plotly.io as pio
import webbrowser
from fractions import Fraction
from plotly.subplots import make_subplots


# This Class is for optical bandgap measurement analysis using UV-vis Spectra 
# To initiate this class
# hv-- you must convert your wavelength(nm) into photon energy(ev)
# r-- your reflectance data 


# Method: Plot 
# To use this method, you need to provide 
# l, your sample thickness(but if you only care about the transition energy, l's value does not matter)
# n, the order of the bandgap 
    # n = 2, direct allowed transition
    # n = 2/3, direct forbid transition 
    # n = 1/2, indirect allowed transit
    # n = 1/3, indirect forbid transit 
    # direct means electron + photon / indirect means electron + photon + phonon 


class bandgap: 
    def __init__(self,hv,r):
        self.hv = np.array(hv, dtype=float)
        self.r = np.array(r, dtype=float)
        self.y = 0
        self.x = 0
    def plot(self, l, n, fig=None, label=None, alpha=1.0, color=None):
        n_fraction = Fraction(n).limit_denominator()
        y = (self.hv * self.r) ** n / (l ** n)
        x = self.hv
        
        self.y = y 
        self.x = x

        if fig is None:
            fig = go.Figure()

        fig.add_trace(go.Scatter(
            x=x, 
            y=y, 
            mode='lines', 
            name=label, 
            line=dict(color=color),
            opacity=alpha
        ))

        # Check the value of n_fraction and set the title accordingly
        if n_fraction == 2:
            title = "Direct (Allowed) Bandgap"
        elif n_fraction == Fraction(2, 3):
            title = "Direct (Forbidden) Bandgap"
        elif n_fraction == Fraction(1, 2):
            title = "Indirect (Allowed) Bandgap"
        elif n_fraction == Fraction(1, 3):
            title = "Indirect (Forbidden) Bandgap"
        else:
            title = f"Bandgap, n = {n_fraction}"

        yaxis_title = f"<i>(α hv)</i><sup>{n_fraction}</sup>"
        fig.update_layout(
            title=dict(text=title, font=dict(size=30)),
            xaxis_title=dict(text="hv/eV", font=dict(size=28)),
            yaxis_title=dict(text=yaxis_title, font=dict(size=28)),
            xaxis=dict(showgrid=True, gridcolor='LightGrey', tickfont=dict(size=24)),
            yaxis=dict(showgrid=True, gridcolor='LightGrey', tickfont=dict(size=24)),
            legend=dict(font=dict(size=26)),
            plot_bgcolor='white',
            font=dict(size=24)
        )
        return fig
    

    def line_fit(self, xi, xf, xxi, xxf, fig):
        if fig is None:
            fig = go.Figure()

        mask1 = (self.x >= xi) & (self.x <= xf)
        x1_subset = self.x[mask1]
        y1_subset = self.y[mask1]
        coefficients1 = np.polyfit(x1_subset, y1_subset, 1)

        mask2 = (self.x >= xxi) & (self.x <= xxf)
        x2_subset = self.x[mask2]
        y2_subset = self.y[mask2]
        coefficients2 = np.polyfit(x2_subset, y2_subset, 1)

        # Calculate the intersection point of the two lines
        a1, b1 = coefficients1
        a2, b2 = coefficients2
        intersection_x = (b2 - b1) / (a1 - a2)
        intersection_y = a1 * intersection_x + b1

        # Define the short ranges after the intersection
        short_range_x1 = np.linspace(intersection_x-0.5, intersection_x + 0.5, 100)
        short_range_y1 = a1 * short_range_x1 + b1

        short_range_x2 = np.linspace(intersection_x-0.5, intersection_x + 0.5, 100)
        short_range_y2 = a2 * short_range_x2 + b2

        fig.add_trace(go.Scatter(
            x=short_range_x1,
            y=short_range_y1,
            mode='lines',
            name='Fit Line 1',
            line=dict(color='red', dash='dash'),
            showlegend=False
        ))

        fig.add_trace(go.Scatter(
            x=short_range_x2,
            y=short_range_y2,
            mode='lines',
            name='Fit Line 2',
            line=dict(color='blue', dash='dash'),
            showlegend=False
        ))

        # Annotate the intersection point with a circle
        fig.add_trace(go.Scatter(
            x=[intersection_x],
            y=[intersection_y],
            mode='markers+text',
            text=[f'({intersection_x:.3f}, {intersection_y:.3f})'],
            textfont=dict(size=22),
            textposition='top left',
            marker=dict(color='green', size=12,symbol='circle'),
            opacity=0.7,
            name='Intersection'
        ))

        return fig

#example usage: 

"""
ab1 = bandgap(hv,age1)
ab2 = bandgap(hv,age2)
ab3 = bandgap(hv,age3)

s=0.5
fig = go.Figure()
fig = ab1.plot(1, 1/3, fig ,label='Annel_Ge1',alpha = s-0.1,color = 'red')
fig = ab2.plot(1, 1/3, fig, label='Annel_Ge2',alpha =s-0.2,color ='green')
fig = ab3.plot(1, 1/3, fig, label='Annel_Ge3',alpha =s-0.3,color ='blue')
fig = ab3.line_fit(3.43,3.54,4.05,4.29,fig)
fig = ab3.line_fit(4.64,4.97,5.27,5.46,fig)
fig.update_layout(title="Annealed_Indirect(Forbidden)_Bandgap")
#fig.update_yaxes(range=[min(age3), None])
name = "anneal.html"
fig.write_html(name)
fig.show()


webbrowser.open(name)
"""

