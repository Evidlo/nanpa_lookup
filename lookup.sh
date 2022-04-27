#!/bin/bash
# Evan Widloski - 2020-12-10
# Look up phone registrants in NANPA database

# usage: ./lookup.sh -n 123-456-0987
# usage: ./lookup.sh -f numbers.txt

# look up NPA-NXX code in database
lookup() {
    grep -Fw -f npanxx.txt database.csv | cut -d $'|' -f 4
}

# convert number to NPA-NXX code
parse_number() {
    NUMBER=$(sed 's/-//;s/\+1//' <<< $1)
    echo ${NUMBER:0:3}\|${NUMBER:3:3}\|${NUMBER:6:1}
}

if [[ $1 == "-f" ]]
then
    # lookup list of numbers provided by file
    rm -f npanxx.txt
    while read number
    do
        parse_number $number >> npanxx.txt
    done < "$2"
    lookup
elif [[ $1 == "-n" ]]
then
    # lookup up single number
    parse_number $2 > npanxx.txt
    lookup
elif [[ $1 == "-a" ]]
then
    # pull call log from android
    adb root
    adb pull /data/data/com.android.providers.contacts/databases/contacts2.db
    sqlite3 contacts2.db "SELECT normalized_number FROM calls;" > numbers.txt
    ./lookup.sh -f numbers.txt | sort | uniq -c | sort -n
fi

