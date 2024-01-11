#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return 0
    sum = 0
    roman_numerals = {'M': 1000, 'D': 500, 'C': 100,
                      'L': 50, 'X': 10, 'V': 5, 'I': 1}
    prev = 0

    for i in reversed(roman_string):
        current = roman_numerals.get(i, 0)

        if current >= prev:
            sum += current
        else:
            sum -= current

        prev = current

    return sum
