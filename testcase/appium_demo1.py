#! /Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding:utf-8 -*-
# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from utils.my_utils import highlight_element_appium



caps = {}
caps["platformName"] = "android"
caps["deviceName"] = "LMX4C17A04007025"
caps["appPackage"] = "com.ss.android.article.lite"
caps["appActivity"] = ".activity.SplashActivity"
caps["autoGrantPermissions"] = "true"

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
driver.implicitly_wait(3)

el1 = driver.find_element_by_id("com.ss.android.article.lite:id/ax4")

highlight_element_appium(el1,driver,"ax4.png","ax41.png")
el1.click()

el4 = driver.find_element_by_id("com.ss.android.article.lite:id/xs")
highlight_element_appium(el4,driver,"xs.png","xs1.png")
el4.click()




driver.quit()

