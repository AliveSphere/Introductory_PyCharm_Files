# Craig Dill (cd9au)
# This program demonstrates functions and exception handling while performing
# file processing operations.  File operations are presented menu style.
import os       # os service needed for deleting and renaming files


# Global constant variables for status
STATUS_GOOD = 0
STATUS_BAD = -1
# The main method drives the program calling the other functions.


def main():
    status = STATUS_GOOD  # status contains 0 when no exceptions occur, -1 if exception occurs
    choice = 0
    while status == STATUS_GOOD and choice < 9:
        choice = menu()             # Pick up a choice 1 through 8 to process the file
        if choice == 1:
            status = read_file()
        elif choice == 2:
            status = read_file_record()
        elif choice == 3:
            status = modify_file()
        elif choice == 4:
            status = delete_record()
        elif choice == 5:
            status = append_file()
        elif choice == 6:
            status = create_file()
        elif choice == 7:
            status = copy_file("copy", "", "")
        elif choice == 8:
            status = delete_file()
        # if choice > 8 would not be in the loop so else catches choice 8


def menu():
    choice = 0
    while choice == 0:
        try:        # Numeric user input can always throw an exception so handled with try/except
            choice = int(input("Please enter the NUMBER of your selection:\n\n1. Read file records\n"
                               "2. Read a file record\n3. Change a file record\n4. Delete a file record\n"
                               "5. Add file records\n6. Create a file\n7. Copy a file\n8. Delete a file\n"
                               "9. Exit program\n\tMy selection is: "))
            if choice < 1 or choice > 9:
                choice = 0      # if choice outside valid range, force another loop iteration
        except ValueError:      # reach here if user entered something like one instead of 1
            print("Please enter the NUMBER 1, 2, 3, 4, 5, 6, 7, 8 or 9")
            choice = 0
    return choice


def read_file():
    # getting the file name is common to all the menu operations, so placed in a function for code reuse
    file_name = get_file_name("Please enter the file name to read.")
    # openning files is common to all the menu operations so placed in a function for code reuse
    status = open_file(file_name, "r")  # open_file() returns -1 if exception encountered else file object
    if status != -1:                    # perform these operations if file opened successfully
        infile = status
        data = infile.read()            # read and print all the data
        print(data)
        infile.close()                  # only close the file if it was successfully opened
        status = STATUS_GOOD                      # send back success
    return status                       # or send back failure if file did not open when called open_file


# Read a file record by searching for it.  This is more practical if the file were set up
# as records, but it is not.
def read_file_record():
    file_name = get_file_name("Please enter the file name containing the record.")
    search_value = ""           # get the value to look for in the file, possible the first item in a record
    while search_value == "":   # or a key of a key value pair to place in a dictionary
        search_value = input("Please enter the record (key) you want to find: ")
    status = open_file(file_name, "r")  # open_file returns the file object reference or -1
    if status != -1:
        infile = status
        found = False
        try:                    # reading a line from a file might cause an IOError exception. Handle it.
            line = infile.readline()
            while found is False and line != "":    # search while not found and not end of file
                if line.rstrip("\n").lower() == search_value.lower():
                    print(line.rstrip("\n") + " found!")
                    found = True
                line = infile.readline()    # forgetting this line in a while loop causes infinite looping
            if not found:
                print(search_value + " not found.")
            status = STATUS_GOOD      # Not found is still good status, 0 reflects no exceptions
        except IOError:
            print("An error occurred searching file " + file_name)
            status = STATUS_BAD     # Exceptions are bad, this program handles the exceptions and exits.
        infile.close()      # Can't close the file if there was an exception, maybe file never opened
    return status


# modify_file relies on copy_file() for the bulk of the work, so it calls copy_file for code reuse
# The only difference between modify and copy file is a particular record is changed, everything else
# is still copied.  Behind the scenes however, is different.  Modifying a file uses a second file
# just as copying does, but when modifying a record in the file all lines not changing are copied
# directly to the second (hidden) file, the modified line is copied to the (hidden) file, then
# the remainder of the unmodified records are copied.  When all lines are copied, the original
# file is deleted and the (hidden) file is renamed to the original file's name.  This is done in
# copy_file.
def modify_file():
    replace = input("Please enter the information to replace: ")
    replacement = input("Please enter the replacement information: ")
    replace = str(replace)          # This is here in case the replace value is numeric
    replacement = str(replacement)
    status = copy_file("modify", replace, replacement)  # copy_file requires 3 arguments
    return status                                       # operation, replace value, replacement value


# Function delete record utilizes copy_file similarly to the way modify_file uses it.
def delete_record():
    delete = input("Please enter the information to delete: ")
    delete = str(delete)
    status = copy_file("delete", delete, "")    # No replacement value, just deleting
    return status


# Function create_file only creates the file and does not permit addition of records.  The file
# is populated using append_file
def append_file():
    file_name = get_file_name("Please enter the file name to append. ")
    status = open_file(file_name, "a")      # get the file object reference or -1
    outfile = status
    if status != -1:
        try:
            str_data = input("Please enter file record, -1 to quit entering data: ")
            while str_data != "-1":
                if str_data == str(str_data):       # is the input already string?
                    outfile.write(str_data + "\n")  # yes
                else:
                    outfile.write(str(str_data) + "\n")  # make it string
                str_data = input("Please enter file record, -1 to quit entering data: ")
            status = STATUS_GOOD
            outfile.close()     # only close the file if it opened
            print("File appended.")
        except IOError:         # .write can throw an IOError exception
            print("An error occurred attempting to add records to file " + file_name)
            status = STATUS_BAD
        outfile.close()
    return status


def create_file():
    file_name = get_file_name("Please enter the file name to create.")
    status = open_file(file_name, "w")      # get the file object reference or -1 from open_file()
    if status != -1:                        # if it opened, it is created, close it and let append populate it
        outfile = status
        outfile.close()
        status = STATUS_GOOD
        print("File created.")
    return status


# copy_file performs file copying, modifying, and record deleting
def copy_file(operation, replace, replacement):
    source_file_name = get_file_name("Please enter name of source file.")
    if operation == "copy":
        dest_file_name = get_file_name("Please enter name of destination file: ")
    else:
        dest_file_name = "temp.txt"     # hidden temp file for modifying and deleting records
    status = STATUS_GOOD
    source_file = open_file(source_file_name, "r")
    if source_file != -1:               # only open the destination file if the source opened
        dest_file = open_file(dest_file_name, "w")
        if source_file != -1 and dest_file != -1:   # if both source and destination opened
            try:
                count = 0               # count is here to determine if deleted or modified record found
                line = source_file.readline()
                while line != "":
                    if line.strip("\n").lower() != replace.lower():  # if this line is not the replace line
                        dest_file.write(line)       # whether copying, modifying or deleting, write it
                    elif operation == "copy":       # copy writes it anyway
                        dest_file.write(line)
                    elif operation == "modify":     # modify replaces it and increments count as evidence
                        dest_file.write(replacement + "\n")
                        count += 1
                        line = line.rstrip("\n")
                        print(line + " replaced with " + replacement + ".")
                    elif operation == "delete":     # delete does not copy it, but increments count as evidence
                        count += 1
                        print(replace + " deleted.")
                    line = source_file.readline()
                source_file.close()
                dest_file.close()
                if count == 1:      # 1 means a record was deleted or modified in the temp file
                    os.remove(source_file_name)     # deleted or modified record must do the hidden file shuffle
                    os.rename("temp.txt", source_file_name)
                elif count == 0 and operation != "copy":  # had a modify or delete but did not find the record
                    print(replace + " not found!")
                elif operation == "copy":
                    print("Copy completed.")
            except IOError:
                print("Error while copying file " + source_file_name + "!")
                status = STATUS_BAD
        else:
            status = STATUS_BAD
    return status


# Delete the entire file
def delete_file():
    file_name = get_file_name("Please enter the file name to delete.")
    try:        # Removing the file can throw an exception, so handle it
        os.remove(file_name)
        print(file_name + " deleted.")
        status = STATUS_GOOD
    except IOError:
        print("An error occurred deleting the file!")
        status = STATUS_BAD
    return status


def get_file_name(prompt):
    file_name = ""
    prompt += "\nNo file extension please: "
    while file_name == "":
        file_name = input(prompt)
    file_name += ".txt"
    return file_name


def open_file(file_name, mode):
    try:
        outfile = open(file_name, mode)
        status = outfile
    except IOError:
        if mode == 'r':
            access = "read"
        else:
            access = "write"
        print("An error occurred attempting to open " + file_name + " for " + access + " mode!")
        status = STATUS_BAD
    return status


main()
