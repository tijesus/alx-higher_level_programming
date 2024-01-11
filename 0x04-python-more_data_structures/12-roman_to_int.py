#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    sum = 0
    roman = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    for roman in reversed(roman_string):
        numeral = roman[roman]
        sum += numeral 
        if sum < numeral * 5:
            sum += numeral
        else:
            sum -= numeral
    return sum

#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    sum = 0
    roman_numerals = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    prev = 0

    for i in reversed(roman_string):
        current = roman_numerals.get(i, 0)

        if current >= prev:
            sum += current
        else:
            sum -= current

        prev = current

    return sum
