#! /Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding:utf-8 -*-

from appium import webdriver
from utils.my_utils import highlight_element_appium

class TestDemo:
    def setup(self):
        # App.start()
        # com.xueqiu.android /.common.MainActivity
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "LMX4C17A04007025"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["autoGrantPermissions"] = "true"

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def _to_page(self,driver,where):
        tab_names = driver.find_elements_by_id("com.xueqiu.android:id/tab_name")
        for e in tab_names:
            print("ey-id下一共有以下控件：" + e.text)
            if where in e.text:
                highlight_element_appium(e, driver, "tab_names.png", "tab_names1.png")
                print("进入页面：" + e.text)
                e.click()
                break # 当找到页面点击之后跳出循环
            else:
                print("没有"+where+"页面")

    def test_xuqiu(self):
        # 进入交易
        self._to_page(self.driver,"交易")
        print(self.driver.contexts)


    def teardown(self):
        pass
        # self.driver.quit()