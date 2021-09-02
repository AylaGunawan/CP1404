"""
CP1404 - Practical 05
Word Occurrences
"""

text = input("Text: ")
words = text.split(" ")
longest_word_length = 0

word_occurrences = {}
for word in words:
    if word in word_occurrences:
        word_occurrences[word] += 1
    else:
        word_occurrences[word] = 1
    if len(word) > longest_word_length:
        longest_word_length = len(word)

for sorted_word in sorted(word_occurrences):
    print("{:{}} : {}".format(sorted_word, longest_word_length, word_occurrences[sorted_word]))
