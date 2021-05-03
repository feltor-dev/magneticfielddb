#!/bin/bash

: ${FELTOR_PATH:="../feltor"}

make -C $FELTOR_PATH/inc/geometries geometry_diag device=omp

rm -f $2 # in case the file is opened elsewhere
$FELTOR_PATH/inc/geometries/geometry_diag $1 $2
