import requests
from urllib.parse import urljoin
import urllib
from bs4 import BeautifulSoup
import string
import os

def get_file_name(url):
    """returns file name for text document"""
    for i in range(0,len(url)):
        x = len(url)-1-i
        if url[x] == "/":
            return url[x+1:]

def get_content(url):
    """saves content to a text file in folder 'religious documents'"""
    print(url)
    data = urllib.request.urlopen(url) # it's a file like object and works just like a file

    path = 'religious documents'

    if not os.path.exists(path):
        os.makedirs(path)

    file_name = get_file_name(url)

    with open(os.path.join(path, file_name), 'wb') as temp_file:
        for line in data:
            temp_file.write(line)

    temp_file.close()

if __name__ == '__main__':
    url = 'http://textfiles.com/occult/ATHEISM/aaffirmative.txt'
    print(get_file_name(url))
    get_content(url)
