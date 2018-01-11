# Charles Buyas cjb8qf


"""

The folk rule:
As young as (1/2 * age) + seven
As old as (2 * age) - thirteen
I used a double divide sign in order to make it a clean division and get rid of the decimal point

"""

num1 = int(input("How old are you? "))
if num1 >= 14:
    print("You can date people between", str((num1//2) + 7), "and", str((2*num1) - 13), "years old")
else:
    print("You shouldn't be dating yet!")
