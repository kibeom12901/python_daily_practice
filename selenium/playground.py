from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://www.amazon.com/SAMSUNG-Dust-Resistant-Powerful-Processor-Lightweight/dp/B0CCX11JT6?ref=dlx_deals_dg_dcl_B0CCX11JT6_dt_sl14_ee&pf_rd_r=N4GPZXX0X52BZMCTN0F7&pf_rd_p=803dde02-c3c4-4c0f-8e6d-8126ac0017ee&th=1")

# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")

# print(f"The price is {price_dollar.text}.{price_cents.text}")

driver.get("https://www.python.org/")
search_bar = driver.find_element(By.NAME, value="q")
print(search_bar.get_attribute("placeholder"))

button = driver.find_element(By.ID, value="submit")
print(button.size)

documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
print(documentation_link.text)

bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link.text)

dates = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
date_list = [date.text for date in dates]
print(date_list)

dates = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
date_list = [date.text for date in dates]

events = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
event_list = [event.text for event in events]

dictionary = {n: {"time": date_list[n], "name": event_list[n]} for n in range(len(event_list))}
print(dictionary)

# driver.close()
driver.quit()
