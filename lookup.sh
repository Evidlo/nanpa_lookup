#!/bin/bash
# Evan Widloski - 2020-12-10
# Look up phone registrants in NANPA database

# usage: ./lookup.sh -n 123-456-0987
# usage: ./lookup.sh -f numbers.txt

# download database
if [ ! -f allutlzd.txt ]
then
    wget https://nationalnanpa.com/nanp1/allutlzd.zip
    unzip allutlzd.zip
fi

# look up NPA-NXX code in database
lookup() {
    grep -Fw -f npanxx.txt allutlzd.txt | cut -d $'\t' -f 4
}

# convert number to NPA-NXX code
parse_number() {
    NUMBER=$(sed 's/-//' <<< $1)
    echo ${NUMBER:0:3}-${NUMBER:3:3}
}

if [[ $1 == "-f" ]]
then
    rm -f npanxx.txt
    while read number
    do
        parse_number $number >> npanxx.txt
    done < "$2"
    lookup
else
    parse_number $2 > npanxx.txt
    lookup
fi

