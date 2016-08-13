#!/usr/bin/env python3
# HW08_ch11_ex01
# Write a function that reads the words in words.txt and stores them as keys
# in a dictionary (returning the dictionary). It doesn’t matter what the
# values are. Then you can use the in operator as a fast way to check whether
# a string is in the dictionary.
###############################################################################
# Imports


# Body
def store_to_dict():
    words_dict = {}
    with open("words.txt", "r") as fin:
        for word in fin:
            words_dict[word.strip()] = "English"
    return words_dict

###############################################################################
def main():  # DO NOT CHANGE BELOW
    words_dict = store_to_dict()
    print(words_dict)
    if "this" in words_dict:
        print("Yup.")
    if "qwertyuiop" in words_dict:
        print("Hmm.")

if __name__ == '__main__':
    main()
