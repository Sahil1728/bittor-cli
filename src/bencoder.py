"""
Reference: https://www.bittorrent.org/beps/bep_0003.html

Bencoding format:
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


def bencode_string(s: str) -> str:
    length = len(s)
    return f"{length}:{s}"


def bencode_integer(i: int) -> str:
    sign = ""
    if i < 0:
        sign = "-"
    return f"i{sign}{i}e"

def bencode_list(l: list) -> str:
    base_string = "l"
    for element in l:
        if isinstance(element, str):
            base_string += bencode_string(element)
        elif isinstance(element, int):
            base_string += bencode_integer(element)
        elif isinstance(element, list):
            base_string += bencode_list(element)
        elif isinstance(element, dict):
            base_string += bencode_dictionary(element)
    return base_string + "e"


def bencode_dictionary(d: dict) -> str:
    base_string = "d"
    for key, value in sorted(d.items()):
        base_string += bencode_string(key)
        if isinstance(value, str):
            base_string += bencode_string(value)
        elif isinstance(value, int):
            base_string += bencode_integer(value)
        elif isinstance(value, list):
            base_string += bencode_list(value)
        elif isinstance(value, dict):
            base_string += bencode_dictionary(value)
    return base_string + "e"


def bencode(data) -> str:
    result = None
    if isinstance(data, str):
        result = bencode_string(data)
    elif isinstance(data, int):
        result = bencode_integer(data)
    elif isinstance(data, list):
        result = bencode_list(data)
    elif isinstance(data, dict):
        result = bencode_dictionary(data)
    return result