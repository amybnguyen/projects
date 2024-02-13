from selenium import webdriver
from selenium.webdriver.common.by import By
import time

timeout = time.time() + 5
five_min = time.time() + 60 * 5

driver = webdriver.Chrome()
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, value="cookie")

while True:
    cookie.click()

    if time.time() > timeout:
        shop_items_list = []
        store = {}
        shop_items = driver.find_elements(By.CSS_SELECTOR, value="#store b")
        for items in shop_items:
            shop_items_list.append(items.text)

        for i in range(len(shop_items_list) - 1):
            shop_item = shop_items_list[i].split(" - ")
            store[i] = {
                "item": shop_item[0],
                "price": int(shop_item[1].replace(",", ""))
            }

        cookies_in_bank = driver.find_element(By.ID, value="money")
        money = int(cookies_in_bank.text.replace(",", ""))
        for i in range(len(store) - 1, -1, -1):
            if store[i]["price"] < money:
                item_to_buy = driver.find_element(By.ID, value=f"buy{store[i]["item"]}")
                item_to_buy.click()
                break
            else:
                pass
        timeout = time.time() + 5

    if time.time() > five_min:
        cookie_per_s = driver.find_element(By.ID, value="cps").text
        print(cookie_per_s)
        break
