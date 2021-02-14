from datetime import time

from selenium import webdriver
import json
import time,datetime

cookie_path = 'cookie.txt'
driver=webdriver.Firefox(executable_path='D:\driver\geckodriver.exe') # firefox版本：80
url2 = 'https://mooc1.chaoxing.com/bbscircle/gettopicdetail?courseId=214848254&clazzid=32661805&topicid=223198150&showChooseClazzId=list_32661805&ut=t&folderId=&cpi=48361720&openc=74f0d9fa3b8cc007d24fabfe4038779f&enc=ede3cc71e666cf1aa5e6f814dc5d09dd'

driver.get(url2)
with open(cookie_path, 'r', encoding='utf-8') as f:
    cookies = f.readlines()

for cookie in cookies:
    cookie = cookie.replace(r'\n', '')
    cookie_li = json.loads(cookie)
    time.sleep(3)
    for cookie in cookie_li:
        driver.add_cookie(cookie)
    driver.refresh()