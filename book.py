from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup
import os 


if not os.path.exists("books/"):
    os.mkdir("books")


url = "https://www.wattpad.com/"
story = input("Table of contents address succeeding 'story/'")

req = Request(url+"story/"+story, headers={'User-Agent': 'Mozilla/5.0'})
web_byte = urlopen(req).read()

webpage = web_byte.decode('utf-8')

page_soup = soup(webpage,"html.parser")

if not os.path.exists("books/"+story):
    os.mkdir("books/"+story)

a_cont = page_soup.find_all('a',class_ ="on-navigate-part")
chap_name = ""
continued = False
chap = False
for  a in a_cont:
    next_url = url + a['href']
    print(next_url)

    if chap:    
        if (a.text.strip()).startswith("CHAPTER"):
            continued = False
            chap = True
            chap_name = a.text.strip()
        else:
            continued = True
    else:
        chap_name = a.text.strip()



    
    req = Request(next_url, headers={'User-Agent': 'Mozilla/5.0'})
    web_byte = urlopen(req).read()
    webpage = web_byte.decode('utf-8')
    page_soup = soup(webpage,"html.parser")
    p_cont = page_soup.find_all('p')
    with open("books/"+story+"/"+chap_name.strip()+".txt" ,'a+') as f:
        if continued:
                f.writelines('\n'+chap_name.strip()+'\n')
        for p in p_cont:
            f.writelines(p.text+'\n')
