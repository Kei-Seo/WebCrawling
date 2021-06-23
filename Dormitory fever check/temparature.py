from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('Cchromedriver_win32chromedriver.exe')
url = 'httpsdorm.cnu.ac.krintranetlogin.php'
driver.get(url)
xpath = input[@name='idno']
id_btn = driver.find_element_by_xpath(xpath)
id_btn.send_keys(201702026)

xpath = input[@name='pass']
pass_btn = driver.find_element_by_xpath(xpath)
pass_btn.send_keys(cheld!#5)

xpath = input[@class='login_btn']
enter_btn = driver.find_element_by_xpath(xpath)
enter_btn.click()

time.sleep(2)
driver.get('httpsdorm.cnu.ac.krintranetusercorona19_daychkform.php')
time.sleep(2)

xpath = input[contains(@name,'q3') and contains(@value,'N')]
q3_btn = driver.find_element_by_xpath(xpath)
q3_btn.click()

xpath = input[contains(@name,'q2') and contains(@value,'N')]
q2_btn = driver.find_element_by_xpath(xpath)
q2_btn.click()

xpath = input[contains(@name,'agree') and contains(@value,'Y')]
agree_btn = driver.find_element_by_xpath(xpath)
agree_btn.click()

xpath = input[@name='agree2']
agree2_btn = driver.find_element_by_xpath(xpath)
agree2_btn.click()

xpath = input[@class='btn_blue']
complate = driver.find_element_by_xpath(xpath)
complate.click()

alert = driver.switch_to.alert
alert.accept()
alert.accept()


