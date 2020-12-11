# nanpa_lookup

Look up callers in the North America Number Plan Adminstrator (NANPA) database. Useful for identifying source of robocalls.

### Quickstart (Android)

Grabs the call log from Android dialer and counts number of calls from each registrant in the database.

Requires `adb`, `sqlite3` and a rooted phone.

``` bash
git clone http://github.com/evidlo/nanpa_lookup && cd nanpa_lookup
adb root
adb pull /data/data/com.android.providers.contacts/databases/contacts2.db
sqlite3 contacts2.db "SELECT normalized_number FROM calls;" > numbers.txt
./lookup.sh -f numbers.txt | sort | uniq -c | sort -n
```
    
For example, here are the top few companies with the largest number of calls to my cell:

```
    643 "CELLCO PARTNERSHIP DBA VERIZON WIRELESS - GA"              
    665 "OMNIPOINT COMMUNICATIONS, INC. - NY"                       
    666 "LEVEL 3 COMMUNICATIONS, LLC - CA"                          
    713 "CELLCO PARTNERSHIP DBA VERIZON WIRELESS - MI"              
    754 "ONVOY, LLC - CA"                                           
    776 "CELLCO PARTNERSHIP DBA VERIZON WIRELESS - FL"              
    818 "CELLCO PARTNERSHIP DBA VERIZON WIRELESS - OH"              
    848 "CELLCO PARTNERSHIP DBA VERIZON WIRELESS - TX"              
    903 "CELLCO PARTNERSHIP DBA VERIZON WIRELESS - NY"              
   1495 "CELLCO PARTNERSHIP DBA VERIZON WIRELESS - CA"              
   2605 "NEW CINGULAR WIRELESS PCS, LLC - DC"                       
   3408 "NEW CINGULAR WIRELESS PCS, LLC - GA"                       
   5448 "NEW CINGULAR WIRELESS PCS, LLC - IL" 
```

Onvoy LLC, Level 3 Communications, and Omnipoint Communications are all VOIP companies.

### Usage

Query the database for a number:

    >>> ./lookup.sh -n 907-200-1234
    "GCI COMMUNICATION CORP. DBA GENERAL COMMUNICATION"
    >>> ./lookup.sh -n 9072001234
    "GCI COMMUNICATION CORP. DBA GENERAL COMMUNICATION"

Or provide a file containing phone numbers:

    >>> ./lookup.sh -f path/to/numbers.txt
    "GCI COMMUNICATION CORP. DBA GENERAL COMMUNICATION"
    "CELLCO PARTNERSHIP DBA VERIZON WIRELESS - NC"
    "ONVOY, LLC - TN"
    "GCI COMMUNICATION CORP. DBA GENERAL COMMUNICATION"
    
### Exporting calls from Android

Download contacts database

    adb shell "su -c 'cat /data/data/com.android.providers.contacts/databases/contacts2.db'" > contacts2.db

Dump all calls to numbers.txt.  Filter out long conversations that are obviously not spam

    sqlite3 contacts2.db "SELECT normalized_number FROM calls WHERE duration <= 1;" > numbers.txt

### Caveats

This does not work for robocalls which spoof the origin number, only for spammers making use of legitimate numbers from VOIP companies.  This may eventually be addressed by [STIR/SHAKEN](https://en.wikipedia.org/wiki/STIR/SHAKEN).
