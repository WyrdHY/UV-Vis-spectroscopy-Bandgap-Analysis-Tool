<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bandgap Analysis Using UV-vis Spectra</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 0 2rem;
        }
        h1, h2, h3, h4 {
            color: #333;
        }
        pre {
            background: #f4f4f4;
            padding: 1rem;
            border-radius: 5px;
        }
        code {
            background: #f4f4f4;
            padding: 0.2rem;
            border-radius: 3px;
        }
    </style>
</head>
<body>
    <h1>Bandgap Analysis Using UV-vis Spectra</h1>
    <p>This repository contains a class for optical bandgap measurement analysis using UV-vis spectra. The class, <code>bandgap</code>, allows you to plot bandgap transitions and perform line fitting to determine transition energies.</p>

    <h2>Class Initialization</h2>
    <p>To initialize the <code>bandgap</code> class, you need to provide:</p>
    <ul>
        <li><code>hv</code>: Your photon energy data (in eV).</li>
        <li><code>r</code>: Your reflectance data.</li>
    </ul>
    <pre><code>bg = bandgap(hv, r)</code></pre>

    <h2>Methods</h2>
    <h3>Plot Method</h3>
    <p>The <code>plot</code> method is used to plot the bandgap transitions. You need to provide:</p>
    <ul>
        <li><code>l</code>: Sample thickness. If you only care about the transition energy, the value of <code>l</code> does not matter.</li>
        <li><code>n</code>: The order of the bandgap.</li>
        <ul>
            <li><code>n = 2</code>: Direct allowed transition</li>
            <li><code>n = 2/3</code>: Direct forbidden transition</li>
            <li><code>n = 1/2</code>: Indirect allowed transition</li>
            <li><code>n = 1/3</code>: Indirect forbidden transition</li>
        </ul>
        <li><code>fig</code> (optional): Existing Plotly figure to add the plot to.</li>
        <li><code>label</code> (optional): Label for the plot.</li>
        <li><code>alpha</code> (optional): Opacity of the plot.</li>
        <li><code>color</code> (optional): Color of the plot.</li>
    </ul>
    <pre><code>fig = bg.plot(l, n, fig=None, label=None, alpha=1.0, color=None)</code></pre>

    <h3>Line Fit Method</h3>
    <p>The <code>line_fit</code> method is used to fit lines to two specified ranges and determine their intersection point. You need to provide:</p>
    <ul>
        <li><code>xi</code>: Initial x-value for the first range.</li>
        <li><code>xf</code>: Final x-value for the first range.</li>
        <li><code>xxi</code>: Initial x-value for the second range.</li>
        <li><code>xxf</code>: Final x-value for the second range.</li>
        <li><code>fig</code>: Existing Plotly figure to add the fit lines to.</li>
    </ul>
    <pre><code>fig = bg.line_fit(xi, xf, xxi, xxf, fig)</code></pre>

    <h2>Example Usage</h2>
    <pre><code>
# Example usage of the bandgap class

# Initialize the bandgap instances
ab1 = bandgap(hv, age1)
ab2 = bandgap(hv, age2)
ab3 = bandgap(hv, age3)

# Set sample thickness and opacity
s = 0.5

# Create a Plotly figure
fig = go.Figure()

# Plot the data
fig = ab1.plot(1, 1/3, fig, label='Annel_Ge1', alpha=s-0.1, color='red')
fig = ab2.plot(1, 1/3, fig, label='Annel_Ge2', alpha=s-0.2, color='green')
fig = ab3.plot(1, 1/3, fig, label='Annel_Ge3', alpha=s-0.3, color='blue')

# Perform line fitting
fig = ab3.line_fit(3.43, 3.54, 4.05, 4.29, fig)
fig = ab3.line_fit(4.64, 4.97, 5.27, 5.46, fig)

# Update the layout with a title
fig.update_layout(title="Annealed_Indirect(Forbidden)_Bandgap")

# Save the figure as an HTML file
name = "anneal.html"
fig.write_html(name)

# Show the figure
fig.show()

# Open the HTML file in a web browser
webbrowser.open(name)
    </code></pre>
</body>
</html>
