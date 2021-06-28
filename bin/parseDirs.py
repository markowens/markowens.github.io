from glob import iglob
import os

rootdir = "."

# for subdir, dirs, files in os.walk(rootdir):
#   for dir in dirs:
#     if ".git" in dir or "./.git" in subdir:
#       continue
#     if ".ipynb_checkpoints" in dir or "./.ipynb_checkpoints" in subdir:
#       continue
#     if ".idea" in dir or "./.idea" in subdir:
#       continue            

#     print(f"{subdir} - {dir}")

  # for file in files:
    # print(f"{os.path.join(subdir, file)}")


print("/n=============================\n")    

# rootdir_glob = "./**/*"
# file_list = [f for f in iglob(rootdir_glob, recursive=True) if os.path.isfile(f)]
# for f in file_list:
#   print(f)
default_index = "/home/mark/www/ghweb/blank_index.html"
rootdir_glob = "./**/*"
dir_list = [f for f in iglob(rootdir_glob, recursive=True) if os.path.isdir(f)]
for f in dir_list:
  cmd = "cp " + default_index + " "  + f + "/index.html"
  print(cmd)
  os.system(cmd)
