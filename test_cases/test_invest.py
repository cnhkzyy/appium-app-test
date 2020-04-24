from page_objects import *
from test_datas import *
import pytest
import re
import allure


@allure.feature("投资功能")
class TestInvest:

    #投资成功
    @pytest.mark.fail
    #@pytest.mark.flaky(reruns=1, reruns_delay=2)
    @allure.story("正常投资")
    @allure.title("投资功能：正常投资")
    @allure.severity("blocker")
    @allure.tag("最重要", "回归测试")
    @allure.issue("http://192.168.0.109:8080/browse/FUT-2", name="用户投资后显示投资金额不正确")
    @allure.description("投资功能：正常情况下进行投资")
    def test_invest_success(self, common_driver):
        WelcomePage(common_driver).swipe_screen()
        WelcomePage(common_driver).click_experience_now()
        LoginPage(common_driver).click_register_login()
        LoginPage(common_driver).input_phone(login_success_data["phone"])
        LoginPage(common_driver).input_pwd(login_success_data["pwd"])
        IndexPage(common_driver).click_later()
        InvestPage(common_driver).enter_invest()
        before_invest_money = InvestPage(common_driver).get_user_left_money()
        InvestPage(common_driver).input_invest_money(invest_success_data["money"])
        InvestPage(common_driver).invest_now()
        InvestPage(common_driver).click_confirm()
        InvestPage(common_driver).click_back()
        IndexPage(common_driver).click_me()
        after_invest_money = UserInfoPage(common_driver).get_user_left_money()
        assert float(before_invest_money) == float(after_invest_money) + invest_success_data["check"]



    #不输入金额
    @allure.story("不输入金额")
    @allure.title("投资功能：不输入金额")
    @allure.severity("critical")
    @allure.tag("次重要")
    @allure.description("投资功能：不输入金额的情况下进行投资")
    def test_invest_noMoney(self, common_toast_driver):
        WelcomePage(common_toast_driver).swipe_screen()
        WelcomePage(common_toast_driver).click_experience_now()
        LoginPage(common_toast_driver).click_register_login()
        LoginPage(common_toast_driver).input_phone(login_success_data["phone"])
        LoginPage(common_toast_driver).input_pwd(login_success_data["pwd"])
        IndexPage(common_toast_driver).click_later()
        InvestPage(common_toast_driver).enter_invest()
        InvestPage(common_toast_driver).invest_now()
        toast_text_1 = InvestPage(common_toast_driver).get_toast_text_1()
        assert re.search(toast_text_1, invest_noMoney_data["check"]) != None



    #输入金额为0
    @pytest.mark.invest
    @allure.story("输入金额为0")
    @allure.title("投资功能：输入金额为0")
    @allure.severity("critical")
    @allure.tag("次重要")
    @allure.description("投资功能：输入金额为0的情况下进行投资")
    def test_invest_zeroMoney(self, common_toast_driver):
        WelcomePage(common_toast_driver).swipe_screen()
        WelcomePage(common_toast_driver).click_experience_now()
        LoginPage(common_toast_driver).click_register_login()
        LoginPage(common_toast_driver).input_phone(login_success_data["phone"])
        LoginPage(common_toast_driver).input_pwd(login_success_data["pwd"])
        IndexPage(common_toast_driver).click_later()
        InvestPage(common_toast_driver).enter_invest()
        InvestPage(common_toast_driver).input_invest_money(invest_zeroMoney_data["money"])
        InvestPage(common_toast_driver).invest_now()
        toast_text_2 = InvestPage(common_toast_driver).get_toast_text_2()
        assert re.search(toast_text_2, invest_zeroMoney_data["check"]) != None



    #输入投资不是100的整数倍
    @pytest.mark.invest
    @allure.story("投资金额不是100的整数倍")
    @allure.title("投资功能：投资金额不是100的整数倍")
    @allure.severity("critical")
    @allure.tag("次重要")
    @allure.description("投资功能：投资金额不是100的整数倍的情况下进行投资")
    def test_invest_noMutil_money(self, common_toast_driver):
        WelcomePage(common_toast_driver).swipe_screen()
        WelcomePage(common_toast_driver).click_experience_now()
        LoginPage(common_toast_driver).click_register_login()
        LoginPage(common_toast_driver).input_phone(login_success_data["phone"])
        LoginPage(common_toast_driver).input_pwd(login_success_data["pwd"])
        IndexPage(common_toast_driver).click_later()
        InvestPage(common_toast_driver).enter_invest()
        InvestPage(common_toast_driver).input_invest_money(invest_noMulti_money_data["money"])
        InvestPage(common_toast_driver).invest_now()
        toast_text_3 = InvestPage(common_toast_driver).get_toast_text_3()
        assert re.search(toast_text_3, invest_noMulti_money_data["check"]) != None



