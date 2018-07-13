import os
from bs4 import BeautifulSoup
import time
import requests
from urllib2 import urlopen as uReq
import re,time
url_list=[]
final_list=[]
f=open("lawyerinfo","r")
r=f.read()
f.close()

#print r
soup = BeautifulSoup(r,"html.parser")
for link in soup.find_all('a', href=True):
    if "-" in link['href'] and "/en/professionals/" in link['href']:
        url="https://www.perkinscoie.com"+link['href']
        url_list.append(str(url))
        f=open("lawyerinfourl","a")
        f.write(str(url)+"\n")
        f.close()


