"""
Program: textanalysis.py
Author: Ken
Computes and displays the Flesch Index and the Grade
Level Equivalent for the readability of a text file.
"""

ERROR_CODE_FILE_NOT_FOUND: int = -1

# Take the inputs
fileName = input("Enter the file name (text.txt): ")
try:
    inputFile = open(fileName, 'r')
    text = inputFile.read()
except FileNotFoundError:
    print(f"|{fileName}|, file not found error")
    exit(ERROR_CODE_FILE_NOT_FOUND)
except:
    print('unknown file open or read error')

# Count the sentences
sentences = text.count('.') + text.count('?') + \
            text.count(':') + text.count(';') + \
            text.count('!')

# Count the words
word_tupl: tuple = text.split()
words = len(word_tupl)

# Count the syllables
syllables = 0
vowels = "aeiouAEIOU"
for word in word_tupl:
    for vowel in vowels:
        syllables += word.count(vowel)
    for ending in ['es', 'ed', 'e']:
        if word.endswith(ending):
            syllables -= 2
    if word.endswith('le'):
        syllables += 1

# Compute the Flesch Index and Grade Level
index = 206.835 - 1.015 * (words / sentences) - \
        84.6 * (syllables / words)
level = int(round(0.39 * (words / sentences) + 11.8 * \
                  (syllables / words) - 15.59))

# Output the results
print("The Flesch Index is", index)
print("The Grade Level Equivalent is", level)
print(sentences, "sentences")
print(words, "words")
print(syllables, "syllables")   