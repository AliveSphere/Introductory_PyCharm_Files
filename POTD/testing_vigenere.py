from vigenere import letter_to_index


if letter_to_index('a') == 0:
    print("letter_to_index - Passed 'a' test!")
else:
    print("letter_to_index - FAILED 'a' test! Expected 0, but got", letter_to_index('a'))
