import jieba
import xlwt
# import nltk
import sort3
import csv
import codecs
# path = 'C:Users/Admin/Desktop/1.txt'
# file = open(path, encoding='gb18030', errors='ignore')
# file2 = open("C:Users/Admin/Desktop/2.txt", 'w',encoding='utf-8')
# file2.write(file.read())
# file.close()
# file2.close()

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



#以上代码用于文本格式的修改，避免文档中格式的种种问题，也可以读取docx等文件
excludes = {"they","their","your","this","that","from","with","which","about","should"}
#去除掉你不想要统计次数的单词



#去除特殊符号

def get_file_list(path):

    # path = u'D:\\学习资料\\2010-2020年考研英语二真题\\2019年英语二真题.pdf'
    pdf_utils = sort3.PDFUtils()
    # print (pdf_utils.pdf2txt(path))
    txt=pdf_utils.pdf2txt(path)
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
    tup2=(path,'YES')
    for item in items:
        # item[2]=path
        item=item+tup2
        print(item)

    # print(items)
    return items


path = u'D:\\学习资料\\2010-2020年考研英语二真题\\2019年英语二真题.pdf'

items= get_file_list(path)
items.sort(key=lambda x:x[1], reverse=True)  # 见下面函数讲解

data_write_csv('2019.csv', items)
# file2 = open("C:Users/Admin/Desktop/test2.txt","w")
# for i in range(1000):
#     word, count = items[i]
#     #print ("{0:<10}{1:>5}{1:>5}".format(word, count,count))
#     # file2.write("{0:<20}\n".format(word))
#     print("{0:<20}{1:>20}".format(word, count))
# # file2.close()
# #将统计的信息打印并写入文件，这里写入时没有加入词频