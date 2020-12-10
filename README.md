# nanpa_lookup

Look up registrants in North America Number Plan Adminstrator

## quickstart

    git clone http://github.com/evidlo/nanpa_lookup && cd nanpa_lookup
    ./lookup.sh -n 907-200-1234
    
## usage

    # provide a number
    ./lookup.sh -n 907-200-1234
    ./lookup.sh -n 9072001234

    # or provide line separated list of numbers
    ./lookup.sh -f path/to/numbers.txt
    
    # get a list of unique registrants
    ./lookup.sh -f path/to/numbers.txt | sort | uniq
