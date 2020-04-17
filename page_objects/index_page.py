from .base_page import BasePage
from appium.webdriver.webdriver import MobileBy
from appium.webdriver.common.touch_action import TouchAction
import time


class IndexPage(BasePage):

    #取消设置手势密码
    cancel_gesture_pwd_id = "com.xxzb.fenwoo:id/btn_cancel"
    #立即设置
    set_now_id = "com.xxzb.fenwoo:id/btn_confirm"
    #创建手势密码
    create_gesture_pwd = "com.xxzb.fenwoo:id/btn_gesturepwd_guide"
    #九宫格绘制
    gesture_pwd_lock_view_id = "com.xxzb.fenwoo:id/gesturepwd_create_lockview"
    #确定
    confirm_id = "com.xxzb.fenwoo:id/right_btn"
    #继续
    continue_id = "com.xxzb.fenwoo:id/right_btn"
    #取消
    cancle_id = "com.xxzb.fenwoo:id/reset_btn"
    #设置成功toast
    set_success_toast_xpath = "//*[contains(@text, '手势密码设置成功')]"


    #我
    me_xpath = "//android.widget.TextView[@text='我']"


    #点击以后再说
    def click_later(self):
        self.get_element(self.cancel_gesture_pwd_id).click()


    #点击立即设置
    def click_set_now(self):
        self.get_element(self.set_now_id).click()


    #点击创建手势密码
    def click_create_gesture_pwd(self):
        self.get_element(self.create_gesture_pwd).click()


    #点击确定
    def click_confirm(self):
        self.get_element(self.confirm_id).click()


    #点击继续
    def click_continue(self):
        self.get_element(self.continue_id).click()


    #点击取消
    def click_cancle(self):
        self.get_element(self.cancle_id).click()


    #绘制九宫格密码
    def set_gesture_pwd(self):
        #进入九宫格绘制
        self.click_set_now()
        self.click_create_gesture_pwd()
        self.click_confirm()
        #获取九宫格对象
        element = self.get_element(self.gesture_pwd_lock_view_id)
        #获取大小
        size = element.size
        #获取坐标：左上角坐标
        start_point = element.location
        time.sleep(2)
        for i in range(2):
            #开始绘制
            TouchAction(self.driver).press(x=start_point["x"] + size["width"] * 1/6, y=start_point["y"] + size["height"] * 1/6).wait(200).\
                move_to(x=start_point["x"] + size["width"] * 3/6, y=start_point["y"] + size["height"] * 1/6).wait(200).\
                move_to(x=start_point["x"] + size["width"] * 5/6, y=start_point["y"] + size["height"] * 1/6).wait(200).\
                move_to(x=start_point["x"] + size["width"] * 3/6, y=start_point["y"] + size["height"] * 3/6).wait(200).\
                move_to(x=start_point["x"] + size["width"] * 1/6, y=start_point["y"] + size["height"] * 5/6).wait(200).\
                move_to(x=start_point["x"] + size["width"] * 3/6, y=start_point["y"] + size["height"] * 5/6).wait(200).\
                move_to(x=start_point["x"] + size["width"] * 5/6, y=start_point["y"] + size["height"] * 5/6).wait(200).\
                release().wait(200).perform()
            self.click_continue()



    #获取设置成功的文本
    def get_set_success_toast_text(self):
        set_success_toast_text = self.get_toast_element(self.set_success_toast_xpath).text
        return set_success_toast_text



    #点击我
    def click_me(self):
        self.get_element(self.me_xpath, by=MobileBy.XPATH).click()

