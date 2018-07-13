import os
from bs4 import BeautifulSoup
import time
import requests
from urllib2 import urlopen as uReq
import re,time,json
url_list=[]
final_list=[]
f=open("lawyerinfourl","r")
r=f.read()
f.close()
print r.strip()
data=r.split("\n")
for x in data:
    r = requests.get(x)
    #print r.content
    soup = BeautifulSoup(r.content,"html.parser")
    mydivs = soup.find("span", {"class": "bio-title-text"})
   
    mydivsp = soup.find("span", {"class": "bio-position type-25"})
   
    mydivs1 = soup.find("span", {"class": "phone-number"})
 
    mydivs2 = soup.find("a", {"class": "type-29"})
   
    mydivo = soup.find("div", {"class": "side-item-wrapper"})
   
    mydivp = soup.find("div", {"class": "side-item-list"})
    # print "practicearea",mydivp.text
    # print "overview",mydivo.text
    # print "vcfcard",mydivs2['href']
    # print "phoncar",mydivs1.text
    # print "posiom",mydivsp.text
    # print "name",mydivs.text

    vlink="https://www.perkinscoie.com"+mydivs2['href']
    print vlink
    jsonarr={}
    jsonarr['name'] = mydivs.text.strip()
    jsonarr['position'] = mydivsp.text.strip()
    jsonarr['phone'] =mydivs1.text.strip()
    jsonarr['overview'] = mydivo.text.strip()
    jsonarr['vcflink'] =vlink.strip()
    jsonarr['parea'] = mydivp.text.strip()
    print jsonarr
    with open("lawyerinfojson.json", "a") as f1:
        json.dump(jsonarr,f1)
        f1.write(",\n")
        f1.close()




