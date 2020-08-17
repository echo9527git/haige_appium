import yaml
from appium import webdriver


# 广告弹窗id--com.xueqiu.android:id/ib_close

class BasePage():
    _driver : webdriver


    def __init__(self,driver:webdriver = None):
        self._driver = driver

    def find(self,locator):
        return self._driver.find_element(*locator)

    # 定义数据驱动
    def steps(self,path):
        with open(path) as f:
            steps = yaml.safe_load(f)
            element = None
            for step in steps:
                if 'by' in step.keys():
                    element = self.find((step['by'],step['locator']))
                if 'action' in step.keys():
                    action = step['action']
                    if action == 'click':
                        element.click()

