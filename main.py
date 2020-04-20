import pytest, os
import time
from common.conf_dir import root_dir, logs_dir, html_reports_dir
from multiprocessing import Pool
from clean import *

device_infos = [{"platform_version": "5.1.1", "server_port": 4723, "device_port": 62001, "system_port": 8200},
                {"platform_version": "7.1.1", "server_port": 4725, "device_port": 62025, "system_port": 8201}]


cur_time = time.strftime("%Y-%m-%d_%H-%M-%S")

def run_parallel(device_infos):
    pytest.main([
        f"--cmdopt={device_infos}",
        #"--reruns=1",
        #"--reruns-delay=10",
        "-m", "fail",
        "--junitxml", f"{html_reports_dir}/autotest_report_{cur_time}.xml",
        "--html", f"{html_reports_dir}/autotest_report_{cur_time}.html",
        "--css", f"{html_reports_dir}/assets/style.css",
        "--self-contained-html"])



if __name__ == "__main__":
    with Pool(2) as pool:
        pool.map(run_parallel, device_infos)
        pool.close()
        pool.join()