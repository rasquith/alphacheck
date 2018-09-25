from codecs import decode
from string import ascii_uppercase
import json


# The letters of the alphabet in uppercase
ALPHA_SET = set(list(ascii_uppercase))


def string_to_set(input_str):
    """Function takes a string and returns a set of its elements
    Args:
        input_str(str)"""
    input_str = decode(input_str, "unicode_escape")
    return(set(list(input_str.upper())))


def has_alphabet(input_str):
    """Function checks if a string contains at least one of each letter of the
    alphabet
    Args:
        input_str(str)
    Returns:
        has_alphabet(bool): True if the string contains the alphabet"""
    input_set = string_to_set(input_str)
    return ALPHA_SET.issubset(input_set)
