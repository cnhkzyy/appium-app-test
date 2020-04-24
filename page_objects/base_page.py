from appium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.webdriver import MobileBy
from common.base_driver import BaseDriver
import time
from common.my_logging import *
import logging
import allure



class BasePage:

    def __init__(self, driver):
        self.driver = driver


    #等待元素可见
    def wait_eleVisible(self, locator, by=MobileBy.ID, wait_time=30):
        WebDriverWait(self.driver, wait_time).until(EC.visibility_of_element_located((by, locator)))


    #等待元素存在
    def wait_elePresence(self, locator, by=MobileBy, wait_time=30):
        WebDriverWait(self.driver, wait_time).until(EC.presence_of_element_located((by, locator)))


    #查找并返回一个元素
    def get_element(self, locator, by=MobileBy.ID, wait_time=30):
        self.wait_eleVisible(locator, by, wait_time)
        element = self.driver.find_element(by, locator)
        return element


    #查找并返回多个元素
    def get_elements(self, locator, by=MobileBy.ID, wait_time=30):
        elements = self.driver.find_elements(by, locator)
        return elements


    #滑屏
    def swipe(self, x1_percent, y1_percent, x2_percent, y2_percent, size):
        self.driver.swipe(size["width"] * x1_percent, size["height"] * y1_percent, size['width'] * x2_percent, size['height'] * y2_percent, duration=200)
        time.sleep(1)


    #获取toast元素
    def get_toast_element(self, locator, by=MobileBy.XPATH, wait_time=15):
        self.wait_elePresence(locator, by, wait_time)
        element = self.driver.find_element(by, locator)
        return element






