#!/usr/bin/python3
def roman_to_int(roman_string):
    rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    prev_val = 0

    if type(roman_string) is str and roman_string:
        for c in range(len(roman_string) - 1, -1, -1):
            if rom_val[roman_string[c]] >= prev_val:
                result += rom_val[roman_string[c]]
            else:
                result -= rom_val[roman_string[c]]
            p = rom_val[roman_string[c]]

    return result
