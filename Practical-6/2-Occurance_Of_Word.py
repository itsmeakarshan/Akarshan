#  Program to count occurences of all words in a sentence

def word_count(str,word):
    dictionary = {}
    words = str.split()

    for i in words:
        if i in dictionary:
            dictionary[i] += 1
        else:
            dictionary[i] = 1

    print(dictionary[word])

str=input("Write a sentence: ")
word=input("Enter the word to count it's occurance: ")
word_count(str,word)
