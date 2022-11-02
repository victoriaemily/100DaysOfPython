from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException

import time

from dotenv import load_dotenv

import os

load_dotenv()

i = 0

chrome_driver_path = "C:\\Users\\victo\\Downloads\\chromedriver.exe"
URL =  "https://www.instagram.com/"

class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        self.driver.get(URL + "accounts/login/")
        print("successfully got!")
        
    def login(self, user, password):
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@name='username']").send_keys(user)
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(4)
        
    def findFollowers(self):
        time.sleep(4)
        self.driver.get(URL)
        self.driver.get(URL + "_zyozyo/followers/")
        time.sleep(4)
        return self.driver.find_elements(By.XPATH, "//div[@aria-labelledby]")
        
    def follow(self, follower, i):
        pass
        # time.sleep(3)
        # self.driver.find_elements(By.XPATH, "//button[@type='button']")[i].click()
        
myObject = InstaFollower()
myObject.login(os.getenv("IG_USER"), os.getenv("IG_PASS"))
followers = myObject.findFollowers()
for follower in followers:
    time.sleep(2)
    followers.driver.find_element(By.XPATH, "//button[@type='button']").click()




