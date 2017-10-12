from __future__ import print_function, division
from os.path import exists

import sys
import string
import random
import requests
import glob

# global variables
suffix_map = {}        # map from prefixes to a list of suffixes
#{(prefix, [sf1, sf2, sf3, ..., sfn])}
prefix = ()            # current tuple of words

def get_book(file_name):
    """Checks to see if filename is on file, and loads it

    returns: lines of file
    """
    f = open(file_name, 'rb')
    lines = f.readlines()
    return lines

def process_file(f, order):
    """Reads a file and performs Markov analysis.

    filename: string
    order: integer number of words in the prefix

    returns: map from prefix to list of possible suffixes.
    """
    for line in f:
        for word in line.rstrip().split():
            process_word(word, order)

def clean_words(word):
    #removes errant punctuation and numbers
    punctuation = ['[', ']', "'", ":", "@", "*", "/", "(", ")", '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for letter in word:
        if letter in punctuation:
            return False
    #removes character names
    if (word == word.upper()) and (len(word) > 3):
        return False
    #removes numbers
    try:
        int(word)
        return False
    except:
        return True
    return True

def process_word(word, order):
    """Processes the words in each paragraph, mapping words to all possible suffixes
    """
    global prefix

    #boolean false if the word shouldn't be included
    check = clean_words(word)
    if check == False:
        return

    try:
        word = word.decode("utf-8")
    except:
        return
    #starts off the dictionary
    if len(prefix) < order:
        prefix += (word,)
        return

    #check if the previous word already has a chain started
    try:
        suffix_map[prefix].append(word)
    except KeyError:
        # if not, start one
        suffix_map[prefix] = [word]

def random_text(n):
    """Generates random wordsfrom the analyzed text.

    Starts with a random prefix from the dictionary.

    n: number of words to generate
    """
    # choose a random prefix (not weighted by frequency)
    start = random.choice(list(suffix_map.keys()))

    for i in range(n):
        suffixes = suffix_map.get(start, None)
        if suffixes == None:
            # if the start isn't in map, we got to the end of the
            # original text, so we have to start again.
            random_text(n-i)
            return

        # choose a random suffix
        word = random.choice(suffixes)
        print(word, end=' ')
        start = shift(start, word)

def shift(t, word):
    """Forms a new tuple by removing the head and adding word to the tail.

    t: tuple of strings
    word: string

    Returns: tuple of strings
    """
    return t[1:] + (word,)

def main(files, n=50, order=7):
    for t in files:
        f = get_book(t)
        n = int(n)
        order = int(order)
        process_file(f, order)

    random_text(n)
    print()


if __name__ == '__main__':
    #texts = ['bible.txt', 'philosphy.txt', 'emma.txt']
    files = glob.glob('religious documents/*.txt')

    texts = []
    for f in files:
       texts.append(f)

    main(texts, 100, 2)
