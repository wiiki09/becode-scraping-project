from bs4 import BeautifulSoup
import requests
import random
import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

#url='https://www.immoweb.be/en/search/house/for-sale?countries=BE'
url="https://www.immoweb.be/en/search/apartment/for-sale?countries=BE"

driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.get(url)

soup=BeautifulSoup(driver.page_source, "lxml")
driver.close()


immo_links=[]
page_number=int(soup.find_all("span", attrs={"class" : "button__label", "aria-hidden" : "true" })[-1].text)+1


for i in range(1,page_number):

    #url="https://www.immoweb.be/en/search/house/for-sale?countries=BE&page="+str(i)
    url="https://www.immoweb.be/en/search/apartment/for-sale?countries=BE&page="+str(i)

    driver = webdriver.Firefox()
    driver.implicitly_wait(30)
    driver.get(url)

    soup=BeautifulSoup(driver.page_source, "lxml")
    driver.close()
    
    f = open("immoweb_links.txt", "a")
    for elem in soup.find_all("a", attrs={"class" : "card__title-link"}):
        immo_links.append(elem.get('href'))
        f.writelines(elem.get('href')+'\n')
        
    f.close()
    print(len(immo_links))





