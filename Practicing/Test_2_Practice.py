# Charles Buyas cjb8qf


"""
infile = open("neighbors.txt", "r")
print("Ugly spacing printing the lines of neighbors.txt.")
for line in infile:
    print(line)
infile.close()

print("Next.\n")

print("Printing the lines of neighbors.txt by changing print function end argument.")
infile = open("neighbors.txt", "r")
for line in infile:
    print(line, end="")
infile.close()

infile = open("neighbors.txt", "r")
banana = []
for monkey in infile:
    banana.append(monkey.strip("\n") + "snake")
infile.close()
print(banana)

print("Printing lines of neighbors.txt by right stripping the new line character before printing")
infile = open("neighbors.txt", "r")
for line in infile:
    # line.rstrip("\n")
    line = line.rstrip("\n")
    print(line)
infile.close()


dis_km = input("Enter a distance in kilometers: ")


def kilo_to_miles(banana):
    banana = float(dis_km) * 0.6214
    return banana

print(kilo_to_miles(dis_km))

no_of_ft = int(input("Enter a number of feet: "))


def feet_to_inches(value_input):
    value_input = no_of_ft*12
    return value_input

print(feet_to_inches(no_of_ft))

infile = open('data.txt', 'r')
for line in infile:
    print(line)
infile.close()

name = input("Name a file man: ")
infile = open(name, "r")
line_number = 1
for line in infile:
    print(line_number, end= '')
    print(':', end= ' ')
    line = line.rstrip('\n')
    print(line)
    line_number += 1
infile.close()

ch = input("Enter a digit: ")
if ch.isdigit():
    print("Digit")
else:
    print("No digit")

values.split('$')
print(values)

import re
string =  'The following information will be used for regular expression practice. Susie was born on 04-12-1999 and John
 was born on 10-01-2000'
regex = re.compile(r'\d{2}-\d{2}-\d{4}')
print(regex.findall(string))

re.sub('-', '/', )

KILOMETERS_TO_MILES = 0.6214


def main():
    my_kilometers = float(input("Enter the distance in kilometers: "))

    show_miles(my_kilometers)


def show_miles(kilometers):
    miles = kilometers * KILOMETERS_TO_MILES
    print("The conversion of", format(kilometers, '.2f'), "kilometers")
    print("to miles is", format(miles, '.2f'), "miles.")
main()
"""
