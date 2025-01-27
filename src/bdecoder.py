"""
Reference: https://www.bittorrent.org/beps/bep_0003.html
########################################################
By - R Sahil Sharma
########################################################
"""
### TODO: ( we just have to write the reverse logic of bencoder.py ):
from typing import Any, Iterable, OrderedDict

# def bdecode_integer(data:str) -> int:
#     # we will get data as i<data>e
#     data = data[1:-1]
#     sign = 1
#     value = 0
#     if data[0] == "-":
#         sign = -1
#         value = int(data[1:])
#     elif data[0] == 0 and len(data) > 1:
#         raise ValueError("Invalid integer format")
#     else:
#         value = int(data)
#     return sign * value

# def bdecode_string(data:str) -> str:
#     # we will get data as <length>:<data>
#     index = data.index(':')
#     length = int(data[:index])
#     index += 1
#     result = data[index:index+length]
#     return result

# def bdecode_list(data:str) -> list:
#     # We will get data as l<data>e
#     data = data[1:-1]  # Remove outer 'l' and 'e'
#     result = []
#     idx = 0
    
#     while idx < len(data):
#         if data[idx].isdigit():  # String
#             colon_idx = data.index(':', idx)
#             length = int(data[idx:colon_idx])
#             string_start = colon_idx + 1
#             string_end = string_start + length
#             result.append(data[string_start:string_end])
#             idx = string_end
#         elif data[idx] == 'i':  # Integer
#             end_idx = data.index('e', idx)
#             result.append(bdecode(data[idx:end_idx + 1]))
#             idx = end_idx + 1
#         elif data[idx] in 'ld':  # List or Dictionary
#             nesting = 1
#             start_idx = idx
#             idx += 1
#             while nesting > 0 and idx < len(data):
#                 if data[idx] in 'ld':
#                     nesting += 1
#                 elif data[idx] == 'e':
#                     nesting -= 1
#                 idx += 1
#             result.append(bdecode(data[start_idx:idx]))
#         else:  # Skip any other character (like 'e')
#             idx += 1
            
#     return result


# def bdecode_dictionary(data:str) -> dict:
#     # We will get data as d<data>e
#     data = data[1:-1]
#     pass

# def get_decode_method(data:str) -> Callable:
#     if data[0] == "i":
#         return bdecode_integer
#     elif data[0] == "l":
#         return bdecode_list
#     elif data[0] == "d":
#         return bdecode_dictionary
#     else:
#         idx = data.index(':')
#         try:
#             length = int(data[:idx])
#         except ValueError:
#             raise ValueError("Invalid string format")
#         else:
#             return bdecode_string



# # func_mapping = {
# #     "i": bdecode_integer,
# #     "l": bdecode_list,
# #     "d": bdecode_dictionary,
# # }
#     # if data[0] in func_mapping:
#     #     ##### type<data>e #####
#     #     func = func_mapping[data[0]]
#     #     result = func(data[1:-1])
#     # elif ':' in data:
#     #     idx = data.index(':')
#     #     try:
#     #         length = int(data[:idx])
#     #         result = bdecode_string(length, data)
#     #     except ValueError:
#     #         raise ValueError("Invalid string format")

# """
# Logic of alternate decoder:
# Use stack
# RULES:
#     - Can only pop l if at top and we get e
#     - Can only pop d if at top and we get e
#     - Can only pop i if at top and we get e
#     - Can only pop <len>: if at top and we get buffer equal to <len>
# """

# nested_pop_rules = {
#     "l": "e",
#     "d": "e",
# }


# def altenate_decoder(data:str) -> Any:
#     stack = []
#     index = 0
#     cur_struct = None
#     while index < len(data):
#         char = data[index]
#         if char == 'l':
#             stack.append([])
#             index += 1
#         elif char == 'd':
#             stack.append({})
#             index += 1
#         elif char == 'i':
#             index += 1
#             end_idx = data.index('e', index)
#             val = bdecode_integer(data[index:end_idx])
#             stack[-1].append(val)
#             index = end_idx + 1
#         elif char.isdigit():
#             col_idx = data.index(':', index)
#             length = int(data[index:col_idx])
#             val = bdecode_string(data[col_idx+1:col_idx+length+1])
#             stack[-1].append(val)
#             index = col_idx+length+1
#         elif char == 'e':
#             completed_struct = stack.pop()
#             if stack:
#                 if isinstance(stack[-1], list):
#                     stack[1].append(completed_struct)
#                 elif isinstance(stack[-1], dict):
#                     if 'key' not in stack[1]:
#                         stack[-1]['key'] = completed_struct
#                     else:
#                         stack[-1][stack[-1]['key']] = completed_struct
#                         del stack[-1]['key']
#             else:
#                 cur_struct = completed_struct
#             index += 1
            
#     return stack[-1]

### COMPLETE RE-WRITE ###

class Decoder:
    def __init__(self, data:bytes):
        self.data = data
        self.index = 0

    def _read(self, i:int) -> bytes:
        """Returns the next i bytes from data"""
        bytes_read = self.data[self.index : self.index + i]
        # update index
        self.index += i
        errr = "Unexpected end of data"
        assert len(bytes_read) == i, f"Not enough bytes to read - {errr}"
        return bytes_read
    
    def _read_till(self, end_char:bytes) -> bytes:
        """Reads bytes till end_char is encountered"""
        try:
            idx = self.data.index(end_char, self.index)
            bytes_read = self.data[self.index:idx]
            self.index = idx + 1
            return bytes_read
        except Exception as e:
            raise Exception(f"Failure while reading till {end_char} - {e}")

    def _method_selector(self) -> object:
        """Selects the method to decode the next section of data and returns the result"""
        cur_char = self.data[self.index:self.index+1]
        # cur_char = chr(self.data[self.index]).encode('utf-8')
        # handling string at first
        if cur_char in [b'1', b'2', b'3', b'4', b'5', b'6', b'7', b'8', b'9', b'0']:
            length_of_string = int(self._read_till(b':'))
            string_data = self._read(length_of_string)
            return string_data
        elif cur_char == b'i':
            # starting of integer
            self.index += 1
            return int(self._read_till(b'e'))
        elif cur_char == b'd':
            return self._read_dict()
        elif cur_char == b'l':
            return self._read_list()
        elif cur_char == b'':
            raise Exception("Unexpected end of file reached")
        else:
            raise Exception(f"Invalid character encountered - {cur_char}")

    def _read_dict(self) -> OrderedDict:
        """Returns ordered dictionary of nested decoded data"""
        dictt = OrderedDict()
        self.index += 1 # skipping d
        dict_key = None
        while self.data[self.index:self.index+1] != b'e':
            if dict_key is None:
                dict_key = self._method_selector()
            else:
                dictt[dict_key] = self._method_selector()
                dict_key = None
        self.index += 1 # skipping e
        return dictt
    

    def _read_list(self) -> list:
        """Returns list of nested decoded data"""
        lst = []
        self.index += 1 # skipping l
        while self.data[self.index:self.index+1] != b'e':
            lst.append(self._method_selector())
        self.index += 1 # skipping e
        return lst
    
    def _decode(self) -> Iterable:
        """Decodes the data and returns an iterable"""
        if self.data[:1] not in  [b'l', b'd']:
            return self._wrap_result_in_tuple()
        else:
            return self._method_selector()

    def _wrap_result_in_tuple(self) -> tuple:
        """Wraps the result in a tuple"""
        l = []
        length = len(self.data)
        while self.index < length:
            l.append(self._method_selector())
        return l[-1]

def bdecode(data:str) -> Any:
    result = None
    # encoding to bytes
    decoder = Decoder(data.encode('utf-8'))
    result = decoder._decode()
    return result