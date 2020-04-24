from page_objects import *
from test_datas import *
import pytest
import re
import allure


@pytest.mark.login
@allure.feature("登录功能")
class TestLogin:


    #正常登录
    @allure.story("正常登录")
    @allure.title("登录功能：正常登录")
    @allure.severity("blocker")
    @allure.tag("最重要", "回归测试")
    @allure.description("用例描述：使用正确的手机号和密码登录")
    def test_login_success(self, common_driver):
        WelcomePage(common_driver).swipe_screen()
        WelcomePage(common_driver).click_experience_now()
        LoginPage(common_driver).click_register_login()
        LoginPage(common_driver).input_phone(login_success_data["phone"])
        LoginPage(common_driver).input_pwd(login_success_data["pwd"])
        IndexPage(common_driver).click_later()
        IndexPage(common_driver).click_me()
        nickName = UserInfoPage(common_driver).get_nickName()
        assert nickName == login_success_data["check"]


    #不填手机号登录
    @allure.story("不填手机号登录")
    @allure.title("登录功能：不填手机号登录")
    @allure.severity("critical")
    @allure.tag("次重要")
    def test_login_noPhone(self, common_driver):
        """
        用例描述：使用空的手机号和正确的密码登录
        """
        WelcomePage(common_driver).swipe_screen()
        WelcomePage(common_driver).click_experience_now()
        LoginPage(common_driver).click_register_login()
        LoginPage(common_driver).click_next_step()
        invalid_phone_text = LoginPage(common_driver).get_invalid_phone_text()
        assert invalid_phone_text == login_noPhone_data["check"]


    #手机号为空字符串
    @allure.story("手机号为空字符串")
    @allure.title("登录功能：手机号为空字符串")
    @allure.severity("normal")
    @allure.tag("次重要")
    @allure.description("登录功能：使用空字符串的手机号和正确的密码登录")
    def test_login_phoneIsEmpty(self, common_driver):
        WelcomePage(common_driver).swipe_screen()
        WelcomePage(common_driver).click_experience_now()
        LoginPage(common_driver).click_register_login()
        LoginPage(common_driver).input_phone(login_phoneIsEmpty_data["phone"])
        invalid_phone_text = LoginPage(common_driver).get_invalid_phone_text()
        assert invalid_phone_text == login_phoneIsEmpty_data["check"]


    #手机号长度不够
    @allure.story("手机号长度不够")
    @allure.title("登录功能：手机号长度不够")
    @allure.severity("normal")
    @allure.tag("次重要")
    @allure.description("登录功能：使用长度不够的手机号和正确的密码登录")
    def test_login_phoneLenError(self, common_driver):
        WelcomePage(common_driver).swipe_screen()
        WelcomePage(common_driver).click_experience_now()
        LoginPage(common_driver).click_register_login()
        LoginPage(common_driver).input_phone(login_phoneLenError_data["phone"])
        invalid_phone_text = LoginPage(common_driver).get_invalid_phone_text()
        assert invalid_phone_text == login_phoneLenError_data["check"]



    #使用新手机号注册
    @allure.story("使用新手机号注册")
    @allure.title("登录功能：使用新手机号注册")
    @allure.severity("blocker")
    @allure.tag("最重要", "回归测试")
    @allure.description("登录功能：使用新手机号注册")
    def test_login_noRegister(self, common_toast_driver):
        WelcomePage(common_toast_driver).swipe_screen()
        WelcomePage(common_toast_driver).click_experience_now()
        LoginPage(common_toast_driver).click_register_login()
        LoginPage(common_toast_driver).input_phone(login_noRegister_data["phone"])
        verify_toast_text = LoginPage(common_toast_driver).get_verify_shortMessage_toast_text()
        assert re.search(login_noRegister_data["check"], verify_toast_text) != None


    #不填密码
    @allure.story("不填密码")
    @allure.title("登录功能：不填密码登录")
    @allure.severity("critical")
    @allure.tag("次重要")
    @allure.description("登录功能：不填密码进行登录")
    def test_login_noPwd(self, common_driver):
        WelcomePage(common_driver).swipe_screen()
        WelcomePage(common_driver).click_experience_now()
        LoginPage(common_driver).click_register_login()
        LoginPage(common_driver).input_phone(login_success_data["phone"])
        LoginPage(common_driver).click_next_step()
        assert LoginPage(common_driver).input_pwd_element() != None


    #填入密码错误
    @allure.story("密码错误")
    @allure.title("登录功能：密码错误")
    @allure.severity("critical")
    @allure.tag("次重要")
    @allure.description("登录功能：密码输错的情况下登录")
    def test_login_pwdError(self, common_driver):
        WelcomePage(common_driver).swipe_screen()
        WelcomePage(common_driver).click_experience_now()
        LoginPage(common_driver).click_register_login()
        LoginPage(common_driver).input_phone(login_phonePwd_error_data["phone"])
        LoginPage(common_driver).input_pwd(login_phonePwd_error_data["pwd"])
        phone_pwd_error_text = LoginPage(common_driver).get_phone_pwd_error_text()
        assert phone_pwd_error_text == login_phonePwd_error_data["check"]
