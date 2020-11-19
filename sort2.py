import os

def file_name(file_dir):
    for root, _, files in os.walk(file_dir):
        # print(root) #当前目录路径
        # print(dirs) #当前路径下所有子目录
        print(files) #当前路径下所有非目录子文件

file_name('D:\\学习资料\\2010-2020年考研英语二真题')       