from __future__ import print_function, division
from os.path import exists
from pickle import dump, load

import sys
import string
import random
import requests
import unicodedata

# global variables
suffix_map = {}        # map from prefixes to a list of suffixes
#{(prefix, [sf1, sf2, sf3, ..., sfn])}
prefix = ()            # current tuple of words

def get_book(file_name):
    """Checks to see if filename is on file, and loads it
    If it's not on file, code travels to project gutenberg, creates file, and then loads it

    returns: plain text file
    """
    f = open(file_name)
    lines = f.readlines()
    return lines

def process_file(f, order=2):
    """Reads a file and performs Markov analysis.

    filename: string
    order: integer number of words in the prefix

    returns: map from prefix to list of possible suffixes.
    """
    clean_file(f)

    for line in f:
        for word in line.rstrip().split():
            process_word(word, order)

def clean_file(fp):
    """Cleans file of any information not desired, including
    Header
    Footer
    Unparsable characters
    """

    for line in fp:
        if line.startswith('*** START OF THIS PROJECT GUTENBERG EBOOK EMMA ***'):
            break

def process_word(word, order=2):
    """Processes the words in each paragraph, mapping words to all possible suffixes
    """
    global prefix

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
        word = str(word)
        word.replace("b'", "")
        print(word, end=' ')
        start = shift(start, word)

def shift(t, word):
    """Forms a new tuple by removing the head and adding word to the tail.

    t: tuple of strings
    word: string

    Returns: tuple of strings
    """
    return t[1:] + (word,)

def main(filename, n=20, order=2):
    f = get_book(filename)
    try:
        n = int(n)
        order = int(order)
    except ValueError:
        print('Inputs not well defined')
    else:
        process_file(f, order)
        random_text(n)
        print()


if __name__ == '__main__':
    texts = '158.txt'
    main(texts, 20, 2)
