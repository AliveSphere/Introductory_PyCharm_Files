# Charles Buyas cjb8qf


# This program uses a Comma Separated Value file of names and meanings to report the meaning of a name.

# input a .csv file of names and meanings
# output a dictionary of names and meanings

# Write a function called load_names_file_as_dict that takes a file name parameter
# The file sent to this function is a .csv file of name, meaning pairs.  The names
# are all capital letters.  The function reads each line from the file and adds
# the name meaning pair to the dictionary using the stripped name as the key.  Close
# the file and return the dict to the caller.


def load_names_file_as_dict(file_name):
    names_file = open(file_name, "r")
    names = {}
    for line in names_file:
        temp = line.split(",")
        names[temp[0]] = temp[1].strip()
    names_file.close()
    return names


def main():
    names = load_names_file_as_dict("names_csv.py")
    name_lookup = input("Please enter a name to look up or simply press enter to quit: ")
    while name_lookup != "":
        meaning = names.get(name_lookup.upper(), name_lookup + " not found.")
        if meaning != name_lookup + " not found.":
            print(name_lookup + " means " + meaning + ".")
        else:
            print(meaning)
        name_lookup = input("Please enter a name to look up or simply press enter to quit: ")


main()
