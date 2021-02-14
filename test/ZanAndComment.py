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
# driver.maximize_window()
driver.get(url)

cookie_path = 'cookie.txt'
driver.find_element(By.ID,'unameId').send_keys('18656273986')
driver.find_element(By.ID,'passwordId').send_keys('iamagreatman_1')
sleep(7)

driver.find_element(By.XPATH,'//input[@value="登录"]').click()
# cookie = driver.get_cookies()
# with open(cookie_path, 'w', encoding='utf-8') as f:
#     f.writelines(json.dumps(cookie) + r'\n')  # 一行保存一个cookie

def GiveScore():
    for i in range(random.randint(7, 10)):
        print(driver.find_element_by_xpath('//i[@class="icon-add2 addScore"]'))
        driver.find_element_by_xpath('//i[@class="icon-add2 addScore"]').click()
        sleep(0.5)


url2 = 'https://groupweb.chaoxing.com/course/topicDiscuss/info?uuid=109643cc66834aaea0bb95e6bdf86dbb_topicDiscuss&activeId=232816881&startTime=1588843643643&timeLong=86400000&activeStatus=2&courseId=206062734'
driver.get(url2)
# //div[@class="noticeDetail_replyList"]  [@class="likeIcon"]
#加载更多
driver.implicitly_wait(5)
ele_locator = '//*[@id="subPageMain"]/div[2]/div[3]/p[1]'
param = (By.XPATH, ele_locator)
try:
    while WebDriverWait(driver, 5).until(EC.visibility_of_element_located(param)):
        driver.find_element(By.XPATH, ele_locator).click()
except TimeoutException as e:
    print(e)
    pass
#执行点赞
All_Students = driver.find_elements_by_xpath('//div[@class="like"]/i')
print('未点赞数:',len(All_Students))
for i in All_Students:
    # print(i)
    try:
        i.click()
        sleep(1)
    except TimeoutException as e:
        print(e)
        pass
#打分功能实现
All_Score = driver.find_elements_by_xpath('//span[@class="icon-grade"]')
print('未评分数：',len(All_Score))
# print('定位到的输入框为：',driver.find_element_by_xpath(ele_locator))
for j in All_Score:
    # print(i)
    try:
        # element1 = driver.find_element_by_xpath('//*[@id="a71a3e55-4f38-4664-b679-74a270f4a569"]/div[1]/div/div[1]/div/div[2]/a[2]')
        driver.execute_script("arguments[0].click();", j)
        # j.click()
        sleep(1)
        # driver.find_element_by_xpath('input[@class="ipt-num"]').send_keys(random.randint(7, 10))
        ele_locator = '//input[@class="ipt-num"]'
        param = (By.XPATH, ele_locator)
        while WebDriverWait(driver, 5).until(EC.visibility_of_element_located(param)):
            # // *[ @ id = "1C62CC57-3F4B-4FAD-B2AF-D893A4027B6E"] / div[1] / div / div[1] / div / div[1] / i[2]
            # driver.find_element_by_xpath('input[@class="ipt-num"]').click()
            # driver.find_element_by_xpath('input[@class="ipt-num"]').clear()
            Finput = driver.find_element_by_xpath('//input[@class="ipt-num"]')
            print('定位到的输入框为：',Finput )
            Finput.send_keys(random.randint(7, 10))
            # // *[ @ id = "6d0a3085-cd0d-4e40-adcf-668e3fb5bbc7"] / div[1] / div / div[1] / div / div[1] / input
            # // *[ @ id = "4a1db1da-d792-481d-92cc-1d11a0ecaf87"] / div[1] / div / div[1] / div / div[1] / input
            # // *[ @ id = "4a1db1da-d792-481d-92cc-1d11a0ecaf87"] / div[1] / div / div[1] / div / div[2] / a[2]
            # GiveScore()
            sleep(1)
            element1 = driver.find_element_by_xpath('//*[@id="a71a3e55-4f38-4664-b679-74a270f4a569"]/div[1]/div/div[1]/div/div[2]/a[2]')
            driver.execute_script("arguments[0].click();", element1)
            # driver.find_element_by_xpath('//*[@id="a71a3e55-4f38-4664-b679-74a270f4a569"]/div[1]/div/div[1]/div/div[2]/a[2]').click()
    except TimeoutException as e:
        print(e)
        pass



