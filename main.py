
import os
import shutil
import time
import platform

start_time = time.time()

pictures_path = "C:\\Users\\BSNR\\Documents\\Loan Documents"
dest = "C:\\Users\\BSNR\\Documents\\Projects\\dest"

if platform.system()=="Windows" :
    path_joiner = "\\"
else:
    path_joiner="/"

def traverse(path,destination):
    
    if os.path.isfile(path):
        src = path
        base_name = os.path.basename(src)
        get_extension = base_name.split('.')[-1]
        dest_ext = destination+path_joiner+get_extension
        if not os.path.isdir(dest_ext):
            os.makedirs(dest_ext)
        dest_withfilename = dest_ext+path_joiner+base_name
        shutil.copyfile(src,dest_withfilename)

    else: 
        content  = os.listdir(path)
        for each_path in content:
            # ignoring hidden files
            if each_path[0]=='.':
                continue
            path_inprogress = path+path_joiner+each_path
            # print("paths/filenames: ",each_path)
            traverse(path_inprogress,destination)


traverse(pictures_path,dest)

end_time = time.time()

print("running time: ",end_time-start_time)