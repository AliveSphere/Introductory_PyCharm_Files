# Charles Buyas cjb8qf


prompt = "You know as soon as you answer this question it will be all over\n"\
 "the Internet, so I suggest you fabricate. How much do you weigh? "
try:
    weight = float(input(prompt))
    choice = int(input("Please enter the NUMBER of your planetary choice:\n1. Venus\n2. Mars\n3. Jupiter\n4. Saturn "))
    output = "Your weight would be "
    if choice == 1:
        output += str((.78 * weight)) + "."
    elif choice == 2:
        output += str((.39 * weight)) + "."
    elif choice == 3:
        output += str((2.65 * weight)) + "."
    elif choice == 4:
        output += str((1.17 * weight)) + "."
    else:
        output += "undetermined"
    print(output)
except ValueError:
    print("The input must be an integer such as 100, 90, 1, 2, 3 or 4")
