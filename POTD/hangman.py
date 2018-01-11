# Charles Buyas cjb8qf


guesses = 6
word = input("Enter a word: ")
word = word.upper()
wl = list(word)
dashes = ""
dash = 0
while dash < len(word):
    dashes += "-"
    dash += 1
while guesses > 0:
    plg = input("[" + dashes + "] You have " + str(guesses) + " left, enter a letter: ")
    if plg.upper() in wl:
        print("Correct!")
        d = list(dashes)
        for i in range(len(word)):
            if plg.upper() == word[i]:
                d[i] = plg.upper()
        dashes = ""
        for i in range(len(word)):
            dashes += d[i]
    if dashes == word.upper():
        print("You win! The word was " + '"' + word.upper() + '"')
        guesses -= 6
    if plg.upper() not in wl:
        guesses -= 1
        if guesses == 0:
            print("You lose! The word was " + '"' + word.upper() + '"')
        else:
            print("Incorrect!")
