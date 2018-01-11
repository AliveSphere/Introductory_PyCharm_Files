# Charles Buyas cjb8qf


num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))
num3 = int(input("Number 3: "))
num4 = int(input("Number 4: "))
num5 = int(input("Number 5: "))
list1 = [num1, num2, num3, num4, num5]
print("\nYou entered:", list1)
avg1 = float((num1+num2+num3+num4+num5)/5)
print("The average is:", avg1)
range1 = max(list1)-min(list1)
print("The range is:", range1)
user1 = int(input("Which item do you want to remove?: "))
list1.remove(user1)
print("\nThe new list has the following values:", list1)
avg2 = float((num1+num2+num3+num4+num5-user1)/4)
print("The average is:", avg2)
range2 = max(list1)-min(list1)
print("The range is:", range2)
