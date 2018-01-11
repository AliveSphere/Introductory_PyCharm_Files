# Charles Buyas cjb8qf


roman_numerals = [['M', 1000], ['CM', 900], ['D', 500], ['CD', 400], ['C', 100], ['XC', 90], ['L', 50], ['XL', 40],
                  ['X', 10], ['IX', 9], ['V', 5], ['IV', 4], ['I', 1]]

numeral = int(input("Enter an integer: "))
if 1 <= numeral <= 3999:
    result = ''
    calculate = numeral
    for two in roman_numerals:
        while calculate - two[1] >= 0:
            calculate -= two[1]
            result += two[0]
    print("In roman numerals, " + str(numeral) + " is " + result)
else:
    print("Input must be between 1 and 3999")
