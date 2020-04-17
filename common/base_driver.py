from appium import webdriver
from .conf_dir import caps_dir
import yaml


class BaseDriver:

    fs = open(f"{caps_dir}//caps.yml")
    caps_data = yaml.load(fs, Loader=yaml.FullLoader)

    #操作对象的设备信息
    desired_caps = {}
    desired_caps["platformName"] = caps_data["platformName"]
    desired_caps["platformVersion"] = caps_data["platformVersion"]
    desired_caps["deviceName"] = caps_data["deviceName"]
    desired_caps["appPackage"] = caps_data["appPackage"]
    desired_caps["appActivity"] = caps_data["appActivity"]


    def base_driver(self, automationName="appium"):
        if automationName != "appium":
            self.desired_caps["automationName"] = automationName
        driver = webdriver.Remote(f"http://{self.caps_data['server_ip']}:{self.caps_data['server_port']}/wd/hub", desired_capabilities=self.desired_caps)
        return driver


