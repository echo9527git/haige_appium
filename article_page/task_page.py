#! /Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding:utf-8 -*-
from appium import webdriver
import time


class TaskPage(object):
    def __init__(self, driver: webdriver):
        self.driver = driver


    @classmethod
    def open_box(self):
        self.switch_context("WEBVIEW_xweb")
        # /hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TabHost/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[4]/android.view.View/android.widget.Image/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TabHost/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.RelativeLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[4]/android.view.View/android.widget.Image
        xpth ="//*[@resource_id='com.ss.android.article.lite:id/app']/parent::android.view.View[4]"
        box = self.driver.find_element_by_xpath(xpth)
        print(box+"==============")
        # self.driver.find_elements_by_id("com.ss.android.article.lite:id/ey").click()
        # print("点击开启宝箱")

    def test_webview(self):
        for i in range(5):
            # ['NATIVE_APP', 'WEBVIEW_com.tencent.mm:appbrand0']
            print(self.driver.contexts)
        # ['NATIVE_APP', 'WEBVIEW_com.tencent.mm:appbrand0']
        # print("当前context："+self.driver.current_context)
        print("context-1:"+self.driver.contexts[0])
        print("context-2:" + self.driver.contexts[1])
        # self.driver.switch_to.context(self.driver.contexts[1])
        # print("当前context：" + self.driver.current_context)

    def switch_context(self,which):
        '''
        自定义切换context方法
        :param which: NATIVE或者WEB
        :return:
        '''
        contexts = self.driver.contexts
        print(contexts)
        for context in range(len(contexts)-1):
            if which in "NATIVE_APP":
                self.driver.switch_to.context(contexts[0]);
                print("切换到--NATIVE_APP")
            elif which in "WEBVIEW_xweb":
                time.sleep(3)
                print("当前context："+self.driver.current_context)
                self.driver.switch_to.context(contexts[1]);
                print("切换到--WEBVIEW_xweb")
            else:
                print("没有找到需要切换的-"+which+"-页面")