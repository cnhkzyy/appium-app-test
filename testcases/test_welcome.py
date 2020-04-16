from PageObjects import *
import pytest



class TestWelcome:


    #测试首页滑屏
    @pytest.mark.welcome
    def test_welcome(self, common_driver):
        WelcomePage(common_driver).swipe_screen()
        WelcomePage(common_driver).get_spe_screenshot()
        image_text = WelcomePage(common_driver).identify_screenshot()
        assert image_text == "立即体验"

