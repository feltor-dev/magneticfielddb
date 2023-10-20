"""Storage and Access to magnetic field coefficients for Feltor """

import json
import os.path
import importlib_resources as res

def select( path, *paths) :
    """ Select a file in the data folder

    The file is then opened and its contents returned as a dictionary
    Parameters:
    path, *paths (pathlike): one or more path indicators to a file
        relative to path/to/magneticfielddb/data (forwarded to
        os.path.join(path,*paths) )
    Return:
    dict : A dictionary containing the contents of the chosen file
    """
    ref = res.files( "magneticfielddb").joinpath(os.path.join("data",path,*paths))
    return json.loads( ref.read_text())

def files() :
    """ Create a list of available files

    Return:
    list:   A list of file paths relative to path/to/magneticfielddb/data
            of all files in the data repository
            each item in the list can be passed to the select function
    """
    file_list = list()

    def inner_list_files( directory_name, file_list) :
        for f in res.files( "magneticfielddb").joinpath(directory_name ).iterdir():
            if res.files( "magneticfielddb").joinpath( os.path.join( directory_name, f)).is_dir():
                inner_list_files( os.path.join( directory_name, f), file_list)
            else :
                file_list.append( os.path.join( os.path.relpath( directory_name, "data"), f) )

    inner_list_files( "data", file_list)
    return file_list
