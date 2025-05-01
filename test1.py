import random
import time
from bs4 import BeautifulSoup
import requests



url = "https://www.tottus.cl/tottus-cl/buscar?Ntt=pie"

result = requests.get(url)

doc = BeautifulSoup(result.text, "html.parser")

prices = doc.find_all(string="$")

print(prices)

