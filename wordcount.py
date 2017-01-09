# put your code here.
# open file
# create an empty diction
# iterate over each line (split on spaces)
# iterate over lists to add words to dictionary


# text = open("twain.txt")

# wordcount = {}

# for line in text:
#     word_list = line.rstrip().split(" ")
#     for word in word_list:
#         wordcount[word] = wordcount.get(word, 0) + 1

# for item in sorted(wordcount.iteritems()):
#     print item

import string

def poemword_count(filename):

    full_text = open(filename)
    wordcount = {}

    for line in full_text:
        word_list = line.rstrip().split(" ")
        for word in word_list:
            word = word.lower()
            word = "".join([char for char in word if char not in (string.punctuation)])
            wordcount[word] = wordcount.get(word, 0) + 1

    for item in sorted(wordcount.iteritems()):
        print item[0], item[1]


poemword_count("twain.txt")