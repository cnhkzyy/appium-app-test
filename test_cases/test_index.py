from page_objects import *
from test_datas import *
import pytest


class TestIndex:


    #设置手势密码
    def test_set_gesture_pwd(self, common_toast_driver):
        WelcomePage(common_toast_driver).swipe_screen()
        WelcomePage(common_toast_driver).click_experience_now()
        LoginPage(common_toast_driver).click_register_login()
        LoginPage(common_toast_driver).input_phone(login_success_data["phone"])
        LoginPage(common_toast_driver).input_pwd(login_success_data["pwd"])
        IndexPage(common_toast_driver).set_gesture_pwd()
        set_success_toast_text = IndexPage(common_toast_driver).get_set_success_toast_text()
        assert set_success_toast_text == "手势密码设置成功"
