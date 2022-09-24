# nanpa_lookup

Look up callers in the North America Number Plan Adminstrator (NANPA) database. Useful for identifying source of robocalls.

### Usage

Query the database for a number:

    >>> ./lookup.py -n 9072001234 --field company
    GCI COMMUNICATION CORP. DBA GENERAL COMMUNICATION

Or provide a file containing phone numbers:

    >>> ./lookup.py -f numbers.txt --field company
    GCI COMMUNICATION CORP. DBA GENERAL COMMUNICATION
    CELLCO PARTNERSHIP DBA VERIZON WIRELESS - NC
    ONVOY, LLC - TN
    GCI COMMUNICATION CORP. DBA GENERAL COMMUNICATION
    

### Pull Logs from Android

Grab call log for last 30 days from a rooted Android phone via adb:

``` bash
./lookup.py -a 30 --field company | sort | uniq -c
```

```
      1 BANDWIDTH.COM CLEC, LLC - MS
      1 BANDWIDTH.COM CLEC, LLC - TN
     16 BRIGHTLINK COMMUNICATIONS, LLC
      2 CELLCO PARTNERSHIP DBA VERIZON
      1 CENTURYTEL OF LARSEN-READFIELD
      3 CHARTER FIBERLINK-TENNESSEE, L
      1 COMCAST IP PHONE, LLC
      1 GLOBAL CROSSING LOCAL SERVICES
     15 ILLINOIS BELL TEL CO
      2 LEVEL 3 COMMUNICATIONS, LLC - 
      1 MCIMETRO ACCESS TRANSMISSION S
     10 NEW CINGULAR WIRELESS PCS, LLC
      9 No matches found
      8 ONVOY, LLC
      5 ONVOY, LLC - TN
      3 PEERLESS NETWORK OF TENNESSEE,
      4 TELEPORT COMMUNICATIONS AMERIC
      8 T-MOBILE USA, INC.
     16 UNITED STATES CELLULAR - TN
```

### Caveats

This does not work for robocalls which spoof the origin number, only for spammers making use of legitimate numbers from VOIP companies.  This may eventually be addressed by [STIR/SHAKEN](https://en.wikipedia.org/wiki/STIR/SHAKEN).
