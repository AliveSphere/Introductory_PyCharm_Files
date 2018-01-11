# Charles Buyas cjb8qf


output = ""
total = 0
count = 0
name = input("Please enter a name, -1 to exit the loop: ")  # priming input
while name != "-1":                                         # -1 is sentinel value (can be anything)
    try:
        score = int(input("Please enter " + name + "'s score between 0 and 100: "))
        if 0 <= score <= 100:
            name = format(name, "20")
            # output defined above loop, used here
            output += name + str(score) + "\n"
            total += score                                  # total defined above loop used here
            count += 1
            # Must repeat the priming input
            name = input("Please enter a name, -1 to exit the loop: ")
        else:
            print("Score must be between 0 and 100, inclusive")
    except ValueError:
        print("There was an error with the input score! Enter integers only! ")
if count > 0:
    print(output)
    print("The average score is", format(total/count, ".1f"))
