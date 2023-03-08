from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.action_chains import ActionChains

opts = Options()
#set Surf as the browser to be used
opts.binary_location = "c:\\Users\\IT\\AppData\\Local\\Chromium\\Application\\surf.exe"
#set chromedriver supports 110
driver = webdriver.Chrome(executable_path='c:\\dev\\surf\\surfchromium\\selenium\\chromedriver.exe',chrome_options=opts)
#sample website
driver.get("https://admin.surf-admin.link/lp_login.html")
time.sleep(5)
#submit user name
actions = ActionChains(driver)
actions.send_keys('ziv@democompany1.com')
actions.perform()
actions.send_keys(Keys.RETURN)
actions.perform()
time.sleep(3)
#submit password
actions.send_keys('Panda230?')
actions.perform()
actions.send_keys(Keys.RETURN)
actions.perform()
time.sleep(5)
driver.close()