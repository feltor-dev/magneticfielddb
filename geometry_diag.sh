#!/bin/bash

make geometry_diag device=cpu

rm -f $2 # in case the file is opened elsewhere
./geometry_diag $1 $2
