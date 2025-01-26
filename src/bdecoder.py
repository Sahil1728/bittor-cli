"""
Reference: https://www.bittorrent.org/beps/bep_0003.html
########################################################
By - R Sahil Sharma
########################################################
"""
### TODO: ( we just have to write the reverse logic of bencoder.py ):
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
    result = []
    idx = 0
    # vars for strlen and is_string
    strlen = ""
    buffer = ""
    # import pdb; pdb.set_trace()
    while idx < len(data):
        if buffer == "":
            # here we will get if the buffer is string or not
            while data[idx].isdigit():
                strlen += data[idx]
                idx += 1
            if strlen == "":
                # isn't a string so we just add it to buffer
                buffer = data[idx]
                idx += 1
                continue
            # extracting the string here only
            idx += 1
            buffer = strlen+":"+data[idx:idx+int(strlen)]
            print(buffer)
            value = bdecode(buffer)
            result.append(value)
            buffer = ""
            idx += int(strlen)
        else:
            if data[idx] == "e":
                value = bdecode(buffer+"e")
                result.append(value)
                buffer = ""
                idx += 1
                continue
            else:
                buffer += data[idx]
                idx += 1
        
    return result


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

