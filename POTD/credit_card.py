# Charles Buyas cjb8qf


ccn = input("Type a credit card number (just digits): ")
ccn2 = ccn
ccn.split()
list1 = list(ccn)
total1 = 0
total2 = ""
total3 = 0
for ccn in range(len(ccn) - 1, -1, -2):
    sum1 = int(list1[ccn])
    del list1[ccn]
    total1 += sum1
list2 = [int(i)*2 for i in list1]

i = 0
while i < len(list2):
    total2 += str(list2[i])
    i += 1

total2.split()
list3 = list(total2)
j = 0
while j < len(list3):
    total3 += int((list3[j]))
    j += 1

total4 = total1 + total3
if total4 % 10 == 0:
    print("Yes,", ccn2, "is a valid credit card number")
else:
    print(ccn2, "is not a valid credit card number")
