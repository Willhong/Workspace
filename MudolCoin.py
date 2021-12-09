import requests
from bs4 import BeautifulSoup
import ssl
import urllib
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import threading
import datetime

prev_price=[]

coin_type=['무돌','메타']
coin_address=['0x45dbbbcdff605af5fe27fd5e93b9f3f1bb25d429','0xe815a060b9279eba642f8c889fab7afc0d0aca63']


def startTimer():
    GetPrice(coin_type[0],coin_address[0])
    GetPrice(coin_type[1],coin_address[1])
    timer = threading.Timer(15, startTimer)
    timer.start()

def GetPrice(type,address):
    f=open('/Users/hong/Library/Mobile Documents/com~apple~CloudDocs/저장용/ltog.txt','a')
    global elements
    global element
    global driver
    url = 'https://dexata.kr/?tokenA='+address+'&tokenB='
    driver.get(url)
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "flex")))
    elements = driver.find_elements_by_class_name('flex')
    current_price =elements[0].text.split('\n')[8]
    now = datetime.datetime.now()
    timestamp='['+str(now.year)+':'+str(now.month)+':'+str(now.day)+':'+str(now.hour)+':'+str(now.minute)+':'+str(now.second)+']'

    print(timestamp+type+' 시세 : '+current_price)
    f.write(timestamp+type+' 시세 : '+current_price+'\n')
    f.close()
    



url = 'https://dexata.kr/?tokenA='+''+'&tokenB='

s=Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
# 창 숨기는 옵션 추가
options.add_argument("headless")
driver = webdriver.Chrome(service=s,options=options)
startTimer()