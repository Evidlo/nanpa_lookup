# Nanpa_lookup

Look up registrants in North America Number Plan Adminstrator.

Useful for identifying source of robocalls.

## Quickstart

    git clone http://github.com/evidlo/nanpa_lookup && cd nanpa_lookup
    ./lookup.sh -n 907-200-1234
    
## Usage

Provide a number:

    >>> ./lookup.sh -n 907-200-1234
    "GCI COMMUNICATION CORP. DBA GENERAL COMMUNICATION"
    >>> ./lookup.sh -n 9072001234
    "GCI COMMUNICATION CORP. DBA GENERAL COMMUNICATION"

Or provide line separated list of numbers:

    >>> ./lookup.sh -f path/to/numbers.txt
    "GCI COMMUNICATION CORP. DBA GENERAL COMMUNICATION"
    "CELLCO PARTNERSHIP DBA VERIZON WIRELESS - NC"
    "ONVOY, LLC - TN"
    "GCI COMMUNICATION CORP. DBA GENERAL COMMUNICATION"
    
Get a list of unique registrants:

    >>> ./lookup.sh -f path/to/numbers.txt | sort | uniq -c | sort -n
    "GCI COMMUNICATION CORP. DBA GENERAL COMMUNICATION"
    "CELLCO PARTNERSHIP DBA VERIZON WIRELESS - NC"
    "ONVOY, LLC - TN"
    
## Exporting calls from Android

Download contacts database

    adb shell "su -c 'cat /data/data/com.android.providers.contacts/databases/contacts2.db'" > contacts2.db

Dump all calls to numbers.txt

    sqlite3 contacts2.db "SELECT normalized_number FROM calls WHERE duration==0;" > numbers.txt
