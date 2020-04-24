import os

cur_dir = os.path.split(os.path.abspath(__file__))[0]

root_dir = cur_dir.rsplit("\\", maxsplit=1)[0]

caps_dir = cur_dir.replace("common", "caps")

images_dir = cur_dir.replace("common", "images")

logs_dir = cur_dir.replace("common", "logs")

html_reports_dir = cur_dir.replace("common", "html_reports")

allure_reports_dir = cur_dir.replace("common", "allure_reports")

