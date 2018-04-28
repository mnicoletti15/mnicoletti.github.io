# import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import sys
import re

driver = webdriver.Chrome()


print("--start--")

# Zip Codes
sys.stdout = open("zip_codes.txt", "w")
for i in range(23):      # Number of pages plus one 
    url = "http://www.wholefoodsmarket.com/stores/list/state?page={}".format(i)
    
    driver.get(url)
    
    select_sitelist = driver.find_elements_by_xpath("//*[@id='block-views-store-locations-by-state-state']/div/div/div[3]/div[*]/div[3]/div/div[2]/span[3]")
    for a in select_sitelist:
            print(a.text)

# Addresses
sys.stdout = open("addresses.txt", "w")
addresses = []
for i in range(23):      # Number of pages plus one
    url = "http://www.wholefoodsmarket.com/stores/list/state?page={}".format(i)
    
    driver.get(url)

    select_sitelist = driver.find_elements_by_xpath("//*[@id='block-views-store-locations-by-state-state']/div/div/div[3]/div[*]/div[3]/div")
    for a in select_sitelist:
        query = a.text
        if query[:18] == "Whole Foods Market":
            query = query[19:]
        addresses.append(query)
        print(query)
        print("---")

# Latitudes/Longitudes
sys.stdout = open("latlong.txt", "w")
driver.get("https://www.latlong.net/convert-address-to-lat-long.html")
for address in addresses:
    search = driver.find_element_by_css_selector("input[placeholder='Type address here to get lat long']")
    search.clear()
    address.replace
    query = address.replace('\n', ' ')
    search.send_keys(query)
    button = driver.find_element_by_css_selector("button[title='Find lat long coordinates']")
    button.click()
    WebDriverWait(driver, 5)
    longitude = driver.find_element_by_xpath("//*[@id='lng']").get_attribute('value')
    latitude = driver.find_element_by_xpath("//*[@id='lat']").get_attribute('value')
    print(query, ':')
    print("({}, {})".format(latitude, longitude))

sys.stdout = sys.__stdout__
print("--finished--")
driver.close()
