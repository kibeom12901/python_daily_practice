from bs4 import BeautifulSoup
import requests
import lxml

# use https://myhttpheader.com/ to figure out
headers = {
    "User-Agent": YOUR_USER_AGENT
    "Accept-Language": YOUR_ACCEPT_LANGUAGE
}

URL = "https://www.amazon.com/dp/B0B97ZLV46/ref=syn_sd_onsite_desktop_0?ie=UTF8&pd_rd_plhdr=t&aref=yzWFrq5H0a&th=1"

response = requests.get(URL, headers=headers)
response.raise_for_status()
data = response.text

soup = BeautifulSoup(data, "lxml")

price_elements = soup.find_all("span", class_="a-offscreen")
main_price = price_elements[10].text.strip()
number = main_price.split("$")[1]
answer = float(number)

print(number)
