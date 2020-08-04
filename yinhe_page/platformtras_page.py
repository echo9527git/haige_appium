from appium.webdriver import webdriver
from selenium.webdriver.common.by import By

from yinhe_page.base_page import BasePage
from time import sleep
from utils.my_utils import highlight_element_appium

class PlatformTransPage(BasePage):
    def __init__(self, driver: webdriver, black_list,which_page):
        self.driver = driver
        self.black_list = black_list
        self.which_page = which_page

    # 返回
    _back_locator = (By.CLASS_NAME,"icon-back")
    # 转出/转入
    _trans_out_in_money_locator = (By.CLASS_NAME,"item-after")
    # 金额
    _money_edit_locator = (By.CSS_SELECTOR,"input[type='number']")
    # 确定转账--通过Xpath父子关系寻找
    # _sure_trans_locator = (By.XPATH,"//div[@class='button-div']")-------为什么不可以？
    _sure_trans_locator = (By.CLASS_NAME,"button-div")
    # 直接游戏
    _direct_game_locator = (By.XPATH,'//*[@id="globalControl"]/div[7]/div[2]/ion-modal-view/ion-content/div[1]/div/div[3]/span[2]')
    # 转账成功之后的确定弹框---通过串联定位
    _success_sure_loctor = (By.CLASS_NAME,"popup-buttons")


    def click_left_back(self):
        '''
        平台互转节目左上角返回
        :return:
        '''
        self.find_and_click(self._back_locator)
        print("是从哪个页面进入的平台互转：")
        print(self.which_page)
        return self.which_page

    def click_sure_trans(self,money):
        '''
        输入金额并点击确定转账
        :param money: 需要转入的金额
        :return: 没有返回值
        '''
        try:
            boxs = self.find_elements(self._trans_out_in_money_locator)
            print(boxs)
            print("转出选项："+boxs[0].text)
            self.find_element(self._money_edit_locator).send_keys(money)
            # 输入金额之后需要点击一个非键盘区域使键盘收回，点击转入框
            boxs[1].click()
            # sure_button = self.find_element(self._sure_trans_locator)
            # 使用父元素定位子元素--串联寻找
            sure_button = self.find_element(self._sure_trans_locator).find_element_by_tag_name('span')
            print("sure_button:" + sure_button.text)
            sure_button.click()
            # 点击确定转账之后查看转入的text
            sleep(2)
            print(self.find_elements(self._trans_out_in_money_locator)[1].text)
            # 转账成功或者失败确定--父子关系串联定位
            success_button = self.find_element(self._success_sure_loctor).find_element_by_tag_name("button")
            success_button.click()
            print("转账成功确定")
        except: # 抛了异常，说明获取余额失败，点击失败弹框-确定
            # 转账成功或者失败确定--父子关系串联定位
            success_button = self.find_element(self._success_sure_loctor).find_element_by_tag_name("button")
            # highlight_element_appium(success_button,self.driver,"trans_faild.png","trans_faild1.png")
            success_button.click()
            print("抛了异常，说明获取余额失败，点击失败弹框-确定")

