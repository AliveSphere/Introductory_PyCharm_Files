# Charles Buyas cjb8qf


import re

# below I find patterns of text without the use of regular expressions


def is_phone_number(banana):
    if len(banana) != 12:
        return False
    for digits in range(0, 3):
        if not banana[digits].isdecimal():
            return False
    if banana[3] != '-':
        return False
    for digits in range(4, 7):
        if not banana[digits].isdecimal():
            return False
    if banana[7] != '-':
        return False
    for digits in range(8, 12):
        if not banana[digits].isdecimal():
            return False
    return True


message = 'You can call me at 444-555-6969. 420-666-8888 is my office phone number.'
print(message)
for text in range(len(message)):
    cake_batter = message[text: text+12]
    if is_phone_number(cake_batter):
        print("Phone number found: " + cake_batter)
print('Done\n')

"""
what I have below accomplishes the same task
as the above code, just in fewer lines
"""

# below I find patterns of text with the use of regular expressions
# I added "import re" to the top of the file in order to use the re module
# re.compile creates a regular expression object
phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# below I use match_objects as my variable name, but mo is a commonly used generic name for match objects
# using the search function, I find the first mo that satisfies my conditions
# I then use the .group() method since I know there will be a mo in whatever I'm searching
match_objects = phone_num_regex.search('My number is 420-666-6969.')
print("First phone number found: " + match_objects.group())
# below, I have done something similar, except I instead use .findall()
# .findall() searches through a string for all accounts of whatever I specify
# .findall() then turns all of the iterations that pass into a list
# I can then print out the list
multiple_match_objects = phone_num_regex.findall('My number is 420-666-6969. My office number is 420-666-8888.')
print("All phone number(s) found:", multiple_match_objects, '\n')

"""
now I start to try different kinds of grouping and searching methods
"""

new_phone_num_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = new_phone_num_regex.search('My phone number is 420-666-6969.')
multiple_mo = new_phone_num_regex.findall('My phone number is 420-666-6969. Office: 555-123-4567.')
print("Group 1 is: " + mo.group(1))
print("Group 2 is: " + mo.group(2))
print("To show all groups, I type mo.groups(), and the result is:", mo.groups())
print("Using .findall() instead of .search(), I get a list of lists:", multiple_mo)

# Since lists are order based, I can name certain parts of the list and print them separately.
area_code, main_number = mo.groups()
print(area_code)
print(main_number, '\n')

# below I try separating the numbers on a different format
parentheses_phone_num_regex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = parentheses_phone_num_regex.search('My phone number is (420) 666-6969.')
print(mo.group(1))
print(mo.group(2), '\n')

# below I reveal the use of the pipe character "|" to match multiple groups
hero_regex = re.compile(r'Batman|Tina Fey')
mo_1 = hero_regex.search("Batman and Tina Fey are my heroes.")
print(mo_1.group())
mo_2 = hero_regex.search('Tina Fey and Batman are heroes.')
print(mo_2.group(), '\n')

# below I use | to search for certain patterns as *part* of my regex
bat_regex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = bat_regex.search('Batmobile lost a wheel.')
print(mo.group())
print(mo.group(1), '\n')

# below I attempt to do the same, but with multiple instances
bat_regex = re.compile(r'Bat(man|mobile|copter|bat)')
line = "Batman said the Batmobile lost a wheel."
for x in range(len(line)):
    mo_bat = bat_regex.findall(line)
    print(mo_bat[x])
