from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.webdriver import WebDriver
import time
import requests
from bs4 import BeautifulSoup
url_list=[]
b = webdriver.Chrome()    
b.get('https://www.perkinscoie.com/en/professionals/index.html?start=0')
time.sleep(20)
html_source = b.page_source
print html_source
f=open("lawyerinfo","w")
f.write(str(html_source.encode('utf-8').strip()))
f.close()
b.close()

