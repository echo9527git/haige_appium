from selenium.webdriver.common.by import By

from yinhe_page.activity_page import ActivityPage
from yinhe_page.base_page import BasePage
from yinhe_page.classify_page import ClassifyPage
from yinhe_page.platformtras_page import PlatformTransPage
from utils.my_utils import highlight_element_appium


class MainPage(BasePage):
    '''




    活动精选大促-更多
    活动3个小入口
    高级代理人入口
    '''
    # 活动banner
    _banner_locator = (By.CLASS_NAME, "slide-box")
    # 系统公告
    _notice_locator = (By.CLASS_NAME, "notice-box")
    # 平台推荐 - 更多
    _platform_more_locator = (By.CLASS_NAME, "f-right")
    # 平台推荐-8个平台
    _platform_eight_locator = (By.CLASS_NAME, "recommend-item")

    def to_classify_page(self):
        self.find_and_click(self._platform_more_locator)
        return ClassifyPage(self.driver, self.black_list)

    def to_recommend_game(self, gameName):
        '''
        进入首页平台推荐中的游戏平台
        :param gameName: 平台的名称：AG真人/BG真人/BBIN真人/开元棋牌/PT电子/MG电子/AG捕鱼王/沙巴体育
        :return: 返回平台互转界面
        '''
        gamas = self.find_elements(self._platform_eight_locator)
        if gameName in "AG真人":
            # e = gamas[0]
            # print("-------------")
            # print(e)
            # highlight_element_appium(e, self.driver, "AG.png", "AG1.png")
            location = gamas[0].location
            size = gamas[0].size
            print("location= "+str(location),"--size= "+str(size))
            self.driver.get_screenshot_as_file("AG.png")
            gamas[0].click()
            print("进入：%s" %gameName)
        elif gameName in "BG真人":
            gamas[1].click()
            print("进入：%s" %gameName)
        elif gameName in "BBIN真人":
            gamas[2].click()
            print("进入：%s" %gameName)
        elif gameName in "开元棋牌":
            gamas[3].click()
            print("进入：%s" %gameName)
        elif gameName in "PT电子":
            gamas[4].click()
            print("进入：%s" %gameName)
        elif gameName in "MG电子":
            gamas[5].click()
            print("进入：%s" %gameName)
        elif gameName in "AG捕鱼王":
            gamas[6].click()
            print("进入：%s" %gameName)
        elif gameName in "沙巴体育":
            gamas[7].click()
            print("进入：%s" %gameName)
        return PlatformTransPage(self.driver, self.black_list,self)

    def to_activity_page(self):
        more_right = self.find_elements(self._platform_more_locator)
        more_right[1].click()
        return ActivityPage(self.driver, self.black_list)

