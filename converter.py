# -*- coding: utf-8 -*-
"""
Created on Tue Mar  4 09:31:57 2025

@author: Dorian
"""

from enum import Enum

class ConversionType(Enum):
    DEC_TO_BIN = "dec_to_bin"
    DEC_TO_HEX = "dec_to_hex"
    BIN_TO_DEC = "bin_to_dec"
    BIN_TO_HEX = "bin_to_hex"
    HEX_TO_DEC = "hex_to_dec"
    HEX_TO_BIN = "hex_to_bin"

def dec_to_bin(n: int) -> str:
    if n == 0:
        return "0"
    bits = []
    while n > 0:
        bits.append(str(n % 2))
        n //= 2
    return "".join(reversed(bits))

def dec_to_hex(n: int) -> str:
    if n == 0:
        return "0"
    hex_chars = "0123456789ABCDEF"
    digits = []
    while n > 0:
        digits.append(hex_chars[n % 16])
        n //= 16
    return "".join(reversed(digits))

def bin_to_dec(b: str) -> int:
    result = 0
    for bit in b:
        result = result * 2 + int(bit)
    return result

def hex_to_dec(h: str) -> int:
    hex_chars = "0123456789ABCDEF"
    result = 0
    for char in h.upper():
        result = result * 16 + hex_chars.index(char)
    return result

def convert_number(value: str, conversion: ConversionType) -> str:
    if conversion == ConversionType.DEC_TO_BIN:
        return dec_to_bin(int(value))
    
    elif conversion == ConversionType.DEC_TO_HEX:
        return dec_to_hex(int(value))
    
    elif conversion == ConversionType.BIN_TO_DEC:
        return str(bin_to_dec(value))
    
    elif conversion == ConversionType.BIN_TO_HEX:
        return dec_to_hex(bin_to_dec(value))
    
    elif conversion == ConversionType.HEX_TO_DEC:
        return str(hex_to_dec(value))
    
    elif conversion == ConversionType.HEX_TO_BIN:
        return dec_to_bin(hex_to_dec(value))
    
    else:
        raise ValueError("Conversion non supportée.")
