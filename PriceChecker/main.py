import os
import requests
import smtplib
import lxml
from bs4 import BeautifulSoup

URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
MY_EMAIL = os.environ.get("MY_EMAIL", "Email password not found")
EMAIL_PASS = os.environ.get("EMAIL_PASS", "Email password not found")
LOWEST_PRICE = 100.00

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(URL, headers=headers)
amazon_page = response.text

soup = BeautifulSoup(amazon_page, "lxml")
price = soup.find(class_="aok-offscreen").getText()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)

if price_as_float < LOWEST_PRICE:
    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.starttls()
    connection.login(user=MY_EMAIL, password=EMAIL_PASS)
    connection.sendmail(from_addr=MY_EMAIL,
                        to_addrs=MY_EMAIL,
                        msg=f"Subject: Low price alert!\n\nThe instant pot is below $100. Buy now!")