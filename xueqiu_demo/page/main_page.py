from selenium.webdriver.common.by import By
from xueqiu_demo.page.base_page import BasePage

class MainPage(BasePage):
    _search_locator = (By.ID,'home_search')
    def goto_search(self):
        self.find(self._search_locator).click()

    def goto_search_yaml(self):
        path = 'C:/Users/Administrator/PycharmProjects/haige_appium/xueqiu_demo/page/main.yaml'
        self.steps(path)