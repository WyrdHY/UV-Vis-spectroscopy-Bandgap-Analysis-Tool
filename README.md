# Bandgap Analysis Using UV-vis Spectra

This class is for optical bandgap measurement analysis using UV-vis Spectra. To initiate this class:

- `hv`: You must convert your wavelength (nm) into photon energy (eV).
- `r`: Your reflectance data.

## Method: Plot

To use this method, you need to provide:

- `l`: Your sample thickness (if you only care about the transition energy, the value of `l` does not matter).
- `n`: The order of the bandgap.
  - `n = 2`: Direct allowed transition
  - `n = 2/3`: Direct forbidden transition
  - `n = 1/2`: Indirect allowed transition
  - `n = 1/3`: Indirect forbidden transition
- *Direct* means electron + photon.
- *Indirect* means electron + photon + phonon.
