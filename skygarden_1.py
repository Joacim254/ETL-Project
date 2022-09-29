from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
import pandas as pd

options = webdriver.ChromeOptions()
options.headless = True

driver = webdriver.Chrome("C:/chromedriver_win32/chromedriver.exe", options=options)
link = 'https://sky.garden/category/televisions-298/products'
driver.get(link)


# newsletter = driver.find_element_by_css_selector("div[id= 'close-button-1545222288830']").click()
newsletter = driver.find_element_by_css_selector("#close-button-1545222288830 > span").click()

items = driver.find_elements_by_css_selector("div[class = 'col-lg-s-4 col-md-s-3 col-sm-s-6 center-flex no-padding ng-star-inserted']")

# load_more = driver.find_element_by_css_selector("button[class='sky-primary-btn mat-flat-button mat-button-base']").click()

l_name, l_price, l_old_price, l_discount = [], [], [], []


for product in items:
    name = product.find_element_by_css_selector("p[class='card-title']").text
    price = product.find_element_by_css_selector("div[class = 'card-price-container ng-star-inserted']").text
    try:
        old_price = product.find_element_by_css_selector("span[class='price-original d-none d-sm-inline-block ng-star-inserted']").text
    except:
        old_price = price
    try:    
        discount = product.find_element_by_css_selector("p[class = 'discount-badge-percentage ng-star-inserted']").text
    except:
        discount = "0 %"

        l_name.append(name)
        l_price.append(price)
        l_old_price.append(old_price)
        l_discount.append(discount)

    sky_products = {
        'item_name': l_name,
        'item_price': l_price,
        'item_old_price': l_old_price,
        'item_discount': l_discount
    }


def skygarden():
    data = pd.DataFrame(sky_products)
    return data