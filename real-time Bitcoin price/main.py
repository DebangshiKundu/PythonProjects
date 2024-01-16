from bs4 import BeautifulSoup
import requests
import time
from playsound import playsound

def scrape():
    url='https://coinmarketcap.com/currencies/bitcoin/'

    r=requests.get(url)

    soup=BeautifulSoup(r.text,'lxml')
    current=soup.body.find(class_='sc-f70bb44c-0 jxpCgO base-text')

    print(current.text)
    return current.text.replace('$','').replace(',','')

target=50000
while True:
    time.sleep(5)
    current=float(scrape())
    if target>=current:
        playsound('pythonProject/real-time Bitcoin price/notification.wav')
