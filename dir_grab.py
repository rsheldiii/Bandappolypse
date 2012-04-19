import os
import platform
import pwd
def get_username():
  return pwd.getpwuid(os.getuid())[0]
def get_system():
  return platform.system()
system = get_system()
user = get_username()
path = ""
path2 = ""
if system == "Darwin":
  path = "/Users/" + str(user) + "/Music/iTunes/iTunes Music"
elif system == "Windows":
  path = "/Users/" + str(user) + "/Music/iTunes/iTunes Media/Music"
  path2 = "Users/" + str(user) + "/Music/Zune"
if os.path.isdir(path):
  group = os.listdir(path)
if path2:
  if os.path.isdir(path2):
    for artist in os.listdir(path2):
      group.append(artist)
dirs = []
for item in group:
    if os.path.isdir(os.path.join(path, item)):
        dirs.append(item)
new_dirs = [artist.replace(",","%2C") for artist in dirs]
dirs = new_dirs    
print ",".join(dirs)

