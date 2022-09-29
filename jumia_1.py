#!/usr/bin/env python
# coding: utf-8

# In[4]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
import pandas as pd


# In[5]:


options = webdriver.ChromeOptions()
options.headless = True

pages = 5
l_name, l_price, l_old_price, l_discount = [], [], [], []
for i in range(1, pages+1):
    
    driver = webdriver.Chrome("C:/chromedriver_win32/chromedriver.exe", options=options)

    link = 'https://www.jumia.co.ke/smart-tvs-2282/?page=' + str(i) + '#catalog-listing'
    driver.get(link)
    cancel_newsletter = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#pop > div > section > button > svg > use"))).click()
    items = driver.find_elements_by_css_selector("article[class = 'prd _fb col c-prd']")

    
    for product in items:

        price = product.find_element_by_css_selector("div[class = 'prc']").text
        try:
            old_price = product.find_element_by_css_selector("div[class = 'old']").text
        except:
            old_price = price
        name = product.find_element_by_css_selector("h3[class = 'name']").text
        try:
            discount = "-" + product.find_element_by_css_selector("div[class = 'bdg _dsct _sm']").text
        except:
            discount = "0%"

        l_old_price.append(old_price)
        l_name.append(name)
        l_price.append(price)
        l_discount.append(discount)
        


jumia_products = {'item_name': l_name, 'item_price': l_price, 'item_old_price': l_old_price, 'item_discount': l_discount}

driver.quit()

def jumia():
    data = pd.DataFrame(jumia_products)
    return data

