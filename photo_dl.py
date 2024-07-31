from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
import requests
from time import sleep

BASE_URL = r"https://bethmigaphotography.pixieset.com/meixnernewborn/"
DIR = r"/Users/davidmeixner/Pictures/Charlotte"

driver = webdriver.Chrome()

#for i in range(79):
#    url = BASE_URL + str(i)

driver.get(BASE_URL)
sleep(5)
# enter password
imgs = driver.find_elements("xpath", "//img")
# Scroll down page to load all images

for i in range(len(imgs)):
    src = imgs[i].get_attribute('src')
    if src.split('-')[-1] in ('large.jpg', 'xlarge.jpg'):
        src = src.split('-')[0] + '-xxlarge.jpg'

    print(f"{i:02}" + ".jpeg: " + src)
    res = requests.get(src, stream = True)
    with open(DIR + "/" + f"{i:02}" + ".jpeg", 'wb') as f:
        f.write(res.content)

driver.close()


