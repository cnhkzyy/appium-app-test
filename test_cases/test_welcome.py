from page_objects import *
import pytest
import allure


@allure.feature("欢迎页功能")
class TestWelcome:


    #测试首页滑屏
    @pytest.mark.welcome
    @allure.story("欢迎页滑屏")
    @allure.title("欢迎页功能：正常滑屏")
    @allure.severity("blocker")
    @allure.tag("最重要", "回归测试")
    @allure.description("用例描述：进入欢迎页滑屏")
    def test_welcome(self, common_driver):
        WelcomePage(common_driver).swipe_screen()
        try:
            WelcomePage(common_driver).click_experience_now()
            assert True == True
        except Exception as e:
            assert True == False

