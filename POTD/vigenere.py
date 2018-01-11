# Charles Buyas cjb8qf
# Sam Jitpaisarnsook (pvj3sz) suggested that I use a dict instead of a list


alphabet = {"a":0, "b":1, "c":2, "d":3, "e":4, "f":5, "g":6, "h":7, "i":8, "j":9, "k":10, "l":11, "m":12, "n":13,
            "o":14, "p":15, "q":16, "r":17, "s":18, "t":19, "u":20, "v":21, "w":22, "x":23, "y":24, "z":25}
numerals = {0:"a", 1:"b", 2:"c", 3:"d", 4:"e", 5:"f", 6:"g", 7:"h", 8:"i", 9:"j", 10:"k", 11:"l", 12:"m", 13:"n",
            14:"o", 15:"p", 16:"q", 17:"r", 18:"s", 19:"t", 20:"u", 21:"v", 22:"w", 23:"x", 24:"y", 25:"z"}


def letter_to_index(letter):
    if letter.lower() not in alphabet:
        return -1
    else:
        return alphabet[letter]


def index_to_letter(index):
    if index.lower() not in numerals:
        return "?"
    else:
        return numerals[index]


def vigenere_encrypt(plain_letter, key_letter):
    if plain_letter.lower() not in alphabet:
        return plain_letter.lower()
    else:
        encrypted = alphabet[plain_letter] + alphabet[key_letter]
        if encrypted > 25:
            encrypted -= 26
            return encrypted
        else:
            return encrypted


def vigenere_decrypt(cipher_letter, key_letter):
    if cipher_letter.lower() not in alphabet:
        return cipher_letter.lower()
    else:
        decrypted = alphabet[cipher_letter] - alphabet[key_letter]
        if decrypted not in range(0, 26, 1):
            decrypted += 26
            return decrypted
        else:
            return decrypted


def encrypt(plaintext, key):
    plaintext = plaintext.lower()
    key = key.lower()
    key_length = ""
    counter = 0
    encrypted_plaintext = ""
    for i in range(len(plaintext)):
        key_length += key[counter]
        counter += 1
        if counter >= len(key):
            counter -= counter
    for i in range(len(plaintext)):
        if plaintext[i] not in alphabet:
            encrypted_plaintext += plaintext[i]
        else:
            encrypt_key = alphabet[plaintext[i].lower()] + alphabet[key_length[i].lower()]
            if encrypt_key > 25:
                encrypt_key -= 26
            encrypted_plaintext += numerals[encrypt_key]
    return encrypted_plaintext


def decrypt(ciphertext, key):
    ciphertext = ciphertext.lower()
    key = key.lower()
    key_length = ""
    counter = 0
    encrypted_ciphertext = ""
    for i in range(len(ciphertext)):
        key_length += key[counter]
        counter += 1
        if counter >= len(key):
            counter -= counter
    for i in range(len(ciphertext)):
        if ciphertext[i] not in alphabet:
            encrypted_ciphertext += ciphertext[i]
        else:
            encrypt_key = alphabet[ciphertext[i].lower()] - alphabet[key_length[i].lower()]
            if encrypt_key < 0:
                encrypt_key += 26
            encrypted_ciphertext += numerals[encrypt_key]
    return encrypted_ciphertext
