# Charles Buyas cjb8qf
# I conferred with Jason Lin when I got stuck trying to figure out how to include " ", "!", and other
# punctuation without changing to another character. He gave me the idea of trying out a range function

line = input("Enter your cipher text: ")
line = line.lower()
caesar_list = list(line)

cipher = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
          "v", "w", "x", "y", "z"]
alphabet = ["x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
            "s", "t", "u", "v", "w"]
output = ""
for x in range(len(caesar_list)):
    if caesar_list[x] in cipher:
        a = cipher.index(caesar_list[x])
        output += alphabet[a]
    else:
        output += caesar_list[x]
print("The decoded phrase is:", output)


"""
output = ""
line = input("Enter your cipher text: ")
for character in line:
    cipher = ord(character) - 3
    output += str(cipher) + " "
print(output)
print()

coded = output
output = ""
for str_unicode in coded.split():
    unicode = int(str_unicode)
    output += chr(unicode)
print(output)
"""
