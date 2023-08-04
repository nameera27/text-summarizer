# # # importing necessary modules
# from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize, sent_tokenize
#
# text = input()
#
# stopWord = set(stopwords.words('english'))
# words = word_tokenize(text)
#
# # for words
# freqTable = dict()
# for word in words:
#     word = word.lower()
#     if word in stopWord:
#         continue
#     if word in freqTable:
#         freqTable[word] += 1
#     else:
#         freqTable[word] = 1
#
# # for sentences
# sentences = sent_tokenize(text)
# sentenceValue = dict()
#
# for sentence in sentences:
#     for word, freq in freqTable.items():
#         if word in sentence.lower():
#             if sentence in sentenceValue:
#                 sentenceValue[sentence] += freq
#             else:
#                 sentenceValue[sentence] = freq
#
# sumVal = 0
# for sentence in sentenceValue:
#     sumVal += sentenceValue[sentence]
# global average
# try:
#     average = int(sumVal / len(sentenceValue))
# except Exception as e:
#     print(e)
#
# summary = ''
# for sentence in sentences:
#     if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
#         summary += ' ' + sentence
# print(summary, end='')
# The huge run-on sentence consists of 1,288 words and countless clauses. It takes patience to read, but once you get into the rhythm, it’s like delving into Faulkner’s stream of consciousness. The experimental writer’s sentence style inspired hundreds of writers since, including Samuel Beckett, Virginia Woolf, F. Scott Fitzgerald, James Joyce, and other masters of modern literature.Nowadays, postmodern fiction writers such as John Barth are still influenced by Faulkner’s run-on technique. He once said, It was Faulkner at his most involuted and incantatory who most enchanted me. The current record holder for the longest english sentence is Jonathan Coe for his staggering

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

# Input text - to summarize
text = input()

# Tokenizing the text
stopWords = set(stopwords.words("english"))
words = word_tokenize(text)

# Creating a frequency table to keep the
# score of each word

freqTable = dict()
for word in words:
    word = word.lower()
    if word in stopWords:
        continue
    if word in freqTable:
        freqTable[word] += 1
    else:
        freqTable[word] = 1

# Creating a dictionary to keep the score
# of each sentence
sentences = sent_tokenize(text)
sentenceValue = dict()

for sentence in sentences:
    for word, freq in freqTable.items():
        if word in sentence.lower():
            if sentence in sentenceValue:
                sentenceValue[sentence] += freq
            else:
                sentenceValue[sentence] = freq

sumValues = 0
for sentence in sentenceValue:
    sumValues += sentenceValue[sentence]

# Average value of a sentence from the original text

average = int(sumValues / len(sentenceValue))

# Storing sentences into our summary.
summary = ''
for sentence in sentences:
    if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
        summary += " " + sentence
print(summary)
