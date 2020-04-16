from .base_page import BasePage

class LoginPage(BasePage):

    #元素定位
    register_login_id = "com.xxzb.fenwoo:id/btn_login"
    input_phone_id = "com.xxzb.fenwoo:id/et_phone"
    input_pwd_id = "com.xxzb.fenwoo:id/et_pwd"
    next_step_id = "btn_next_step"
    invalid_phone_id = "com.xxzb.fenwoo:id/tv_message"
    verify_shortMessage_toast_xpath = "//*[contains(@text, '验证码已经发送到手机')]"


    #点击注册/登录
    def click_register_login(self):
        self.get_element(self.register_login_id).click()


    #输入手机号
    def input_phone(self, phone):
        self.get_element(self.input_phone_id).send_keys(phone)
        self.click_next_step()


    #输入密码
    def input_pwd(self, pwd):
        self.get_element(self.input_pwd_id).send_keys(pwd)
        self.click_next_step()


    #点击下一步
    def click_next_step(self):
        self.get_element(self.next_step_id).click()


    #获取无效的手机号文本
    def get_invalid_phone_text(self):
        invalid_phone_text = self.get_element(self.invalid_phone_id).text
        return invalid_phone_text


    #获取验证码的提示信息
    def get_verify_shortMessage_toast_text(self):
        verify_shortMessage_toast_text = self.get_toast_element(self.verify_shortMessage_toast_xpath).text
        return verify_shortMessage_toast_text




