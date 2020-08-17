
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.my_utils import handle_element_exception


class BasePage:



    def __init__(self,driver: webdriver,black_list):
        self.driver = driver
        self.black_list = black_list
    def find_element(self,locator):
        '''
        基础页面类中封装自己的定位方法---具备异常处理逻辑
        :param locator: 一个元组定位符
        :return: 返回一个定位到的元素，因为需要对元素进行操作
        '''
        try:
            # WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(locator))
            return self.driver.find_element(*locator) #可能会出现异常，如果不出现就直接return
        except:# 如果出现异常就对处理，思路是循环去黑名单中找一些异常弹框：广告、好评、升级、tips等
            handle_element_exception(self.driver,self.black_list)
            # 可能找了两次之后还是没有找到，那么可能需要调用本身进行递归处理
            # * 的作用其实就是把序列 locator 中的每个元素，当作位置参数传进去
            return self.find_element(*locator)

    def find_elements(self,locator):
        return self.driver.find_elements(*locator)

    def find_and_click(self,locator):
        '''
        定位并点击元素，点击的时候也有可能会抛异常，所以也需要异常处理
        :param locator: 一个元组定位符
        :return:
        '''
        try:
            self.find_element(locator).click()
        except:
            handle_element_exception(self.driver,self.black_list)
            # 处理了异常再查找点击
            self.find_element(*locator).click()


