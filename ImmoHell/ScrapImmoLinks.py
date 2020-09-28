from bs4 import BeautifulSoup
import requests
import random
import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

#This is the list of type of property we want search data, we can add more type type
list_of_property_type=["house", "apartment"]

number_of_link=0

for type in list_of_property_type:

    page_index=1

    while True:

        url="https://www.immoweb.be/en/search/"+type+"/for-sale?countries=BE&page="+str(page_index)

        r = requests.get(url)
        if(r.status_code > 399):
            break

        driver = webdriver.Firefox()
        driver.implicitly_wait(30)
        driver.get(url)
        
        soup=BeautifulSoup(driver.page_source, "lxml")
        driver.close()
        
        f = open("immoweb_all_links.txt", "a")
        for elem in soup.find_all("a", attrs={"class" : "card__title-link"}):
            f.writelines(elem.get('href')+'\n')
            number_of_link += 1    
        f.close()

        page_index += 1
        print(number_of_link)





