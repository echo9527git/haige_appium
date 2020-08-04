from niuxifu_demo.mydriver.my_driver import MYDriver
from niuxifu_demo.page.main_page import MainPage


class MyApp():
    @staticmethod
    def app_start(self):
        self.driver = MYDriver('android','com.jinsha.www','.MainActivity').get_jinsha_ios_dirver()
        return MainPage(self.driver)
    def app_close(self):
        pass
    # TODO: