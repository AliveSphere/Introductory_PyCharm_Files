# Charles Buyas cjb8qf


value = input("Input your scores, separated by spaces: ")
list1 = value.split(' ')
list1 = [int(x) for x in list1]

total = float(sum(list1))
base = float(len(list1))
avg = total/base
print("Average:", format(avg, ".3f"))

if 98.000 <= avg <= 100.000:
    print("Letter: A+")
elif 93.000 <= avg <= 97.999:
    print("Letter: A")
elif 90.000 <= avg <= 92.999:
    print("Letter: A-")
elif 87.000 <= avg <= 89.999:
    print("Letter: B+")
elif 83.000 <= avg <= 86.999:
    print("Letter: B")
elif 80.000 <= avg <= 82.999:
    print("Letter: B-")
elif 77.000 <= avg <= 79.999:
    print("Letter: C+")
elif 73.000 <= avg <= 76.999:
    print("Letter: C")
elif 70.000 <= avg <= 72.999:
    print("Letter: C-")
elif 67.000 <= avg <= 69.999:
    print("Letter: D+")
elif 63.000 <= avg <= 66.999:
    print("Letter: D")
elif 60.000 <= avg <= 62.999:
    print("Letter: D-")
else:
    print("Letter: F")
