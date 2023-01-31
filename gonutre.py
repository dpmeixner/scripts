# Parse meals at gonture.com and print out nutrition information

from urllib.request import Request, urlopen
import json
import re
from bs4 import BeautifulSoup
import pandas as pd

req = Request(
    url = "https://www.gonutre.com/plans-and-menus/",
    headers={'User-Agent': 'Mozilla/5.0'}
)

# <script id="__NEXT_DATA__" type="application/json">{"props":{"pageProps":{"meals":

# Get HTML text and convert meals to json object
html = urlopen(req).read()
soup = BeautifulSoup(html)
script = soup.find('script', type="application/json")
data = json.loads(script.text)['props']['pageProps']['meals']

# Filter data on relevant infomrationx
df = pd.json_normalize(data)
df = df[(df.type == 'lunch/dinner') & (df.hasLarge == True)]
filtered = df[['title', 'nutritionalFactsLarge.fat', 'nutritionalFactsLarge.sodium', 'nutritionalFactsLarge.carb', 'nutritionalFactsLarge.sugar', 'nutritionalFactsLarge.protein', 'nutritionalFactsLarge.calories']][(df.type == 'lunch/dinner') & (df.hasLarge == True)] 
filtered.columns = ['title', 'fat', 'sodium', 'carb', 'sugar', 'protein', 'calories']
filtered['calories'] = pd.to_numeric(filtered['calories'])
print(filtered[filtered.calories >= 500].sort_values('fat'))
