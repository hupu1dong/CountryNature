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
url='http://passport2.chaoxing.com/login?fid=&refer=http://i.mooc.chaoxing.com'
driver=webdriver.Firefox(executable_path='D:\driver\geckodriver.exe') # firefox版本：80
driver.maximize_window()
driver.get(url)

cookie_path = 'cookie.txt'
driver.find_element(By.ID,'unameId').send_keys('18656273986')
driver.find_element(By.ID,'passwordId').send_keys('iamagreatman_1')
sleep(7)

driver.find_element(By.XPATH,'//input[@value="登录"]').click()



url2 = 'https://mobilelearn.chaoxing.com/widget/pcvote/goPCVoteStatistic?activePrimaryId=202649694&quessequence=1&courseId=206062734&classId=12109786&fid=124&isTeacherViewOpen=1'
driver.get(url2)
# //*[@id="ul_scroll_58812203"]/li[1]
# test1 = driver.find_elements_by_xpath('//div[@class="AnsweredCon"]/dl[0]//li')
# print(len(test1))
driver.implicitly_wait(5)
# /html/body/div[4]/div[3]/div/div[2]/dl[1]/dd/div[1]/strong/ul/li[1]/a
# /html/body/div[4]/div[3]/div/div[2]/dl[2]/dd/div[1]/strong/ul/li[1]/a
# /html/body/div[4]/div[3]/div/div[2]/dl[3]/dd/div[1]/strong/ul/li[1]/a

# /html/body/div[4]/div[3]/div/div[2]/dl[3]/dd/div[1]/strong/ul/li[16]/a
# /html/body/div[4]/div[3]/div/div[2]/dl[3]/dd/div[1]/strong/ul/li[21]/a
choice = driver.find_elements_by_xpath('//div[@class="AnsweredCon"]//dl//li[1]/a')
print(len(choice))
scolls = driver.find_elements_by_xpath('//div[@class="AnsweredCon"]//i[@class="icon-arrow-down"]')
for i in range(len(scolls)):
    scolls[i].click()
    # choice[i].click()
    s = random.randint(16, 21)
    driver.find_element_by_xpath('//div[@class="AnsweredCon"]/dl['+str(i+1)+']/dd/div[1]/strong/ul/li['+str(s)+']/a').click()


