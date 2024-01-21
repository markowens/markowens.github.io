import os
import shutil
import sys
import os.path
from os import path

src = "/home/mark/www/training/plsight"

for filename in os.listdir(src):
    if filename.endswith(".zip"):
        base = src + "/" + filename.split(".")[0]
        txt = base + ".txt"
        zip = base + ".zip"
        if path.exists(txt) and path.exists(zip):
            os.mkdir(base)
            shutil.move(txt, base + "/.")
            shutil.move(zip, base + "/.")



# src = "/home/mark/Documents"
# dst = "/home/mark/training/pls"

# for filename in os.listdir(src):
#     if filename.endswith(".txt"):
#         #print(f'file: {filename}')
#         with open(src + '/' + filename) as f:
#             line = f.readline()
#             #print(line)
#             if "Course Overview" in line:
#                 print(f'Moving {filename} to pls directory')
#                 shutil.move(src + '/' + filename, dst + '/' + filename)

# for filename in os.listdir(src):
#     if "Pluralsight" in filename:
#         shutil.move(src + '/' + filename, dst + '/' + filename)