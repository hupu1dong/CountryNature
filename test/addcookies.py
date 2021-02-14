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
def code_tesseract(img_checkcode,checkcode):
    driver.save_screenshot('html.png')
    yzm=driver.find_element_by_id(img_checkcode)
    location=yzm.location#获取验证码x,y轴坐标
    size=yzm.size#获取验证码的长宽
    k = 1.25
    rangle=(int(location['x'])*k,int(location['y'])*k,int(location['x']+size['width'])*k,int(location['y']+size['height'])*k)#截取的位置坐标
    i=Image.open("html.png") #打开截图
    frame4=i.crop(rangle) #使用Image的crop函数，从截图中再次截取我们需要的区域
    frame4.save('code.png')#将截取到的验证码保存为jpg图片
    text = pytesseract.image_to_string(Image.open("code.png")).strip()
    # print(text)
    driver.find_element_by_id(checkcode).clear()
    driver.find_element_by_id(checkcode).send_keys(text)


driver.find_element(By.ID,'unameId').send_keys('18656273986')
driver.find_element(By.ID,'passwordId').send_keys('iamagreatman_1')
sleep(6)

driver.find_element(By.XPATH,'//input[@value="登录"]').click()

# ele_locator = "// *[ @ id = 'show_error']"
# param = (By.XPATH, ele_locator)
# try:
#     while WebDriverWait(driver, 3).until(EC.visibility_of_element_located(param)):
#         driver.find_element(By.ID, 'passwordId').clear()
#         driver.find_element(By.ID, 'passwordId').send_keys('iamagreatman_1')
#         sleep(2)
#         driver.find_element_by_id('numVerCode').click()
#         code_tesseract("numVerCode", "numcode")
#         driver.find_element(By.XPATH, '//input[@value="登录"]').click()
# except TimeoutException as e:
#     pass
url2 = 'https://mooc1.chaoxing.com/work/reviewTheList?courseId=87353810&classId=32720457&workId=10480042&isdisplaytable=2&mooc=1&isWork=true&workSystem=0&openc=120de977caaf143238394eb2636d69d4&ut=t'
# li.zmy_item:nth-child(3) > a:nth-child(1) > img:nth-child(1)
driver.get(url2)
sleep(3)
driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div/div[2]/table/tbody/tr[1]/td[10]/a').click()

ele_locator = "/html/body/div[3]/div/div/div/div/p/a[2]/span"
param = (By.XPATH, ele_locator)
try:
    while WebDriverWait(driver, 3).until(EC.visibility_of_element_located(param)):
        driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div/form/div[1]/div[4]/div/div[4]/div[1]/p/input[2]').send_keys(random.randint(90, 99))
        driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div/div/p/a[2]/span').click()
except TimeoutException as e:
    pass
# driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[1]/ul[1]/li[3]/a[1]/img').click()
# sleep(5)
# driver.find_element(By.XPATH,'/html/body/div[4]/div[2]/div[1]/div[2]/ul/li[6]/a').click()




# driver.close()
