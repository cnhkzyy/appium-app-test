import pytest
import time
from multiprocessing import Pool
from common.clean import *
#import socket


device_infos = [{"docker_name": "appium_2", "platform_version": "7.1.2", "server_port": 4725}]
cur_time = time.strftime("%Y-%m-%d_%H-%M-%S")


def run_parallel(device_info):
    pytest.main([
        "-d",
        #"--dist", "load",
        #"--tx", "ssh=root@192.168.0.126",
        #"--tx", "ssh=root@192.168.0.136",
        "--tx", "socket=192.168.0.126:8888",
        "--tx", "socket=192.168.0.136:8888",
        #"--tx", "ssh=root@192.168.0.126//python=/opt/Python-3.8.0/bin/python3.8//chdir=/opt/pyexecnetcache",
        #"--tx", "ssh=root@192.168.0.136//python=/opt/Python-3.8.0/bin/python3.8//chdir=/opt/pyexecnetcache",
        "--rsyncdir", "./",
        "APP_Xdist_AutoTest",
        #"APP_Xdist_AutoTest/test_cases",
        f"--cmdopt={device_info}",
        #"--reruns=1",
        #"--reruns-delay=10",
        #"-m", "login and fail",
        #"--junitxml", f"{html_reports_dir}/autotest_report_{cur_time}.xml",
        #"--html", f"{html_reports_dir}/autotest_report_{cur_time}.html",
        #"--css", f"{html_reports_dir}/assets/style.css",
        #"--self-contained-html",
        "--alluredir", allure_reports_dir
       ])


os.system(f"allure generate {allure_reports_dir} -o {allure_reports_dir}/html --clean")


if __name__ == "__main__":
    with Pool(1) as pool:
       pool.map(run_parallel, device_infos)
       pool.close()
       pool.join()
