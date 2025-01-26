"""
Reference: https://www.bittorrent.org/beps/bep_0003.html
#############################################
string: <length>:<string>
    EXAMPLES:
        - 4:spam
        - 1:a
#############################################
integer: i<integer>e
    NOTE:
        - <integer> is a decimal number
        - <integer> can be negative
        - i-0e is invalid
        - There can be no leading zeros
    EXAMPLES:
        - i0e               #VALID
        - i-0e              #INVALID
        - i123e             #VALID
        - i-123e            #VALID
        - i1234567890e      #VALID
#############################################
lists: l<elements>e
    NOTE:
        - <elements> is a list of bencoded values
        - <elements> can be of any type
        - <elements> can be empty
        - <elements> can be nested
    EXAMPLES:
        - l4:spam4:eggse        # Corresponds to ['spam', 'egg']
        - l1:a2:b3:ce           # Corresponds to ['a', 'b', 'c'] 
#############################################
dictionaries: d<items>e
    NOTE:
        - KEYS MUST BE STRINGS AND APPEAR IN SORTED ORDER (sorted as raw strings)
        - <items> is a list of key-value pairs
        - <items> can be empty
        - <items> can be nested
        - <items> can be of any type
        - <items> can be of any type
    EXAMPLES:
        - d3:cow3:moo4:spam4:eggse   # Corresponds to {'cow': 'moo', 'spam': 'egg'}
        - d4:spaml1:a1:bee           # Corresponds to {'spam': ['a', 'bee']}

#############################################
"""