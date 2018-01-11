# Charles Buyas cjb8qf


"""
Write a program that for integers between 1
and 100, inclusive, outputs AppleOrange if the
integer is a multiple of 3 and 5, outputs Apple if
the integer is a multiple of 3, outputs Orange if
the integer is a multiple of 5, otherwise outputs
the integer. Arrange the output in six columns.
"""

number = int(input("enter number "))
if number in range(15, 101, 15):
    print("AppleOrange")
elif number in range(3, 101, 3):
    print("Apple")
elif number in range(5, 101, 5):
    print("Orange")
else:
    print(number)

number = int(input("\nEnter a number between 1 and 100: "))

if 1 <= number <= 100:
    if number % 3 == 0 and number % 5 == 0:
        print("AppleOrange")
    elif number % 3 == 0:
        print("Apple")
    elif number % 5 == 0:
        print("Orange")
    else:
        print(number)
else:
    print("ValueError.")

l1 = [2, 4, 6, 8, 10]

for i in range(len(l1)):
    print(l1[i])
    print(i)

x = True

while x is True:
    inp = input("enter something")
    print("the statement is true")
    if inp == "fucking turn this off":
        x = False

"""
Try doctor phil
Text based RPG: making choices
"""
