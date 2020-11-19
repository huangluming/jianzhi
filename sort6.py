import jieba
import xlwt
# import nltk
import sort3
import csv
import codecs
import os

def data_write_csv(file_name, datas):#file_name为写入CSV文件的路径，datas为要写入数据列表
    file_csv = codecs.open(file_name,'w+','utf-8')#追加
    # writer = csv.writer(file_csv, delimiter='\t', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    writer = csv.writer(file_csv, dialect='excel')
    
    for data in datas:
        writer.writerow(data)
    print("保存文件成功，处理结束")

def getText(txt):
    txt = txt.lower()          #将文件中的单词全部变为小写
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
        txt = txt.replace(ch, " ")   #将文本中特殊字符替换为空格
    return txt

def get_word_list(path):
    with open(path,'r',encoding='utf-8') as f:
        word_list=[]
        for line in f.readlines():
            line=line.strip('\n') #去掉换行符\n
            word_list.append(line)
        return word_list



#以上代码用于文本格式的修改，避免文档中格式的种种问题，也可以读取docx等文件
excludes = {"they","their","your","this","that","from","with","which","about","should"}
#去除掉你不想要统计次数的单词



#去除特殊符号

def get_file_list(path):

    # path = u'D:\\学习资料\\2010-2020年考研英语二真题\\2019年英语二真题.pdf'
    pdf_utils = sort3.PDFUtils()
    # print (pdf_utils.pdf2txt(path))

    txt=''
    for file in file_name(path):
        file_path=path+"\\"+file
        print(file_path)
        txt_temp=pdf_utils.pdf2txt(file_path)
        txt=txt+txt_temp
        
    hamletTxt = getText(txt)
    #words  = hamletTxt.split() #按照空格，将文本分割
    #words  = nltk.word_tokenize(hamletTxt)
    words   = jieba.lcut(hamletTxt)
    
    #这里使用jieba库进行分词，也可以用上边的两者进行测试分词效果
    counts = {}
    for word in words:
        if len(word) < 7:
            continue
        elif word in excludes:
            continue
        else:
            rword = word
        counts[rword] = counts.get(rword, 0) + 1

    #去除单词长度在7个以下的，去除之前定义的，统计其他单词的数量
    items = list(counts.items())   #将字典转换为列表，以便操作
    # list2=(path,'NO')
    year='all'
    result=[]
    for item in items:
        if(item[0] in get_word_list('C:\\Users\\huanglm\\Desktop\\list.txt')):
            isInList="YES"
        else:
            isInList="NO"  
    
        list2=(year,isInList)
        item_temp=item+list2

        result.append(item_temp)

    # print(items)
    return result




def file_name(file_dir):
    for _, _, files in os.walk(file_dir):
        return files

# def get_all_eng(path):
#     items_all=[]
#     for file in file_name(path):
#         file_path=path+"\\"+file
#         print(file_path)
#         items= get_file_list(file_path,file)
#         items.sort(key=lambda x:x[1], reverse=True)  # 见下面函数讲解
#         # print(items)
#         items_all.append(items)
    
#     # items_all_result = list(items_all.items()) 
#     return items_all

path = u'C:\\Users\\huanglm\\Desktop\\test'

items= get_file_list(path)
items.sort(key=lambda x:x[1], reverse=True)  # 见下面函数讲解

# items_all= get_all_eng(path)
# print(items_all)
data_write_csv('word3.csv', items)
