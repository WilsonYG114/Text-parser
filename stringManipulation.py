import re
import string

import requests
from bs4 import BeautifulSoup

str1 = "hello how are you doing"
target = "hello"



#str2 = str1[x:-1]
#print(str2)

#txt = "The rain in Spain"
#x = re.search("doing", str1)

#starting_index = x.start()

#str2 = str1[0:starting_index]
#print(str2)


#url = 'https://gutenberg.org/cache/epub/68694/pg68694.txt'
#page = requests.get(url)
#soup = BeautifulSoup(page.text, 'html.parser')
#source = str(soup)
#end_target = "*** END OF THE PROJECT GUTENBERG EBOOK"
#x = re.search(end_target, source)

#x = source.rfind(end_target)
#final_resul = source[0:x]
#print(final_resul)

#word = "HELLO HOW ARE YOU HELLO"
#word_list = {}
#data_lst = word.split()
#print(word_list)

url = "https://gutenberg.org/cache/epub/68700/pg68700.txt"
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
source = str(soup)
final_resul = source
begin = "*** START OF THE PROJECT GUTENBERG EBOOK THE RING BONANZA ***"
#end = "*** END OF THE PROJECT GUTENBERG EBOOK THE RING BONANZA ***"
if begin in source and end in source:
    begin_text = begin
    x = re.search(re.escape(begin_text), source)
    ending_index = x.end()
    result = source[ending_index:]
    end_text = end
    start_index = result.rfind(end_text)
    final_resul = result[0:start_index]
else:
    print("begin or end not in text check again")

print(final_resul)