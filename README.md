# A lightweight module to store and access magnetic field coefficients for Feltor

The repository serves as a storage for often used magnetic field coefficients for Feltor
simulations. Furthermore it provides uniform access to these coefficients
through a python interface.
Together with the simplesimdb module this interface can then be used to
setup and run Feltor simulations that require geometry coefficients on input.

[![LICENSE : MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Installation
We do not (yet) have an uploaded version on pypi.
Install directly from github:
```bash
pip install git+https://github.com/feltor-dev/magneticfielddb
```
OR clone the repository and then use the package manager [pip](https://pip.pypa.io/en/stable/).
```bash
git clone https://github.com/feltor-dev/magneticfielddb
cd magneticfielddb
pip install . # local installation of the module
pip install .[test] # Install pytest
pytest --capture=tee-sys . # run the unittests
```

In order to locally run the included jupyter-notebooks you can use
```bash
pip install .[jupyter] # Install all necessary dependencies
jupyter-lab # run notebooks
```

## Usage
Here is an example of how we iterate over all files in the data repository
open them into a python dictionaries and display them on stdout.
```python
### example.py ###
import magneticfielddb as mag

# list all files in the data repository
for f in mag.files() :
    # read each file into a dictionary
    coefficients = mag.select( f)
    # print to stdout
    print( coefficients)
```
## Package Notes
- each file contains at least the "equilibrium", "R_0" and "description" fields
- "R_0" is given in units of meter
- "PP" and "PI" are 1 by default
- Files may contain a field "comment" that contains human readable information
string

## Additional Resources

- `polynomial_field.ipynb` is an example notebook of how to fit polynomial coefficients to given equilibrium. Read the doxygen documentation on
   [`dg::geo::createMagneticField`](https://mwiesenberger.github.io/feltor/geometries/html/group__geom.html#gaa0da1d1c2db65f1f4b28d77307ad238b) to find out about valid fields in your `json` file
- `normalize_params.cpp` is a C++ program that should be used on geometry input files (all files with X-points must be normalized such that the X-point closest to the O-point lies on the Psip=0 surface). Compile with `make` and run with `./normalize_params your-params.json your-params.json` to update parameters in-place.
- `OneSizeFitsAllEquilbrium.nb` is a Mathematica notebook that generates solovev coefficients
- `q-profiles.ipynb` is a jupyter notebook that plots q-profiles and flux surfaces for all equilibria in the database using `path/to/feltor/src/geometry_diag/geometry_diag.cpp` and `simplesimdb`
- `geometry_diag.ipynb` is a jupyter notebook that shows how newly made parameters behave in Feltor and how wall and sheath parameters should be setup for a 3d simulation using `path/to/feltor/src/geometry_diag/geometry_diag.cpp` and `simplesimdb`

## Contributions

Contributions are welcome.
## Authors

Matthias Wiesenberger and Markus Held
