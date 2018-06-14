str = "This is an awesome occasion. This has bever happend before."
# Count character occurences
char_occurances = {}
for char in str:
    char_occurances[char] = char_occurances.get(char, 0) + 1
print(char_occurances)

# Count word ocurences

word_occurences = {}

for word in str.split():
    word_occurences[word] = word_occurences.get(word, 0) + 1
print(word_occurences)
