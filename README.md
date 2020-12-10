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

    >>> ./lookup.sh -f path/to/numbers.txt | sort | uniq
    "GCI COMMUNICATION CORP. DBA GENERAL COMMUNICATION"
    "CELLCO PARTNERSHIP DBA VERIZON WIRELESS - NC"
    "ONVOY, LLC - TN"
