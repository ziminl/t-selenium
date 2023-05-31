# pip install webdriver-manager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

import time
from time import sleep

chrome_options = Options()
chrome_options. add_experimental_option("detach", True)


options = Options()
options.add_experimental_option('detach', True)  # 브라우저 바로 닫힘 방지
options.add_experimental_option('excludeSwitches', ['enable-logging'])  # 불필요한 메시지 제거
service = Service(ChromeDriverManager().install())

driverPath = '/usr/local/Caskroom/chromedriver/89.0.4389.23/chromedriver'
binaryPath = 'C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe'
options = webdriver.ChromeOptions()
options.binary_location = binaryPath
driver = webdriver.Chrome(service=service, chrome_options=options)

username = '1' 
password = '2'


driver.get("https://twitter.com/login")
#Old API	New API
#find_element_by_id(‘id’)	find_element(By.ID, ‘id’)
#find_element_by_name(‘name’)	find_element(By.NAME, ‘name’)
#find_element_by_xpath(‘xpath’)	find_element(By.XPATH, ‘xpath’)
sleep(4)
userinput = driver.find_element(By.XPATH, "//input[@name='text']")
userinput.send_keys(username)
userinput.send_keys(Keys.ENTER)

sleep(2)
passinput= driver.find_element(By.NAME, "password")
passinput.send_keys(password)
passinput.send_keys(Keys.ENTER)
print("password submitted\nsuccess login")


sleep(2)
tweet_input = driver.find_element(By.CLASS_NAME,'public-DraftStyleDefault-block')

tweet_input.send_keys("Text")
tweet_input.send_keys(Keys.ENTER)
sleep(5)
tweet_text = driver.find_element(By.XPATH,'//div[@data-testid="toolBar"]/div[2]/div[3]/div')

tweet_text.click()
sleep(4)

sleep(100)









