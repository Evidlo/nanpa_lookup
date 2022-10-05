# nanpa_lookup

Look up callers in the North America Number Plan Adminstrator (NANPA) database. Useful for identifying source of robocalls.

### Quickstart

    $ pip install nanpa_lookup

Query the database for a number:

    $ nanpa_lookup -n 9072001234 --field company
    GCI COMMUNICATION CORP. DBA GENERAL COMMUNICATION

Or provide a file containing phone numbers:

    $ nanpa_lookup -f numbers.txt --field company
    GCI COMMUNICATION CORP. DBA GENERAL COMMUNICATION
    CELLCO PARTNERSHIP DBA VERIZON WIRELESS - NC
    ONVOY, LLC - TN
    GCI COMMUNICATION CORP. DBA GENERAL COMMUNICATION
    

### Pull Logs from Android

Grab call log for last 30 days from a rooted Android phone via adb:

``` bash
$ nanpa_lookup -a 30 --field company | sort | uniq -c | sort -n
      3 ONVOY, LLC - TN
      3 PEERLESS NETWORK OF TENNESSEE,
      4 BELLSOUTH TELECOMM INC DBA SOU
      4 TELEPORT COMMUNICATIONS AMERIC
      5 NEW CINGULAR WIRELESS PCS, LLC
      5 ONVOY, LLC
      6 LEVEL 3 COMMUNICATIONS, LLC - 
      9 No matches found
     11 ILLINOIS BELL TEL CO
     27 BRIGHTLINK COMMUNICATIONS, LLC
```

### Usage

```
usage: nanpa_lookup [-h] [-n N] [-f F] [-a A] [--field FIELD] [--query QUERY]
                    [--database DATABASE]

Look up number in NANPA database

options:
  -h, --help           show this help message and exit
  -n N                 number
  -f F                 file containing list of numbers
  -a A                 pull numbers from ADB device
  --field FIELD        print out specific field (company, npanxxy, type, ocn, email)
  --query QUERY        make arbitrary SQL query
  --database DATABASE  numbers database
```

### Caveats

This does not work for robocalls which spoof the origin number, only for spammers making use of legitimate numbers from VOIP companies.  This may eventually be addressed by [STIR/SHAKEN](https://en.wikipedia.org/wiki/STIR/SHAKEN).
