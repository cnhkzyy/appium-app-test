from appium import webdriver
from .conf_dir import caps_dir
import yaml
import os


class BaseDriver:

    def __init__(self, device_info):
        self.device_info = device_info
        cmd = "start appium -p {0} -bp {1} -U 127.0.0.1:{2}".format(self.device_info["server_port"], self.device_info["server_port"] + 1, self.device_info["device_port"])
        os.system(cmd)



    def base_driver(self, automationName="appium"):
        fs = open(f"{caps_dir}//caps.yml")
        #平台名称、包名、Activity名称、超时时间、是否重置、server_ip、
        desired_caps = yaml.load(fs, Loader=yaml.FullLoader)
        #版本信息
        desired_caps["platform_version"] = self.device_info["platform_version"]
        #设备名称
        desired_caps["deviceName"] = f"127.0.0.1:{self.device_info['device_port']}"
        #系统端口号
        desired_caps["systemPort"] = self.device_info["system_port"]

        if automationName != "appium":
            desired_caps["automationName"] = automationName

        driver = webdriver.Remote(f"http://127.0.0.1:{self.device_info['server_port']}/wd/hub", desired_capabilities=desired_caps)
        return driver


