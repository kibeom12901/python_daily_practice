from bs4 import BeautifulSoup
import requests
import lxml
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

URL = "YOUR_ZILLOW_URL"
responder_link = "YOUR_GOOGLE_FORM_LINK"

headers = {
    "User-Agent": "YOUR_USER_AGENT",
    "Accept-Language": "YOUR_ACCEPT_LANGUAGE"
}
response = requests.get(URL, headers=headers)
response.raise_for_status()
data = response.text

soup = BeautifulSoup(data, "lxml")

# Getting addresses
address_elements = soup.find_all("div", class_="StyledPropertyCardDataWrapper-c11n-8-109-3__sc-hfbvv9-0 gpfUSu property-card-data")
addresses = [address.get_text(strip=True).split("|")[-1].split("$")[0].strip() for address in address_elements]
print(addresses)

# Getting prices
price_elements = soup.find_all("span", class_="PropertyCardWrapper__StyledPriceLine-srp-8-109-3__sc-16e8gqd-1 jCoXOF")

prices = [
    int(price.get_text().split("+")[0].split("/")[0].replace("$", "").replace(",", "").strip())
    for price in price_elements
    if "$" in price.text
]
print(prices)

# Getting links
link_elements = soup.find_all("a", attrs={"data-test": "property-card-link"})
all_links = []

for link in link_elements:
    href = link.get("href")
    # If the link is relative (starts with "/"), prepend Zillow's domain.
    if href and href.startswith("/"):
        href = "https://www.zillow.com" + href
    all_links.append(href)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

for i in range(len(addresses)):
    driver.get(responder_link)
    time.sleep(1) 

    address_input = driver.find_element(By.XPATH, 'YOUR_ADDRESS_XPATH')
    price_input = driver.find_element(By.XPATH, 'YOUR_PRICE_XPATH')
    link_input = driver.find_element(By.XPATH, 'YOUR_LINK_XPATH')

    address_input.send_keys(addresses[i])
    price_input.send_keys(prices[i])
    link_input.send_keys(all_links[i])

    submit_button = driver.find_element(By.XPATH, 'YOUR_SUBMIT_BUTTON_XPATH')
    submit_button.click()

    time.sleep(2)

driver.quit()
