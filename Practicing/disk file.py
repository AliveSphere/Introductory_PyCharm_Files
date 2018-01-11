# Charles Buyas cjb8qf


# Simulate reading to end of disk file


data = ["Jim", 88, "John", 92, "Joe", 78, "EOF"]
index = 0
total = 0
output = ""
"""
A while loop is preceded by a priming input.
Then while loop header.
It will then perform some sort of task, as many times as we give it a proper input.
The loop will continue to perform this priming input -> task, until it hits some part of coding that
denotes the program should stop looping.
"""
read = data[index]          # priming input
while read != "EOF":        # while loop header
    # data[index + 1] validated before placement in the list
    score = data[(index+1)]
    output += format(read, "20") + str(score) + "\n"
    total += score
    index += 2
    read = data[index]
if index > 0:
    print(output)
    # Calculate the average and print it. Note integer division
    print(format(total/(index//2), "24.1f"))
