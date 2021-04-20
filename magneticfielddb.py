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
    data = "magneticfielddb.data"
    ref = res.files(data ).joinpath( os.path.join( path, *paths))

    with res.as_file(ref) as data_path :
        with open( data_path) as data_file :
            #print( data_file)
            data = json.load( data_file)
            return data

def files() :
    """ Create a list of available files

    Return:
    list:   A list of file paths relative to path/to/magneticfielddb/data
            of all files in the data repository
            each item in the list can be passed to the select function
    """
    data = "magneticfielddb.data"
    file_list = list()
    relpath = res.files(data).joinpath("")

    def inner_list_files( traversable, file_list) :
        for f in traversable.iterdir() :
            if f.is_dir() :
                inner_list_files( f, file_list)
            else :
                file_list.append( f.relative_to(relpath) )

    inner_list_files( relpath, file_list)
    return file_list
