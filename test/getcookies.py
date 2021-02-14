from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time,datetime
from time import sleep
from PIL import Image
import pytesseract # pip install pytesseract
import random
import logging
import json
url='http://passport2.chaoxing.com/login?fid=&refer=http://i.mooc.chaoxing.com'
driver=webdriver.Firefox(executable_path='D:\driver\geckodriver.exe') # firefox版本：80
driver.maximize_window()
driver.get(url)
sleep(25)
with open('cx_cookies.txt','w') as f:
    # 将cookies保存为json格式
    f.write(json.dumps(driver.get_cookies()))

driver.close()