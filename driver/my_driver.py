#! /Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding:utf-8 -*-
from appium import webdriver
# 共赢2
# 银河pc：https://98y77.com//
# 银河h5: https://h5.98y77.com//

# 共赢3
# 银河pc：https://4329yh.com/
# 银河h5: https://h5.4329yh.com

class My_Driver:
    @classmethod
    def my_article_driver(self):
        caps = {}
        # 'automationName': 'uiautomator2'
        # caps["automationName"] = "uiautomator2"
        caps["platformName"] = "android"
        caps["deviceName"] = "emulator-5554"
        # 今日头条极速版
        caps["appPackage"] = "com.ss.android.article.lite"
        caps["appActivity"] = ".activity.SplashActivity"
        # 澳门银河com.gy2yinhe.www/.MainActivity
        # caps["appPackage"] = "com.gy2yinhe.www"
        # caps["appActivity"] = ".MainActivity"
        # 自动赋予App权限
        caps["autoGrantPermissions"] = "true"
        # # 是否在测试前后重置相关环境
        caps["noReset"] = "true"
        # 这玩意儿会删掉app
        # caps["fullReset"] = "true"
        # # 是否需要输入非英文之外的语言并在测试完成后重置输入法
        # caps["unicodeKeyBoard"] = "true"
        # caps["resetKeyBoard"] = "true"

        driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)



        # TODO:后续将selenium及iOS下的driver都封装在这里
        return driver

    @classmethod
    def my_yinhe2_driver(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "emulator-5554"
        # 澳门银河com.gy2yinhe.www/.MainActivity
        caps["appPackage"] = "com.gy2yinhe.www"
        caps["appActivity"] = ".MainActivity"
        # 自动赋予App权限
        caps["autoGrantPermissions"] = "true"
        # # 是否在测试前后重置相关环境
        caps["noReset"] = "true"

        driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

        # TODO:后续将selenium及iOS下的driver都封装在这里
        return driver

    @classmethod
    def my_yinhe3_driver(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "emulator-5554"
        caps["udid"] = "emulator-5554"
        # caps["udid"] = "LMX4C17A04007025"
        # 澳门银河com.gy2yinhe.www/.MainActivity
        caps["appPackage"] = "com.gy3yinhe.www"
        caps["appActivity"] = ".MainActivity"
        # 自动赋予App权限
        caps["autoGrantPermissions"] = "true"
        # # 是否在测试前后重置相关环境
        caps["noReset"] = "true"

        driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

        # TODO:后续将selenium及iOS下的driver都封装在这里
        return driver