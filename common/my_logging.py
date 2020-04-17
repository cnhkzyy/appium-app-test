import logging
import time, os
from logging.handlers import RotatingFileHandler
from .conf_dir import logs_dir


#设置输出的日志内容格式
fmt = '%(asctime)s  %(filename)s  %(funcName)s [line:%(lineno)d] %(levelname)s %(message)s'
datefmt = '%a, %d %b %Y %H:%M:%S'

#设置当前时间
curTime = time.strftime("%Y-%m-%d %H%M", time.localtime())

#设置输出渠道——输出到控制台
hd_1 = logging.StreamHandler()

#设置输出渠道——输出到文件
hd_2 = RotatingFileHandler(f"{logs_dir}/API_autoTest_log_{curTime}.log", backupCount=20, encoding="utf-8")

#设置root logger，由于basicConfig()的参数是**kwargs，所以参数要以key=value的形式传入
logging.basicConfig(format=fmt, datefmt=datefmt, level=logging.INFO, handlers=[hd_1, hd_2])

#logging.info("hello")