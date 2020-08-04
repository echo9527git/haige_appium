#! /Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding:utf-8 -*-
from appium import webdriver


class VideoPage(object):
    def __init__(self,driver: webdriver):
        self.driver = driver