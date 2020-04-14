from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy
import time, pytest
import logging
from Common.my_logging import *


#操作对象的设备信息
desired_caps = {}
desired_caps["platformName"] = "Android"
desired_caps["platformVersion"] = "5.1.1"
desired_caps["deviceName"] = "Android Emulator"
desired_caps["appPackage"] = "com.xxzb.fenwoo"
desired_caps["appActivity"] = "com.xxzb.fenwoo.activity.addition.WelcomeActivity"



@pytest.mark.login
def test_login_success():
    #连接appium
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    time.sleep(3)
    logging.info("加载test_login")
    logging.info("test_login_driver是: " + str(driver))
    logging.info("test_login开始了!")
    logging.info("test_login的driver是: " + str(driver))
    size = driver.get_window_size()
    for i in range(3):
        driver.swipe(size["width"] * 0.9, size["height"] * 0.5, size["width"] * 0.1, size["height"] * 0.5, 200)
    WebDriverWait(driver, 10, 1).until(EC.visibility_of_element_located((MobileBy.ID, "com.xxzb.fenwoo:id/btn_start")))
    driver.find_element_by_id("com.xxzb.fenwoo:id/btn_start").click()
    WebDriverWait(driver, 10, 1).until(EC.visibility_of_element_located((MobileBy.ID, "com.xxzb.fenwoo:id/btn_login")))
    driver.find_element_by_id("com.xxzb.fenwoo:id/btn_login").click()
    WebDriverWait(driver, 10, 1).until(EC.visibility_of_element_located((MobileBy.ID, "com.xxzb.fenwoo:id/et_phone")))
    driver.find_element_by_id("com.xxzb.fenwoo:id/et_phone").send_keys("18684720553")
    driver.find_element_by_id("com.xxzb.fenwoo:id/btn_next_step").click()
    WebDriverWait(driver, 10, 1).until(EC.visibility_of_element_located((MobileBy.ID, "com.xxzb.fenwoo:id/et_pwd")))
    driver.find_element_by_id("com.xxzb.fenwoo:id/et_pwd").send_keys("python")
    driver.find_element_by_id("com.xxzb.fenwoo:id/btn_next_step").click()
    driver.close_app()
    driver.quit()
    assert True == True



