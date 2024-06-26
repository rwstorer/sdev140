word_list: list = []
word_calc: dict = {}
file_contents: str = 'word1 word2 word3 word4 word5 word2 word4 word3'

#with open('text.txt', 'r') as file:
for word in file_contents.split():
    #file_contents = file.read()
    #all_words: tuple = file_contents.split()
    if not word_calc.get(word):
        word_calc[word] = 1
    else:
        word_calc[word] += 1

for key in word_calc.keys():
    if word_calc[key] == 1:
        word_list.append(key)

word_list.sort()
for word in word_list:
    print(word)