from .base_page import BasePage
import re

class InvestPage(BasePage):

    #元素定位
    enter_invest_id = "com.xxzb.fenwoo:id/pbar_process"
    input_invest_money_id = "com.xxzb.fenwoo:id/et_investamount"
    invest_now_id = "com.xxzb.fenwoo:id/btn_investnow"
    confirm_invest_success_id = "com.xxzb.fenwoo:id/btn_confirm"
    back_id = "com.xxzb.fenwoo:id/btn_back"
    toast_xpath_1 = "//*[contains(@text, '请输入')]"
    toast_xpath_2 = "//*[contains(@text, '最小投资金额为')]"
    toast_xpath_3 = "//*[contains(@text, '投资金额必须为')]"



    #进入投资页面
    def enter_invest(self):
        self.get_element(self.enter_invest_id).click()


    #获取用户可用余额
    def get_user_left_money(self):
        user_left_money = re.sub(r"\D", "", self.get_element(self.input_invest_money_id).text)
        return user_left_money


    #输入投资金额
    def input_invest_money(self, money):
        #输入投资金额
        self.get_element(self.input_invest_money_id).send_keys(money)


    #点击立即投资
    def invest_now(self):
        self.get_element(self.invest_now_id).click()


    #点击确定
    def click_confirm(self):
        self.get_element(self.confirm_invest_success_id).click()


    #点击返回
    def click_back(self):
        self.get_element(self.back_id).click()


    #获取请输入投资金额toast弹出框的文本内容
    def get_toast_text_1(self):
        toast_text_1 = self.get_toast_element(self.toast_xpath_1).text
        return toast_text_1


    #获取最小投资金额toast弹出框的文本内容
    def get_toast_text_2(self):
        toast_text_2 = self.get_toast_element(self.toast_xpath_2).text
        return toast_text_2


    #获取投资金额必须为100整数倍的toast弹出框的内容
    def get_toast_text_3(self):
        toast_text_3 = self.get_toast_element(self.toast_xpath_3).text
        return toast_text_3



