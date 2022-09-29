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
link = 'https://www.kilimall.co.ke/new/commoditysearch?c=&aside=smart%20tv&gc_id='
driver.get(link)

#close_pop = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//big"))).click()


pagination = driver.find_element_by_css_selector("button[class = 'btn-next']")
l_name, l_price, l_old_price, l_discount = [], [], [], []

pages = 5
while pages > 1:
    
    pagination.click()
    wait_next = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class = 'el-col el-col-6']")))

    items = driver.find_elements_by_css_selector("div[class = 'el-col el-col-6']")


    for product in items:

        name = product.find_element_by_css_selector("div[class = 'wordwrap']").text
        price = product.find_element_by_css_selector("span[style = 'color: rgb(248, 118, 34); font-size: 16px;']").text
        try:
            old_price = product.find_element_by_css_selector("span[class = 'twoksh']").text
        except:
            old_price = price
        
        try:
            discount = product.find_element_by_css_selector("span[class = 'greenbox']").text
        except:
            discount = "0% off"

        l_old_price.append(old_price)
        l_name.append(name)
        l_price.append(price)
        l_discount.append(discount)
    pages -= 1
    kilimall_products = {
        'item_name': l_name,
        'item_price': l_price,
        'item_old_price': l_old_price,
        'item_discount': l_discount
    }

def mall():
    data = pd.DataFrame(kilimall_products)
    return data