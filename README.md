# A lightweight module to store and access magnetic field coefficients for Feltor

The repository serves as a storage for often used magnetic field coefficients for Feltor
simulations. Furthermore it provides uniform access to these coefficients
through a python interface.
Together with the simplesimdb module this interface can then be used to
setup and run Feltor simulations that require geometry coefficients on input.

[![LICENSE : MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Installation
We do not yet have an uploaded version on pypi.
To install you have to clone the repository and then use the package manager [pip](https://pip.pypa.io/en/stable/).
> You need python3 (>3.6) to install this module

```bash
git clone https://github.com/feltor-dev/magneticfielddb
cd path/to/magneticfielddb
pip install -e . # editable installation of the module
# ... if asked, cancel all password prompts ...
pytest . # run the unittests
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


## Contributions

Contributions are welcome.
## Authors

Matthias Wiesenberger

