import os
import re
import shutil
from common.conf_dir import root_dir, logs_dir, html_reports_dir



#清缓存
def clean_cache(dir_path):
    if os.path.isdir(dir_path):
        for dir in os.listdir(dir_path):
            if os.path.isdir(os.path.join(dir_path, dir)) and re.search(r"cache", dir) != None:
                shutil.rmtree(os.path.join(dir_path, dir))
            elif os.path.isdir(os.path.join(dir_path, dir)) and re.search(r"cache", dir) == None:
                clean_cache(os.path.join(dir_path, dir))


#clean_cache(root_dir)



#清日志
def clean_log(dir_path):
    for file in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, file)) and re.search("log", file) != None:
            os.remove(os.path.join(dir_path, file))


#clean_log(logs_dir)



#清报告
def clean_report(dir_path):
    for file in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, file)) and re.search("html|xml", file) != None:
            os.remove(os.path.join(dir_path, file))


#clean_report(html_reports_dir)


from .welcome_page import WelcomePage
from .login_page import LoginPage
from .index_page import IndexPage
from .userInfo_page import UserInfoPage
from .invest_page import InvestPage
