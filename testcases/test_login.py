from PageObjects import *
import pytest
import re



class TestLogin:


    #正常登录
    def test_login_success(self, common_driver):
        WelcomePage(common_driver).swipe_screen()
        WelcomePage(common_driver).click_experience_now()
        LoginPage(common_driver).click_register_login()
        LoginPage(common_driver).input_phone("18684720553")
        LoginPage(common_driver).input_pwd("python")
        IndexPage(common_driver).click_later()
        IndexPage(common_driver).click_me()
        nickName = UserInfoPage(common_driver).get_nickName()
        assert nickName == "华华"


    #不填手机号登录
    def test_login_noPhone(self, common_driver):
        WelcomePage(common_driver).swipe_screen()
        WelcomePage(common_driver).click_experience_now()
        LoginPage(common_driver).click_register_login()
        LoginPage(common_driver).click_next_step()
        invalid_phone_text = LoginPage(common_driver).get_invalid_phone_text()
        assert invalid_phone_text == "无效的手机号"


    #手机号为空字符串
    def test_login_phoneIsEmpty(self, common_driver):
        WelcomePage(common_driver).swipe_screen()
        WelcomePage(common_driver).click_experience_now()
        LoginPage(common_driver).click_register_login()
        LoginPage(common_driver).input_phone("  ")
        invalid_phone_text = LoginPage(common_driver).get_invalid_phone_text()
        assert invalid_phone_text == "无效的手机号"


    #手机号长度不够
    def test_login_phoneLenError(self, common_driver):
        WelcomePage(common_driver).swipe_screen()
        WelcomePage(common_driver).click_experience_now()
        LoginPage(common_driver).click_register_login()
        LoginPage(common_driver).input_phone("135")
        invalid_phone_text = LoginPage(common_driver).get_invalid_phone_text()
        assert invalid_phone_text == "无效的手机号"



    #使用新手机号注册
    def test_login_noRegister(self, common_toast_driver):
        WelcomePage(common_toast_driver).swipe_screen()
        WelcomePage(common_toast_driver).click_experience_now()
        LoginPage(common_toast_driver).click_register_login()
        LoginPage(common_toast_driver).input_phone("13575567809")
        verify_toast_text = LoginPage(common_toast_driver).get_verify_shortMessage_toast_text()
        assert re.search("验证码已经发送到手机号为135\*\*\*\*7809,注意查收,验证码有效时间为60秒,验证码为\d{4}", verify_toast_text) != None

