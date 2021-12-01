import shutil
import glob
import os
import re

origin_dir = f'{os.environ["USERPROFILE"]}/Documents/Dev/hello'
copy_dir = f'{os.environ["USERPROFILE"]}/Documents/Dev/hello_copy'

p = re.compile(r".*\.(jpg|png)$")
dirs = glob.glob(origin_dir + "/*")
dirs = list(filter(lambda x: p.match(x), dirs))

for i, path in enumerate(dirs):
    _, ext = os.path.splitext(path)
    shutil.copyfile(path, copy_dir + f"/{i+1}{ext}")