import os

cur_dir = os.path.split(os.path.abspath(__file__))[0]

root_dir = cur_dir.rsplit("\\", maxsplit=1)[0]

caps_dir = cur_dir.replace("common", "caps")

images_dir = cur_dir.replace("common", "images")

logs_dir = cur_dir.replace("common", "logs")

test_reports_dir = cur_dir.replace("common", "test_reports")
