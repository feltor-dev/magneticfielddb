"""Storage and Access to magnetic field coefficients for Feltor"""

import json
import os.path
from contextlib import suppress
from importlib.metadata import PackageNotFoundError, version

from importlib_resources import files as abs_path

with suppress(PackageNotFoundError):
    __version__ = version("magneticfielddb")

def select(path, *paths):
    """Select a file in the data folder

    The file is then opened and its contents returned as a dictionary
    Parameters:
    path, *paths (pathlike): one or more path indicators to a file
        relative to path/to/magneticfielddb/data (forwarded to
        os.path.join(path,*paths) )
    Return:
    dict : A dictionary containing the contents of the chosen file
    """
    # From docu https://importlib-resources.readthedocs.io/en/latest/using.html
    file = abs_path("magneticfielddb").joinpath(os.path.join("magneticfielddb-data", path, *paths))
    return json.loads(file.read_text())


def files():
    """Create a list of available files

    Return:
    list:   A list of file paths relative to path/to/magneticfielddb/data
            of all files in the data repository
            each item in the list can be passed to the select function
    """
    file_list = []

    def inner_list_files(directory_name, file_list):
        for f in abs_path("magneticfielddb").joinpath(directory_name).iterdir():
            if f.is_dir():
                inner_list_files(
                    os.path.relpath(f, abs_path("magneticfielddb")), file_list
                )
            else:
                file_list.append(
                    os.path.relpath(
                        f, os.path.join(abs_path("magneticfielddb"), "magneticfielddb-data")
                    )
                )

    inner_list_files("magneticfielddb-data", file_list)
    return file_list
