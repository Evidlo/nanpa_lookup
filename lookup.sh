#!/bin/bash
# Evan Widloski - 2020-12-10
# Look up phone registrants in NANPA database

# usage: ./lookup.sh -n 123-456-0987
# usage: ./lookup.sh -f numbers.txt

# look up NPA-NXX code in database
lookup() {
    while read -r number
    do
        grep -Fw ${number} database.csv | cut -d $'|' -f 4
    done < npanxx.txt
}

# convert number to NPA-NXX code
parse_number() {
    NUMBER=$(sed 's/-//;s/\+1//' <<< $1)
    echo ${NUMBER:0:3}\|${NUMBER:3:3}\|${NUMBER:6:1}
}

# lookup list of numbers provided by file
if [[ $1 == "-f" ]]
then
    rm -f npanxx.txt
    while read number
    do
        parse_number $number >> npanxx.txt
    done < "$2"
    lookup

# lookup up single number
elif [[ $1 == "-n" ]]
then
    parse_number $2 > npanxx.txt
    lookup

# pull call log from android
elif [[ $1 == "-a" ]]
then
    # filter last N days of calls
    last_N_days=30
    # (current time - 30 days) in milliseconds
    date=$(($(date '+%s000') - (${last_N_days} * 24 * 60 * 60 * 1000)))
    adb root
    # adb pull /data/data/com.android.providers.contacts/databases/contacts2.db
    # sqlite3 contacts2.db "SELECT normalized_number FROM calls;" > numbers.txt
    adb pull /data/data/com.android.providers.contacts/databases/calllog.db
    sqlite3 calllog.db "SELECT normalized_number FROM calls WHERE date >= ${date};" > numbers.txt
    ./lookup.sh -f numbers.txt | sort | uniq -c | sort -n
fi

