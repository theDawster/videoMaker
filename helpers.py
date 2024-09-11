from bs4 import BeautifulSoup
import requests
import re
import PexelsAPI


def getVerse(url):

    result = requests.get(url)

    doc = BeautifulSoup(result.text, "html.parser")

    verse_container = doc.find("div", class_=re.compile("scripture"))
    full_verse = verse_container.find('div', class_=re.compile('bilingual-left')).text
    verse, chapter = full_verse.split('—')[0], full_verse.split('—')[1]
    reference = verse_container.find('a')['href']

    return (verse, chapter, reference)

def getDevotional(url):
    result = requests.get(url)

    doc = BeautifulSoup(result.text, "html.parser")
    devotional = doc.find('p', id='thought')

    if devotional:
        return devotional.text
    return "not found"

def getPrayer(url):
    result = requests.get(url)

    doc = BeautifulSoup(result.text, "html.parser")
    prayerContainer = doc.find_all('div', class_="bilingual-left-body")[1]
    prayer = prayerContainer.find('p').text

    if prayer:
        return prayer
    return "not found"

def getBackground():
    x = PexelsAPI.PexelsAPI()
    x.getBackgroundFromCollections()
    pass