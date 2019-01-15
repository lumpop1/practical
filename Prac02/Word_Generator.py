def is_valid_format():


import random

VOWELS = "#aeiou"
CONSONANTS = "%bcdfghjklmnpqrstvwxyz"

word_format = str(input("Enter the words:"))
word = ""
for kind in word_format:
    if kind == "c":
        word += random.choice(CONSONANTS)
    else:
        word += random.choice(VOWELS)
print(word)
