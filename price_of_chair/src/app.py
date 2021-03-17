import requests
from bs4 import BeautifulSoup

request = requests.get("https://www.johnlewis.com/house-by-john-lewis-hinton-office-chair/grey/p2083183")
content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("div", {"itemprop": "offers", "class": "prices-container"})
string_price = element.text.strip() # "£129.00"

price_without_symbol = string_price[1:]

print(float(price_without_symbol) < 200 )

price = float(price_without_symbol)

if price < 200:
    print("Buy the bloody chair!")
    print("The current price is {}".format(string_price))
else:
    print("It costs too much, dummy!")

# <p class="price price--large">£129.00</p>









