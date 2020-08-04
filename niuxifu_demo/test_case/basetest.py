

class BaseTest():
    def setup_class(self):
        # self.mainpage = MyApp.app_start()
        print("BaseTest-setup_class")

    # TODO:获取驱动


    def teardown_class(self):
        print("BaseTest-teardown_class")
# self.driver.quit()
    def setup(self):
        # self.mainpage = MyApp.app_start()
        print("BaseTest-setup")

    # TODO:获取驱动


    def teardown(self):
        print("BaseTest-teardown")