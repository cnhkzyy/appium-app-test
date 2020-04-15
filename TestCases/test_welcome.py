from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy
import time
import pytest
import logging
from Common.my_logging import *
from PageObjects.welcome_page import WelcomePage



welcome = WelcomePage()

#滑屏操作
@pytest.mark.welcome
def test_welcome():
    welcome.swipe_screen()
    welcome.get_spe_screenshot()
    image_text = welcome.identify_screenshot()
    assert image_text == "立即体验"

