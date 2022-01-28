from selenium import webdriver
import yagmail
import os
import sys
options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=/home/pi/.config/chromium')
options.add_argument('--profile-directory=Default')
teslaaccount = "http://www.tesla.com/teslaaccount"
profile = "http://www.tesla.com/teslaaccount/profile?rn=RNxxxxxxxxx" #put your RN here
logout = "http://www.tesla.com/user/logout/"
driver = webdriver.Chrome(options=options)
driver.get(teslaaccount)
python_button = driver.find_element_by_id('form-submit-continue')
python_button.click()
driver.get(profile)
if "LRW" in driver.page_source: #you might need to change this to whatever prefixes your VIN
    yag = yagmail.SMTP(‘youremail@address.com’, ‘password’) #put your email address and password here so yagmail can use it.
    yag.send(‘addressyouwant@toemail.com’, 'TESLA VIN ALERT', "Your VIN has been found") #put the email address you want to send a notification to here
    driver.get(logout)
    driver.quit()
    sys.stdout.flush()
    os._exit(0)
else:
    driver.get(logout)
    driver.quit()
    sys.stdout.flush()
    os._exit(0)
