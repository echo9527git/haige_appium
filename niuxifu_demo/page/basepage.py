from appium import webdriver
from selenium.webdriver.common.by import By

from niuxifu_demo.mydriver.my_driver import MYDriver


class BasePage():
    def __init__(self,driver: webdriver):
        self.driver = driver

    # todo:初步判断每个页面都需要驱动

    def findelement(self,*loctor):
        self.driver.find_element((By.ID,'kw'))
        pass

    def click(self):
        pass

    def input(self):
        pass

    def double_click(self):
        pass
