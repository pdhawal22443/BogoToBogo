import os
import pdb

#1st method is to get list of files and directories from given directory

def file_list1(dir):
    basedir = dir
    subdir_list = []
    for item in os.listdir(dir):
        fullpath = os.path.join(basedir,item)
        if os.path.isdir(fullpath):
            subdir_list.append(fullpath)
        else:
            print(fullpath)

    for d in subdir_list:
        file_list1(d)

file_list1('D:\D1')

#2nd way
#using os.walk

def file_list(dir):
    for root,directory,file in os.walk(dir):
        for f in file:
            print(os.path.join(root,f))
print("=============================================")
file_list('D:\D1')

