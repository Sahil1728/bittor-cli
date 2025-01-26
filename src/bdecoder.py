"""
Reference: https://www.bittorrent.org/beps/bep_0003.html

Bencoding format ( we just have to write the reverse logic of bencoder.py ):
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
from typing import Any, Callable

def bdecode_integer(data:str) -> int:
    # we will get data as i<data>e
    data = data[1:-1]
    sign = 1
    value = 0
    if data[0] == "-":
        sign = -1
        value = int(data[1:])
    elif data[0] == 0 and len(data) > 1:
        raise ValueError("Invalid integer format")
    else:
        value = int(data)
    return sign * value

def bdecode_string(data:str) -> str:
    # we will get data as <length>:<data>
    index = data.index(':')
    length = int(data[:index])
    index += 1
    result = data[index:index+length]
    return result

def bdecode_list(data:str) -> list:
    # We will get data as l<data>e
    data = data[1:-1]
    pass

def bdecode_dictionary(data:str) -> dict:
    # We will get data as d<data>e
    data = data[1:-1]
    pass

def get_decode_method(data:str) -> Callable:
    if data[0] == "i":
        return bdecode_integer
    elif data[0] == "l":
        return bdecode_list
    elif data[0] == "d":
        return bdecode_dictionary
    else:
        idx = data.index(':')
        try:
            length = int(data[:idx])
        except ValueError:
            raise ValueError("Invalid string format")
        else:
            return bdecode_string



# func_mapping = {
#     "i": bdecode_integer,
#     "l": bdecode_list,
#     "d": bdecode_dictionary,
# }
    # if data[0] in func_mapping:
    #     ##### type<data>e #####
    #     func = func_mapping[data[0]]
    #     result = func(data[1:-1])
    # elif ':' in data:
    #     idx = data.index(':')
    #     try:
    #         length = int(data[:idx])
    #         result = bdecode_string(length, data)
    #     except ValueError:
    #         raise ValueError("Invalid string format")


def bdecode(data:str) -> Any:
    result = None
    decode_method = get_decode_method(data)
    result = decode_method(data)
    return result

