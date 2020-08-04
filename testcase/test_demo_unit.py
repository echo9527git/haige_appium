#! /Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding:utf-8 -*-

from unittest import TestCase
from appium import webdriver
from utils.my_utils import highlight_element_appium

class TestDemo(TestCase):
    def setUp(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "LMX4C17A04007025"
        caps["appPackage"] = "com.ss.android.article.lite"
        caps["appActivity"] = ".activity.SplashActivity"
        caps["autoGrantPermissions"] = "true"

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(3)

    def test_demo1(self):
        el1 = self.driver.find_element_by_id("com.ss.android.article.lite:id/ax4")

        highlight_element_appium(el1, self.driver, "ax4.png", "ax41.png")
        el1.click()

        el4 = self.driver.find_element_by_id("com.ss.android.article.lite:id/xs")
        highlight_element_appium(el4, self.driver, "xs.png", "xs1.png")
        el4.click()

    def tearDown(self):
        self.driver.quit()