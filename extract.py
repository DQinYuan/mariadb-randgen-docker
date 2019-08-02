import os
import shutil

targetdir = "/home/dqyuan/language/MariaDB/exportyyzz/pair"

def move(srcroot, fp):
    shutil.copyfile(os.path.join(srcroot, fp), os.path.join(targetdir, fp))
    

for root,_,files in os.walk(r"./conf"):
    s = set()
    for f in files:
        if f.endswith("yy") or f.endswith("zz"):
            prefix = f[:-3]
            if prefix in s:
                move(root, "%s.yy" % prefix)
                move(root, "%s.zz" % prefix)
                s.remove(prefix)
            else:
                s.add(prefix)