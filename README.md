\# Bandgap Analysis Using UV-vis Spectra

## To initiate this class:
- `hv` - you must convert your wavelength (nm) into photon energy (eV).
- `r` - your reflectance data.

## Method: Plot
To use this method, you need to provide:
- `l` - your sample thickness (but if you only care about the transition energy, `l`'s value does not matter).
- `n` - the order of the bandgap:
  - `n = 2` - direct allowed transition
  - `n = 2/3` - direct forbidden transition
  - `n = 1/2` - indirect allowed transition
  - `n = 1/3` - indirect forbidden transition
- *Direct* means electron + photon.
- *Indirect* means electron + photon + phonon.

## Method: Line_fit
To use this method, you need to provide:
- `(xi, xf)` - these two are used to fit the first line.
- `(xxi, xxf)` - these two are used to fit the second line.
- `fig` - provide the figure you want to overlay on to show the bandgap.

Once these four parameters are given, it will automatically fit and find the intersection and display it on the graph. You can call this method multiple times if there are multiple bandgaps. However, you must run `Plot` first before `Line_fit`.
