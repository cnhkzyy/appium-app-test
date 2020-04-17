from .base_page import BasePage
from appium.webdriver.webdriver import MobileBy


class IndexPage(BasePage):

    #设置手势密码
    cancel_gesture_pwd_id = "com.xxzb.fenwoo:id/btn_cancel"
    set_gesture_pwd_id = "com.xxzb.fenwoo:id/btn_confirm"

    #我
    me_xpath = "//android.widget.TextView[@text='我']"


    #点击以后再说
    def click_later(self):
        self.get_element(self.cancel_gesture_pwd_id).click()


    #点击我
    def click_me(self):
        self.get_element(self.me_xpath, by=MobileBy.XPATH).click()

