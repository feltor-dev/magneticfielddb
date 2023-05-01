#!/bin/bash

: ${FELTOR_PATH:="../feltor"}
# If feltor is not here then change the FELTOR_PATH enviromnent variable
# export FELTOR_PATH="path/to/feltor"

make -C $FELTOR_PATH/src/geometry_diag/ geometry_diag

rm -f $2 # in case the file is opened elsewhere
$FELTOR_PATH/src/geometry_diag/geometry_diag $1 $2
