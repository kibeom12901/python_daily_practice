from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

items = driver.find_elements(By.CSS_SELECTOR, "#store div")
item_ids = [item.get_attribute("id") for item in items]
print(item_ids)

cookie = driver.find_element(By.ID, "cookie")

timeout = time.time() + 5
while True:
    cookie.click()

    if time.time() > timeout:
        price_elements = driver.find_elements(By.CSS_SELECTOR, "#store b")
        item_prices = []
        for price in price_elements:
            element_text = price.text
            if element_text != "":
                cost = element_text.split("-")[1].strip().replace(",", "")
                item_prices.append(int(cost))  

        cookie_upgrades = {item_prices[n]: item_ids[n] for n in range(len(item_prices))}

        money_element = driver.find_element(By.ID, "money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)

        affordable_upgrades = {}
        for cost, upgrade_id in cookie_upgrades.items():
            if cookie_count >= cost:
                affordable_upgrades[cost] = upgrade_id

        if affordable_upgrades:
            highest_price_affordable_upgrade = max(affordable_upgrades)
            to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]
        
            purchase = driver.find_element(By.ID, to_purchase_id)
            purchase.click()

        
        timeout = time.time() + 5

driver.quit()
