import os
path = "/media/06FE26B4FE269C45_/Documents and Settings/Dday/Music/Zune"
group = os.listdir(path)
dirs = []
for item in group:
    if os.path.isdir(os.path.join(path, item)):
        dirs.append(item)
    
print ",".join(dirs)

