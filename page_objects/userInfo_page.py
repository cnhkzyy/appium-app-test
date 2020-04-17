from .base_page import BasePage
import re


class UserInfoPage(BasePage):

    #昵称
    nickName_id = "com.xxzb.fenwoo:id/tv_name"
    #个人账户余额
    user_left_money_id = "com.xxzb.fenwoo:id/tv_leave"


    #获取昵称
    def get_nickName(self):
        nickName = self.get_element(self.nickName_id).text
        return nickName


    #获取用户余额
    def get_user_left_money(self):
        user_left_money = re.sub(",", "", self.get_element(self.user_left_money_id).text)
        return user_left_money

