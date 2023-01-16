from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime
import os
import sys
profile = "http://www.tesla.com/teslaaccount/profile?rn=RNxxx" #Put your RN here
logout = "http://www.tesla.com/user/logout/"
driver = webdriver.Chrome()

def check_vin():
    print("Checking for a VIN...")
    driver.get(profile)
    username = driver.find_element(By.ID, 'form-input-identity')
    username.send_keys('xxx') #put your Tesla usernamehere
    login_button = driver.find_element(By.ID, 'form-submit-continue')
    login_button.click()
    password = driver.find_element(By.ID, 'form-input-credential')
    password.send_keys('xxx') #put your Tesla password here
    login_button = driver.find_element(By.ID, 'form-submit-continue')
    login_button.click()
    if "LRW" in driver.page_source: #Change "LRW" as necessary
        vin_found()
    else:
        vin_notfound()

def vin_found():
    print("VIN found in source code at", datetime.now())
    print("Program closing.")
    driver.get(logout)
    driver.quit()
    sys.stdout.flush()
    os._exit(0)

def vin_notfound():
    print("No VIN yet :( Checking again at specified interval.")
    driver.get(logout)
    time.sleep(3600) #Time in seconds determines how often you want to check for a VIN. I recommend no more than every hour
    check_vin()

print("WELCOME TO THE TESLA VIN CHECKER by Karlos22")
check_vin()

