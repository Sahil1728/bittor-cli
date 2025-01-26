"""
Reference: https://www.bittorrent.org/beps/bep_0003.html
########################################################
By - R Sahil Sharma
########################################################
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