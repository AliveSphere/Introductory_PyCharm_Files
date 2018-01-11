# This program demonstrates records and text files with numbers
# Each record of the birthdays file has four fields
# name, month of birth as integer, day of birth as integer
# year of birth as integer


def main():
    birthday_file = open("birthdays.txt", "w")
    again = "y"
    while again == "y" or again == "Y":
        # note, all these inputs should be validated before the program continues
        name = input("Please enter a name of the birthday person: ")
        name += "\n"
        month = int(input("Please enter the month of birth as an integer 1 to 12: "))
        month = str(month) + "\n"
        day = str(int(input("Please enter the day of birth as integer 1 to 31: "))) + "\n"
        year = str(int(input("Please enter the year of birth as integer with four places: "))) + "\n"
        birthday_file.write(name)
        birthday_file.write(month)
        birthday_file.write(day)
        birthday_file.write(year)
        print("\nBirthday record written to permanent storage.")
        again = input("Please enter y to write another birthdays record: ")
    print(birthday_file)
    birthday_file.close()
    print("Birthday file is closed.")


main()
