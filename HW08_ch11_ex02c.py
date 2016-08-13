#!/usr/bin/env python3
# HW08_ch11_ex02c.py
# (1) Modify reverse_lookup_old so that it builds and returns a list of all
# keys that map to v, or an empty list if there are none.

# (2) Paste in your completed functions from HW08_ch11_ex02a.py

# (3) Do not edit what is in main(). It should print what is returned, a list
# of the keys that map to the values passed.
###############################################################################
# Imports


# Body
def reverse_lookup_old(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise ValueError


def reverse_lookup_new(d, v):
    try:
        v = int(v)
    except ValueError as e:
        print(e)
    else:
        keys = []
        for key in d:
            if v == d[key]:
                keys.append(key)
        return keys

###############################################################################
# INSERT COMPLETED CODE FROM HW08_ch11_ex02a BELOW: ###########################
###############################################################################
def histogram_new(s):
    """Creates a word count histogram for a given list of words"""
    d = dict()
    for word in s:
        d[word] = d.get(word, 0) + 1
    return d

def get_pledge_list():
    """ Opens pledge.txt and converts to a list, each item is a word in
    the order it appears in the original file. returns the list.
    """
    pledge_list = []
    # Remove the following punctuation marks
    punctuation = ",."
    with open("pledge.txt", "r") as fin:
        for line in fin:
            for word in line.split():
                word = "".join(letter for letter in word if letter not in punctuation)
                pledge_list.append(word)
    return pledge_list

###############################################################################
# INSERT COMPLETED CODE FROM HW08_ch11_ex02a BELOW: ###########################
###############################################################################
def main():   # DO NOT CHANGE BELOW
    pledge_histogram = histogram_new(get_pledge_list())
    print(reverse_lookup_new(pledge_histogram, "1"))
    print(reverse_lookup_new(pledge_histogram, "9"))
    print(reverse_lookup_new(pledge_histogram, "Python"))

if __name__ == '__main__':
    main()
