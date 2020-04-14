from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy
import time
import pytest
import logging
from Common.my_logging import *



#操作对象的设备信息
desired_caps = {}
desired_caps["platformName"] = "Android"
desired_caps["platformVersion"] = "5.1.1"
desired_caps["deviceName"] = "Android Emulator"
desired_caps["appPackage"] = "com.xxzb.fenwoo"
desired_caps["appActivity"] = "com.xxzb.fenwoo.activity.addition.WelcomeActivity"



#滑屏操作
@pytest.mark.welcome
def test_welcome():
    #连接appium
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    time.sleep(3)
    logging.info("加载test_welcome")
    logging.info("test_welcome_driver是: " + str(driver))
    logging.info("test_welcome开始了!")
    logging.info("test_welcome的driver是: " + str(driver))
    size = driver.get_window_size()
    for i in range(3):
        driver.swipe(size["width"] * 0.9, size["height"] * 0.5, size["width"] * 0.1, size["height"] * 0.5, 200)
    WebDriverWait(driver, 10, 1).until(EC.visibility_of_element_located((MobileBy.ID, "com.xxzb.fenwoo:id/btn_start")))
    driver.find_element_by_id("com.xxzb.fenwoo:id/btn_start").click()
    driver.close_app()
    driver.quit()
    assert True == True

