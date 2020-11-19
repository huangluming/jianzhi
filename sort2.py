import os

def file_name(file_dir):
    for root, _, files in os.walk(file_dir):
        return root,files

print(file_name('C:\\Users\\huanglm\\Desktop\\test')  )


def get_word_list(path):
    with open(path,'r',encoding='utf-8') as f:
        word_list=[]
        for line in f.readlines():
            line=line.strip('\n') #去掉换行符\n
            # word_list.popitem()
            word_list.append(line)

        return word_list

# get_word_list('C:\\Users\\huanglm\\Desktop\\list.txt')