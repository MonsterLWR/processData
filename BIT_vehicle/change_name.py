import os
path = 'JPEGImages'
filelist = os.listdir(path)
for file in filelist:
    olddir = os.path.join(path,file)
    if file.find('jpg') == -1:
       continue
    file = file[1:]
    newdir = os.path.join(path,file)
    os.rename(olddir,newdir)
