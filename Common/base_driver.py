from appium import webdriver

class BaseDriver:

    #操作对象的设备信息
    desired_caps = {}
    desired_caps["platformName"] = "Android"
    desired_caps["platformVersion"] = "5.1.1"
    desired_caps["deviceName"] = "Android Emulator"
    desired_caps["appPackage"] = "com.xxzb.fenwoo"
    desired_caps["appActivity"] = "com.xxzb.fenwoo.activity.addition.WelcomeActivity"


    def base_driver(self):
        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities=self.desired_caps)
        return driver