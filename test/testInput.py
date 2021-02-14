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

def AiSleep_click(ele_locator):
    param = (By.XPATH, ele_locator)
    try:
        while WebDriverWait(driver, 30,2).until(EC.presence_of_element_located(param)):
            driver.find_element(By.XPATH, ele_locator).click()
    except TimeoutException as e:
        print('没发现可点击元素'+ele_locator)
        pass
def AiSleep_switch(ele_locator):
    param = (By.XPATH, ele_locator)
    try:
        while WebDriverWait(driver, 30,2).until(EC.presence_of_element_located(param)):
            iframe = driver.find_element_by_xpath(ele_locator)
            driver.switch_to.frame(iframe)
    except TimeoutException as e:
        print('没发现可切换frame'+ele_locator)
        pass
def AiSleep_sendkeys(ele_locator,keys):
    param = (By.XPATH, ele_locator)
    try:
        while WebDriverWait(driver, 30,2).until(EC.presence_of_element_located(param)):
            driver.find_element(By.XPATH, ele_locator).send_keys(keys)
    except TimeoutException as e:
        print('没发现可输入的框'+ele_locator)
        pass


url='http://222.207.13.101/bbxyjw/cas/login.action'
# http://222.207.13.101/bbxyjw/MainFrm.html?random=0.7856890803274442
driver=webdriver.Firefox(executable_path='D:\driver\geckodriver.exe') # firefox版本：80
driver.maximize_window()
driver.get(url)
driver.add_cookie({'name':'JSESSIONID','value':'09AC7E3F11138C8853E3955D5D7D1C4D','Domain':'222.207.13.101'})
url2='http://222.207.13.101/bbxyjw/MainFrm.html'
driver.get(url2)
driver.implicity_wait(10)
driver.switch_to.frame('frmbody')
driver.find_element(By.XPATH,'/html/body/table/tbody/tr/td[1]/table/tbody/tr[3]/td/table/tbody/tr[2]/td/div/ul/li[1]/a').click()
driver.switch_to.frame('frmDesk')
driver.switch_to.frame('frmReport')

# driver.find_element(By.XPATH,'/html/body/div/div[1]/table/tbody/tr[1]/td[14]/a[1]').click()

AiSleep_click("/html/body/div/div[1]/table/tbody/tr[1]/td[14]/a[1]")
# driver.switch_to.parent_frame()
# driver.switch_to.default_content()
# driver.switch_to.frame('frmbody')
# driver.switch_to.frame('frmDesk')
# driver.swithTo().frame(driver.findElement(By.tagname("iframe")))
# driver.switch_to.frame(0)
# print(driver.switch_to.frame(0))
# driver.switch_to.frame('frmReportA')

# driver.swithTo().frame(driver.findElement(By.tagname("iframe")))
# driver.swithTo().frame(driver.findElement(By.tagname("iframe")))


# iframe
n = driver.find_element(By.XPATH, '//*[@id="tr0_bz1_"]')
print('定位到的输入框长度为：'+len(n))
print('定位到的输入框为：'+n)
driver.find_element(By.XPATH, '//*[@id="tr0_bz1_"]').click()
driver.find_element(By.XPATH, '//*[@id="tr0_bz1_"]').send_keys('测试输入')
sleep(5)
driver.quit()


