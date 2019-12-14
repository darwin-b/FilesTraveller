
import os
import shutil
import time

start_time = time.time()

pictures_path = "D:\\Darwin Required Backup\\Pictures"

dest = "C:\\Users\\BSNR\\Documents\\Projects\\FilesTraveller\\dest"

def traverse(path,destination):
    if os.path.isfile(path):
        src = path
        base_name = os.path.basename(src)
        get_extension = base_name.split('.')[-1]
        dest_ext = destination+"\\"+get_extension
        if not os.path.isdir(dest_ext):
            os.makedirs(dest_ext)
        dest_withfilename = dest_ext+"\\"+base_name
        shutil.copyfile(src,dest_withfilename)

    else: 
        content  = os.listdir(path)
        for each_path in content:
            path_inprogress = path+"\\"+each_path
            # print("paths/filenames: ",each_path)
            traverse(path_inprogress,destination)


traverse(pictures_path,dest)

end_time = time.time()

print("running time: ",end_time-start_time)