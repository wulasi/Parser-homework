import re,requests,re
from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen('http://books.toscrape.com')
bs = BeautifulSoup(html, "html.parser")

bookList = bs.findAll('h3')
word = []
Note = open('data.txt',mode = 'w')
# for i in range(10) # for (let i=0; i < 10; i++) {}   
for name in bookList:
    word = name.get_text()
    Note.writelines(word)
    print(word)

