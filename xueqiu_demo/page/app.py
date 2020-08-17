import yaml
from appium import webdriver

from xueqiu_demo.page.base_page import BasePage
from xueqiu_demo.page.main_page import MainPage


class APP(BasePage):

    _app_package = 'com.xueqiu.android'
    _app_activity = '.common.MainActivity'
    def start(self):
        # 如果driver已经初始化，那么就直接用，不需要重新初始化
        if self._driver is None:
            caps = dict()
            caps["platformName"] = "android"
            caps["deviceName"] = "127.0.0.1:21503"
            # caps["udid"] = "emulator-5554"
            # caps["udid"] = "LMX4C17A04007025"
            # 澳门银河com.gy2yinhe.www/.MainActivity
            caps["appPackage"] = self._app_package
            caps["appActivity"] = self._app_activity
            # 自动赋予App权限
            caps["autoGrantPermissions"] = "true"
            # # 是否在测试前后重置相关环境
            caps["noReset"] = "true"

            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        else:
            # 直接复用driver
            self._driver.start_activity(self._app_package,self._app_activity)
        self._driver.implicitly_wait(5)
        return self


    def start_caps(self):
        path = 'C:/Users/Administrator/PycharmProjects/haige_appium/xueqiu_demo/config/config.yaml'
        cap = yaml.safe_load(open(path))['caps']
        print(cap)
        # 如果driver已经初始化，那么就直接用，不需要重新初始化
        if self._driver is None:
            caps = dict()
            caps["platformName"] = cap['platformName']
            caps["deviceName"] = cap['deviceName']
            # caps["udid"] = "emulator-5554"
            # caps["udid"] = "LMX4C17A04007025"
            # 澳门银河com.gy2yinhe.www/.MainActivity
            caps["appPackage"] = cap['appPackage']
            caps["appActivity"] = cap['appActivity']
            # 自动赋予App权限
            caps["autoGrantPermissions"] = cap['autoGrantPermissions']
            # # 是否在测试前后重置相关环境
            caps["noReset"] = cap['noReset']

            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        else:
            # 直接复用driver
            self._driver.start_activity(self._app_package,self._app_activity)
        self._driver.implicitly_wait(5)
        return self


    def main(self) -> MainPage:
        return MainPage(self._driver)
