#! /Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding:utf-8 -*-
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from article_page.article_app import Article_App
from utils.my_utils import highlight_element_appium
from yinhe_page.yinhe_app import Yinhe_App
import time

class TestDemo():
    def setup_class(self):
        pass

    def teardown_class(self):
        pass

    def setup(self):
        # Article_App.start()
        # Yinhe_App.yinhe2_start()
        self.mainpage = Yinhe_App.yinhe3_start()

    # @pytest.mark.parametrize('a,b,c',[
    #     (1,1,1)
    # ])
    # 未使用caps["noReset"] = "true"时会出现各种初始化弹框处理
    def test_start_app(self):
        # 个人信息安全提示弹框
        WebDriverWait(self.driver,10).until(
            EC.visibility_of_element_located((By.ID,"com.ss.android.article.lite:id/ax4"))
        )
        ax4 = self.driver.find_element_by_id("com.ss.android.article.lite:id/ax4")
        highlight_element_appium(ax4, self.driver, "ax4.png", "ax41.png")
        ax4.click()

        # def loaded(path):
        #     if len(self.driver.find_elements_by_id("com.ss.android.article.lite:id/ax4")) >= 1:  # elements方法如果没有找到元素也不会抛异常
        #         el1 = self.driver.find_element_by_id("com.ss.android.article.lite:id/ax4")
        #         highlight_element_appium(el1, self.driver, "ax4.png", "ax41.png")
        #         el1.click()
        #         return True
        #     else:
        #         return False
        #
        # try:
        #     WebDriverWait(self.driver, 10).until(loaded) # until的参数只是方法名而已，但是这个方法必须是带有参数的!!!
        # except:
        #     print("没有提示个人信息安全")

        # 未登录状态下红包弹窗
        WebDriverWait(self.driver,10).until(
            EC.visibility_of_element_located((By.ID,"com.ss.android.article.lite:id/xs"))
        )
        xs = self.driver.find_element_by_id("com.ss.android.article.lite:id/xs")
        highlight_element_appium(xs, self.driver, "xs.png", "xs1.png")
        xs.click()

        # 点击红包之后出现登录领取红包界面
        rz = self.driver.find_element_by_id("rz")
        highlight_element_appium(rz, self.driver, "rz.png", "rz1.png")
        rz.click()

        # 点击登录领取红包按钮进入一键登录界面
        vl = self.driver.find_element_by_id("vl")
        highlight_element_appium(vl, self.driver, "vl.png", "vl1.png")
        vl.click()

        # 点击一键登录进入收到红包界面，点击赚更多的钱---进入任务界面
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "com.ss.android.article.lite:id/a5_"))
        )
        a5_ = self.driver.find_element_by_id("a5_")
        highlight_element_appium(a5_, self.driver, "a5_.png", "a5_1.png")
        a5_.click()

        # 在任务界面可能会出现新闻推荐弹框
        # TODO：1、做是否有推荐弹框的容错处理；2、需要用到窗口切换
        try:
            # WebDriverWait(self.driver, 10).until(
            #     EC.visibility_of_element_located((By.ID, "com.ss.android.article.lite:id/ql"))
            # )
            ql= self.driver.find_element_by_id("ql")
            highlight_element_appium(a5_, self.driver, "ql.png", "ql1.png")
            ql.click()
        except:
            print("在任务界面没有出现新闻推荐弹框")

    # 使用了caps["noReset"] = "true"之后，不重置初始状态，所以最开始的很多弹窗都不会有，直接进入未登录的首页状态
    def test_login(self):
        # 点击我的或者未登录
        eys = self.driver.find_elements_by_id("com.ss.android.article.lite:id/ey")
        for e in eys:
            print("ey-id下一共有以下控件："+e.text)
            if "我的" in e.text:
                highlight_element_appium(e, self.driver, "eys.png", "eys1.png")
                print("登录还是未登录：" + e.text)
                e.click()
            elif "未登录" in e.text:
                highlight_element_appium(e, self.driver, "eys.png", "eys1.png")
                print("登录还是未登录：" + e.text)
                e.click()

                # 点击未登录进入登录界面点击登录
                a78 = self.driver.find_element_by_id("com.ss.android.article.lite:id/a78")
                highlight_element_appium(a78, self.driver, "a78.png", "a781.png")
                a78.click()

                # 点击一键登录进入我的界面
                WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located((By.ID, "com.ss.android.article.lite:id/vl"))
                )
                vl = self.driver.find_element_by_id("vl")
                highlight_element_appium(vl, self.driver, "vl.png", "vl1.png")
                vl.click()

    # 种菜赚金币po模式
    def test_vegetable_coin(self):
        # 首先需要进入任务界面，通过app启动模块的某个方法进入任务界面，再封装任务page
        # App.to_task_page()
        Article_App.to_my_page()

    # 开宝箱得金币
    def test_open_box(self):
        taskpage = Article_App.to_task_page()
        # taskpage.test_webview()
        taskpage.open_box()

    def test_login(self):
        platTrans = self.mainpage.to_recommend_game("AG真人")
        platTrans.click_sure_trans(1)
        mainpage = platTrans.click_left_back()
        time.sleep(2)
        platTrans = self.mainpage.to_recommend_game("BBIN真人")
        platTrans.click_sure_trans(1)
        platTrans.click_left_back()
        # todo:平台互转获取余额失败/转账失败弹框黑名单处理

    def teardown(self):
        time.sleep(5)
        Yinhe_App.close()