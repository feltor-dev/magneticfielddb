#!/bin/bash

: ${FELTOR_PATH:="../feltor"}

make -C $FELTOR_PATH/inc/geometries geometry_diag device=omp

$FELTOR_PATH/inc/geometries/geometry_diag $1 $2
