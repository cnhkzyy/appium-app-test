import pytest
import time
from common.conf_dir import test_reports_dir

cur_time = time.strftime("%Y-%m-%d_%H-%M-%S")
pytest.main([
        "--reruns=1",
        #"--reruns-delay=10",
        #"-m", "fail",
        "--junitxml", f"{test_reports_dir}/autotest_report_{cur_time}.xml",
        "--html", f"{test_reports_dir}/autotest_report_{cur_time}.html"]
)
