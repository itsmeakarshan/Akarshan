#  Program to count occurences of all words in a sentence

def word_count(str):
    dictionary = {}
    words = str.split()

    for word in words:
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1

    print(dictionary)

str=input("Write a sentence: ")
word_count(str)
