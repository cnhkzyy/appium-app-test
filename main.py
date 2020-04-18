import pytest
import time
from common.conf_dir import html_reports_dir

cur_time = time.strftime("%Y-%m-%d_%H-%M-%S")
pytest.main([
        #"--reruns=1",
        #"--reruns-delay=10",
        "-m", "fail",
        "--junitxml", f"{html_reports_dir}/autotest_report_{cur_time}.xml",
        "--html", f"{html_reports_dir}/autotest_report_{cur_time}.html",
        "--css", f"{html_reports_dir}/assets/style.css",
        "--self-contained-html"]
)
