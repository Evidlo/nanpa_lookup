# nanpa_lookup

Look up callers in the North America Number Plan Adminstrator (NANPA) database. Useful for identifying source of robocalls.

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
    

### Pull Logs from Android

Grabs call log for last 30 days from a rooted Android phone via adb:

``` bash
./lookup.sh -a
```

```
      1 AIRUS, INC. - AL
      1 AIRUS, INC. - SD
      1 BANDWIDTH.COM CLEC, LLC - TN
      1 BELLSOUTH TELECOMM INC DBA SOU
      1 ONVOY, LLC - AL
      1 ONVOY, LLC - GA
      1 ONVOY, LLC - MD
      1 ONVOY, LLC - MO
      1 ONVOY, LLC - TX
      1 ONVOY, LLC - UT
      1 ONVOY, LLCV - MI
      1 ONVOY, LLC - WA
      1 ONVOY, LLC - WY
      1 PEERLESS NETWORK OF GEORGIA, L
      1 PEERLESS NETWORK OF INDIANA, L
      1 PEERLESS NETWORK OF MISSOURI, 
      1 PEERLESS NETWORK OF NORTH CARO
      2 LEVEL 3 COMMUNICATIONS, LLC - 
      2 ONVOY, LLC - AR
      2 ONVOY, LLC - MT
      5 ONVOY, LLC
     17 NEW CINGULAR WIRELESS PCS, LLC
     19 ONVOY, LLC - TN
     22 T-MOBILE USA, INC.
```

### Caveats

This does not work for robocalls which spoof the origin number, only for spammers making use of legitimate numbers from VOIP companies.  This may eventually be addressed by [STIR/SHAKEN](https://en.wikipedia.org/wiki/STIR/SHAKEN).
