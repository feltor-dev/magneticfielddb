import pytest
import magneticfielddb as mag
import os.path

# Run with pytest --capture=tee-sys . to see stdout output

def test_selection () :
    print ( "TEST SELECTION")
    m = mag.select( "COMPASS", "compass_1X.json")
    m = mag.select( os.path.join("COMPASS", "compass_1X.json"))
    print( m)

def test_list() :
    print ( "TEST LIST")

    #test listing
    for p in mag.files() :
        print( p )
    #test if list can be selected
    for p in mag.files() :
        m = mag.select(p)
        print(m)


