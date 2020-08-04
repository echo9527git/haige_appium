#! /Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding:utf-8 -*-
# 封装app相关的所有功能，比如启动、安装、卸载



from article_page.main_page import MainPage
from article_page.my_page import MyPage
from article_page.shwo_page import ShowPage
from article_page.task_page import TaskPage
from article_page.video_page import VideoPage
from utils.my_utils import highlight_element_appium
from driver.my_driver import My_Driver

import time

class Article_App:
    @classmethod # 标记为类方法，这样就可以通过类名.来调用方法，不需要类的实例来调用；
    def start(cls): # 类方法的自身不是self，而是cls

        cls.driver = My_Driver.my_article_driver()
        cls.driver.implicitly_wait(30)
        # 启动之后跳过splash
        # are = cls.driver.find_element_by_id("com.ss.android.article.lite:id/are")
        # highlight_element_appium(are, cls.driver, "are.png", "are1.png")
        # if EC.visibility_of_element_located((By.ID,"com.ss.android.article.lite:id/are")):
        #     are.click()
        # else:
        #     print("splash已经消失，没有进行点击")

        # TODO：由于打开app之后有可能是第一次或者是未登录状态，所以还需要对这些情况进行处理

        # 启动app之后会进入首页，所以需要返回一个首页的对象
        return MainPage(cls.driver)

    @classmethod
    def to_video_page(cls):
        cls._to_page(cls,cls.driver,"视频")
        return VideoPage(cls.driver)

    @classmethod
    def to_show_page(cls):
        cls._to_page(cls,cls.driver, "放映厅")
        return ShowPage(cls.driver)

    @classmethod
    def to_task_page(cls):
        cls._to_page(cls,cls.driver, "任务")
        return TaskPage(cls.driver)

    @classmethod
    def to_my_page(cls):
        cls._to_page(cls,cls.driver, "我的")
        return MyPage(cls.driver)

    def _to_page(self,driver,where):
        time.sleep(5)
        eys = driver.find_elements_by_id("com.ss.android.article.lite:id/ey")
        for e in eys:
            print("ey-id下一共有以下控件：" + e.text)
            if where in e.text:
                highlight_element_appium(e, driver, "eys.png", "eys1.png")
                print("进入页面：" + e.text)
                print(e)
                e.click()
                break # 当找到页面点击之后跳出循环
            else:
                print("没有"+where+"页面")

