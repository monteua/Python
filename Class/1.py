'''
Write a Python class to convert an integer to a roman numeral.
'''

class romanNumeral:
    def num_to_roman(self, num):
        numbers = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        romans = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]

        roman_number = ''
        i = 0

        while num > 0:
            for x in range(num // numbers[i]):
                roman_number += romans[i]
                num -= numbers[i]
            i += 1
        return roman_number

print (romanNumeral().num_to_roman(2017))