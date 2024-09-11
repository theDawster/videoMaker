from selenium import webdriver
from selenium.webdriver.common.by import By
import helpers



url = "https://www.verseoftheday.com/"

content = {}
content['verse'], content['chapter'], content['href'] = helpers.getVerse(url)
print("got verse...")
content['devotional'] = helpers.getDevotional(url)
print('got devotional...')
content['prayer'] = helpers.getPrayer(url)
print("got prayer...")

print("generating video...")
helpers.getBackground()



pass