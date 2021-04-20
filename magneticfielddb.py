"""Storage and Access to magnetic field coefficients for Feltor """

import json
import os.path
# After two days of trying to get importlib_resources to run I give up on it
# even though it is supposed to be the faster and more modern option
# import importlib_resources as res
import pkg_resources as res

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
    #ref = res.files("magneticfielddb" ).joinpath( os.path.join( "data", path, *paths))

    #with res.as_file(ref) as data_path :
    #    with open( data_path) as data_file :
    #        #print( data_file)
    #        data = json.load( data_file)
    #        return data
    ref = res.resource_string( "magneticfielddb", os.path.join( "data", path, *paths))
    return json.loads( ref)

def files() :
    """ Create a list of available files

    Return:
    list:   A list of file paths relative to path/to/magneticfielddb/data
            of all files in the data repository
            each item in the list can be passed to the select function
    """
    base = "magneticfielddb"
    file_list = list()
    #relpath = res.files("magneticfielddb").joinpath("data")

    def inner_list_files( directory_name, file_list) :
        for f in res.resource_listdir(base,directory_name) :
            if res.resource_isdir(base, os.path.join( directory_name, f) ) :
                inner_list_files( os.path.join( directory_name, f), file_list)
            else :
                file_list.append( os.path.join( os.path.relpath( directory_name, "data"), f) )

    inner_list_files( "data", file_list)
    return file_list
