# Charles Buyas cjb8qf


vowels = ["a", "e", "i", "o", "u", "y"]
syllables = 0
word = input("Please give me a word: ")
list1 = list(word)
for i in range(len(word)):
    if list1[i] in vowels:
        syllables += 1
        if list1[i-1] in vowels:
            syllables -= 1
if vowels[1] in list1[-1]:
    syllables -= 1
if syllables == 0:
    print("The word", word, "has 1 syllables.")
else:
    print("The word", word, "has", syllables, "syllables.")
