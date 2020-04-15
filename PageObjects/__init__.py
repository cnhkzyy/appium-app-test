import os
import re
import shutil

dir_path = "../"

#清缓存
def clean_cache(dir_path):
    if os.path.isdir(dir_path):
        for dir in os.listdir(dir_path):
            if os.path.isdir(os.path.join(dir_path, dir)) and re.search(r"cache", dir) != None:
                shutil.rmtree(os.path.join(dir_path, dir))
            elif os.path.isdir(os.path.join(dir_path, dir)) and re.search(r"cache", dir) == None:
                clean_cache(os.path.join(dir_path, dir))

clean_cache(dir_path)
