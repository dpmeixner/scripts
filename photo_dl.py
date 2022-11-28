from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
import requests
from time import sleep

BASE_URL = r"https://imageurl.com"
DIR = r"C:\Save\Path"

driver = webdriver.Chrome()

for i in range(79):
    url = BASE_URL + str(i)

    driver.get(url)
    sleep(5)
    img = driver.find_element("xpath", "//img[contains(@alt, 'Gallery')]")
    src = img.get_attribute('src')

    print(f"{i:02}" + ".jpeg: " + src)
    res = requests.get(src, stream = True)
    with open(DIR + "\\" + f"{i:02}" + ".jpeg", 'wb') as f:
        f.write(res.content)

