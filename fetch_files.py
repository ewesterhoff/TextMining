import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import urllib
import string
import os


def find_all_religions(url):
    """returns list of urls for all listed religions"""
    url_string = requests.get(url)
    soup = BeautifulSoup(url_string.text, 'lxml') # Parse the HTML as a string

    a_tags = soup.find_all('a')
    links = [urljoin(url, a['href'])for a in a_tags]

    #return only the first sixteen
    links = links[:16]
    return links

def find_text_files(url):
    """returns list of text urls from the each religion url"""
    url_string = requests.get(url)
    soup = BeautifulSoup(url_string.text, 'lxml') # Parse the HTML as a string

    a_tags = soup.find_all('a')

    url += '/'
    files = [urljoin(url, a['href'])for a in a_tags]

    texts = []
    #return only text file links
    for a in files:
        x = str(a)
        if x[-3:] == 'txt':
            texts.append(a)
    return texts


def get_file_name(url):
    """returns file name for text document"""
    for i in range(0,len(url)):
        x = len(url)-1-i
        if url[x] == "/":
            return url[x+1:]

def get_content(url):
    """saves content to a text file in folder 'religious documents'"""
    data = urllib.request.urlopen(url)
    path = 'religious documents'

    if not os.path.exists(path):
        os.makedirs(path)

    file_name = get_file_name(url)

    with open(os.path.join(path, file_name), 'wb') as temp_file:
        for line in data:
            temp_file.write(line)

    temp_file.close()

def download_files(links):
    """saves text file from link to a folder named religious docs"""
    for t in links:
        get_content(t)

if __name__ == '__main__':
    url = 'http://textfiles.com/occult/'
    religions = find_all_religions(url)
    text_urls = []
    for r in religions:
        x = find_text_files(r)
        for i in x:
            text_urls.append(i)
    download_files(text_urls)
