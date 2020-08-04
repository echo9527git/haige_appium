from appium import webdriver
import os

class MYDriver():
    platformName = os.getenv("platformName")
    appPackage = os.getenv("appPackage")
    appActivity = os.getenv("appActivity")

    def __init__(self):
        self.caps = {}
        self.caps["platformName"] = self.platformName
        self.caps["deviceName"] = "emulator-5554"
        # 澳门银河com.gy2yinhe.www/.MainActivity
        self.caps["appPackage"] = self.appPackage
        self.caps["appActivity"] = self.appActivity
        # 自动赋予App权限
        self.caps["autoGrantPermissions"] = "true"
        # # 是否在测试前后重置相关环境
        self.caps["noReset"] = "true"

    def get_yinhe_ios_dirver(self):
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", self.caps)
        return self.driver

    def get_yinhe_android_dirver(self):
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", self.caps)
        return self.driver

    def get_jinsha_ios_dirver(self):
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", self.caps)
        return self.driver

    def get_jinsha_android_dirver(self):
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", self.caps)
        return self.driver