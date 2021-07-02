from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('C:/chromedriver_win32/chromedriver.exe')
url = 'https://dorm.cnu.ac.kr/intranet/login.php'
driver.get(url)
xpath = "//input[@name='idno']"
id_btn = driver.find_element_by_xpath(xpath)
id_btn.send_keys(201702026)

xpath = "//input[@name='pass']"
pass_btn = driver.find_element_by_xpath(xpath)
pass_btn.send_keys("cheld!#5")

xpath = "//input[@class='login_btn']"
enter_btn = driver.find_element_by_xpath(xpath)
enter_btn.click()

time.sleep(2)
driver.get('https://dorm.cnu.ac.kr/intranet/user/corona19_daychkform.php')
time.sleep(2)

xpath = "//input[contains(@name,'agreeall')]"
q3_btn = driver.find_element_by_xpath(xpath)
q3_btn.click()

# xpath = "//input[contains(@name,'q2') and contains(@value,'N')]"
# q2_btn = driver.find_element_by_xpath(xpath)
# q2_btn.click()
#
# xpath = "//input[contains(@name,'agree') and contains(@value,'Y')]"
# agree_btn = driver.find_element_by_xpath(xpath)
# agree_btn.click()
#
# xpath = "//input[@name='agree2']"
# agree2_btn = driver.find_element_by_xpath(xpath)
# agree2_btn.click()
#
xpath = "//input[@class='btn_blue']"
complate = driver.find_element_by_xpath(xpath)
complate.click()

alert = driver.switch_to.alert
alert.accept()
alert.accept()

