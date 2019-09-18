#!/usr/bin/env python
# coding: utf-8

# In[59]:


from selenium import webdriver
from bs4 import BeautifulSoup
import xlrd
import lxml
from time import sleep
from xlsxwriter import Workbook
import requests




import csv
def data(file_path, name,phon):
    fieldnames = ['name','phon']

    with open(file_path, "a", newline = "") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        # writer.writeheader()
        writer.writerow({
            "name": name,
            "phon":phon

})







response=requests.get('https://en.wikipedia.org/wiki/List_of_cities_in_Texas_by_population')
soup=BeautifulSoup(response.content,'lxml')
table=soup.find_all('table')[1]
cities=[a.text for a in table.find_all('a')]
for i,city in enumerate(cities):
    if '[' in  city:
        cities.pop(i)




names=[]
phones=[]
driver=webdriver.Chrome('C:/Users/Shoaib/Documents/1. Python/chromedriver')
driver.get('https://hydrafacial.com/find-a-provider/')
sleep(2)
search=driver.find_element_by_id("storemapper-zip")
for g,i in enumerate(cities):
    print("City:",g)
    search.clear()
    search.send_keys(i)
    (driver.find_element_by_id('storemapper-go')).click()
    sleep(5)
    soup=BeautifulSoup(driver.page_source,'lxml')
    left=soup.find('div',id="storemapper-left")

    ul=soup.find('ul',id="storemapper-list")
    li=[li for li in ul.find_all('li')]
    for item in li:
        try:
            phon=item.div.a.text
        except:
            phon=None
        try:
            name=item.h4.text
        except:
            name=None
        phones.append(phon)
        names.append(name)




for name,phone in zip(names,phones):
    data('alldata2.csv',name,phone)



