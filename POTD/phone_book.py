# Charles Buyas cjb8qf


key1 = input("Add an entry to the phone book: ")
entry1 = key1.split(' ')
key2 = input("Add an entry to the phone book: ")
entry2 = key2.split(' ')
key3 = input("Add an entry to the phone book: ")
entry3 = key3.split(' ')
key4 = input("Add an entry to the phone book: ")
entry4 = key4.split(' ')
key5 = input("Add an entry to the phone book: ")
entry5 = key5.split(' ')
dict1 = {entry1[0]: entry1[1], entry2[0]: entry2[1], entry3[0]: entry3[1], entry4[0]: entry4[1],
         entry5[0]: entry5[1]}
dict2 = {entry1[1]: entry1[0], entry2[1]: entry2[0], entry3[1]: entry3[0], entry4[1]: entry4[0],
         entry5[1]: entry5[0]}
contact = input("\nWho do you want to call?: ")
if contact in dict1.keys():
    print(contact + "'s number is:", dict1[contact])
else:
    print("That name is not in the phone book.")
number = input("\nWhich number do you want to look up?: ")
if number in dict2.keys():
    print("That number belongs to:", dict2[number])
else:
    print("That number is not in the phone book.")
