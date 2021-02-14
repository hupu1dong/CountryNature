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
import random
import xlwt
url='http://passport2.chaoxing.com/login?fid=&refer=http://i.mooc.chaoxing.com'
driver=webdriver.Firefox(executable_path='D:\driver\geckodriver.exe') # firefox版本：80
# driver.maximize_window()
driver.get(url)

driver.find_element(By.ID,'unameId').send_keys('18656273986')
driver.find_element(By.ID,'passwordId').send_keys('iamagreatman_1')
sleep(7)

driver.find_element(By.XPATH,'//input[@value="登录"]').click()
f = open('data1.xls', 'w+', encoding='utf-8_sig')
f.write('姓名,分数\n')

url2 = 'https://mobilelearn.chaoxing.com/widget/score/pc/queryScore?activeId=337900621&courseId=214848254&classId=32661805&fid=124&isTeacherViewOpen=1'
driver.get(url2)
# All_Rows=driver.find_elements_by_xpath('//div[@class="whitebg_pf"]//div[starts-with(@id,"yiping")]')
All_Rows=driver.find_elements_by_xpath('//div[@class="whitebg_pf"]//h3[@class="ypTit"]')
datalist = []
for i in All_Rows:
    data = []
    name = i.find_element_by_tag_name('span').text
    data.append(name)
    # print(name)
    score = i.find_element_by_tag_name('b').text
    data.append(score)
    # print(score)
    datalist.append(data)
    f.write(f'{name},{score}\n')

#
# dllen = len(datalist)
# savepath = "姓名与分数.xls"
# saveData(datalist,savepath,dllen)




