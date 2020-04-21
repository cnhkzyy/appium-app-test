from page_objects import *
import pytest



class TestWelcome:


    #测试首页滑屏
    @pytest.mark.welcome
    def test_welcome(self, common_driver):
        WelcomePage(common_driver).swipe_screen()
        try:
            WelcomePage(common_driver).click_experience_now()
            assert True == True
        except Exception as e:
            assert True == False

