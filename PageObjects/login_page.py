from .base_page import BasePage

class LoginPage(BasePage):

    #元素定位
    register_login_id = "com.xxzb.fenwoo:id/btn_login"
    input_phone_id = "com.xxzb.fenwoo:id/et_phone"
    input_pwd_id = "com.xxzb.fenwoo:id/et_pwd"
    next_step_id = "btn_next_step"


    #点击注册/登录
    def click_register_login(self):
        self.get_element(self.register_login_id).click()


    #输入手机号
    def input_phone(self, phone):
        self.get_element(self.input_phone_id).send_keys(phone)
        self.get_element(self.next_step_id).click()


    #输入密码
    def input_pwd(self, pwd):
        self.get_element(self.input_pwd_id).send_keys(pwd)
        self.get_element(self.next_step_id).click()



