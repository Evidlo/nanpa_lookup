#!/bin/bash

# usage: ./lookup.sh 123-456-0987

# download database
if [ ! -f allutlzd.txt ]
then
    wget https://nationalnanpa.com/nanp1/allutlzd.zip
    unzip allutlzd.zip
fi

NUMBER=$(sed 's/-//' <<< $1)
NPANXX=${NUMBER:0:3}-${NUMBER:3:3}

awk -v npanxx=$NPANXX -F $'\t' '$2 == npanxx {print $4}' allutlzd.txt
