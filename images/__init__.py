import os, re

#数据清理
files = os.listdir("./")
for file in files:
    if re.search(r"png", file):
        os.remove(file)