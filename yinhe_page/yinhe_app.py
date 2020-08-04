from selenium.webdriver.common.by import By

from driver.my_driver import My_Driver
from utils.my_utils import handle_element_exception

from yinhe_page.classify_page import ClassifyPage
from yinhe_page.deposit_page import DepositPage
from yinhe_page.main_page import MainPage
import time

from appium import webdriver
from yinhe_page.my_page import MyPage
from yinhe_page.service_page import ServicePage


class Yinhe_App(object):
    # 因为是纯h5代码打包的app，所以启动之后直接切换到webview
    @classmethod
    def yinhe2_start(cls):
        # 黑名单：异常弹框：广告、好评、升级、tips等
        cls.black_list = [
            (By.ID, "image_cancle"),
            (By.ID, "tips"),
            (By.ID, "cancle")
        ]

        cls.driver = My_Driver.my_yinhe2_driver()
        cls.driver.implicitly_wait(10)
        time.sleep(10)
        # ['NATIVE_APP', 'WEBVIEW_com.gy2yinhe.www', 'WEBVIEW_xweb']
        contexts = cls.driver.contexts
        print(contexts)
        print("切换之前context="+cls.driver.current_context)
        cls.driver.switch_to.context(contexts[1])
        print("切换之后context=" + cls.driver.current_context)
        # 在启动app的时候需要有一个app完全启动成功的一个标记 todo：
        # 启动app完成之后需要处理各种弹框：热更新/签到日历/公告todo：

        return MainPage(cls.driver,cls.black_list)

    @classmethod
    def yinhe3_start(cls):
        cls.black_list = [
            (By.CLASS_NAME,"titleclose"),# 公告弹窗关闭
        ]
        cls.driver = My_Driver.my_yinhe3_driver()
        cls.driver.implicitly_wait(10)
        time.sleep(5)
        # ['NATIVE_APP', 'WEBVIEW_com.gy2yinhe.www', 'WEBVIEW_xweb']
        contexts = cls.driver.contexts
        print(contexts)
        print("切换之前context=" + cls.driver.current_context)
        cls.driver.switch_to.context(contexts[1])
        print("切换之后context=" + cls.driver.current_context)
        # 在启动app的时候需要有一个app完全启动成功的一个标记 todo：
        # 启动app完成之后需要处理各种弹框：热更新/签到日历/公告todo：
        handle_element_exception(cls.driver, cls.black_list)
        return MainPage(cls.driver,cls.black_list)


    @classmethod
    def close(cls):
        cls.driver.quit()

    @classmethod
    def to_classify_page(cls):
        cls.driver.find_element_by_class_name("icon-parkinglot").click
        print("进入分类页面")
        return ClassifyPage(cls.driver)

    @classmethod
    def to_deposit_page(cls):
        cls.driver.find_element_by_class_name("icon-cunkuan").click
        print("进入存款页面")
        return DepositPage(cls.driver)

    @classmethod
    def to_service_page(cls):
        cls.driver.find_element_by_class_name("icon-message").click
        print("进入客服页面")
        return ServicePage(cls.driver)

    @classmethod
    def to_mypage(cls):
        cls.driver.find_element_by_class_name("icon-my_line").click
        print("进入我的页面")
        return MyPage(cls.driver)