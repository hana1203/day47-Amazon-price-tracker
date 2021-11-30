import requests
from bs4 import BeautifulSoup
import lxml
amazon_site = "https://www.amazon.com/New-Apple-Watch-GPS-40mm/dp/B08KJ32SFZ/ref=sr_1_5?keywords=apple+watch&qid=1638281339&sr=8-5"
response = requests.get(amazon_site,
                        headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
                                 "Accept-Language":"en-US,en;q=0.9"})
web_page = response.text
# print(web_page)
soup = BeautifulSoup(web_page, "lxml")
price = soup.find(name="span", class_="a-offscreen").getText()
# $338.00
price = price.split("$")
# ['', '338.00']
price = float(price[1])
print(price)
# 338.0
title = soup.find(name="span", id="productTitle").getText()

import smtplib
#smtplib module 불러오기

my_email = "@gmail.com"
password = ""

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    if price > 300:
        connection.sendmail(
            from_addr=my_email,
            to_addrs="@gmail.com",
            msg=f"Subject: Amazon Price Alert for {title}\n\n Your item added to cart {title} now is ${price}. "
                f"Go check out this link {amazon_site}"
        )

# Google 계정에서 less secure app access ON으로 바꿔야지만 파이썬에서 메일 send 접근가능- 안하면 별별 에러
# < module > connection.login(user=my_email, password=password)
# login raise last_exceptionauth
# raise SMTPAuthenticationError(code, resp)
# mtplib.SMTPAuthenticationError: (535, b'5.7.8 Username and Password not accepted.