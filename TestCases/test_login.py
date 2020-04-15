from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy
import time, pytest
import logging
from Common.my_logging import *
from Common.base_driver import BaseDriver
from PageObjects import *


welcome_page = WelcomePage()
login_page = LoginPage()
index_page = IndexPage()
user_info_page = UserInfoPage()



@pytest.mark.login
def test_login_success():
    welcome_page.swipe_screen()
    welcome_page.click_experience_now()
    login_page.click_register_login()
    login_page.input_phone("18684720553")
    login_page.input_pwd("python")
    index_page.click_later()
    index_page.click_me()
    nickName = user_info_page.get_nickName()
    user_info_page.quit()
    assert nickName == "华华"



