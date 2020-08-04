#! /Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding:utf-8 -*-
from appium import webdriver


class MainPage:
    def __init__(self, dirver: webdriver):# 指明参数的类型，方便对方法的调用
        self.driver = dirver