from .base_page import BasePage

class UserInfoPage(BasePage):

    #昵称
    nickName_id = "com.xxzb.fenwoo:id/tv_name"


    #获取昵称
    def get_nickName(self):
        nickName = self.get_element(self.nickName_id).text
        return nickName

