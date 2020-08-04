
from yinhe_page.yinhe_app import Yinhe_App
from yinhe_page.main_page import MainPage

class YinheTest():
    def setup(self):
        self.driver = Yinhe_App.yinhe2_start()

    def test_login(self):
       main =  MainPage.test_hehe()



    def teardown(self):
        self.driver.quit()