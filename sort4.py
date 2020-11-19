#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time:2018/8/24 9:37
# @Author: wardseptember
# @File: CountHighFrequencyWords.py
import re
import sort3

excludes = ['the', 'of', 'to', 'and', 'in', 'a', 'is', 'were', 'was', 'you',
            'I', 'he', 'his', 'there', 'those', 'she', 'her', 'their',
            'that', '[a]', '[b]', '[c]', '[d]', 'them', 'or','for','as',
            'are','on','it','be','with','by','have','from','not','they',
            'more','but','an','at','we','has','can','this','your','which','will',
            'one','should','points)','________','________.','all','than','what',
            'people','if','been','its','new','our','would','part','may','some','i',
            'who','answer','when','most','so','no','into','do','only',
            'each','other','following','had','such','much','out','--','up','these',
            'even','how','use','because','(10','time','(15','[d].',
            '-','it.','[b],','[a],','however,','1','1.','2','2.','3','3.','4','4.',
            '5','5.','6','6.','7','7.','8','8.','9','9.','10','10.','11','11.',
            '12','12.','13','13.','14','14.','15','15.','16','16.','17','17.',
            '18','18.','19','19.','20','20.','.','—',',','a,','(','d','d.'
            ]
#自行过滤简单词，太多了不写了



def getTxt(txt):
    txt=txt.lower()
    for ch in '!"@#$%^&*()+,-./:;<=>?@[]_`~{|}': #替换特殊字符
        txt.replace(ch, ' ')
    return txt
#1.获取单词

path = u'D:\\学习资料\\2010-2020年考研英语二真题\\2019年英语二真题.pdf'
pdf_utils = sort3.PDFUtils()
# print (pdf_utils.pdf2txt(path))
txt=pdf_utils.pdf2txt(path)
EngTxt = getTxt(txt)

#2.切割为列表格式
txtArr = EngTxt.split()

#3.遍历统计
counts = {}
for word in txtArr:
    flag=True
    for word1 in excludes:
        if word==word1:
            flag=False
        else:
            continue
    if flag is True:
        counts[word] = counts.get(word, 0) + 1
    else:
        continue

#4.转换格式，方便打印，将字典转换为列表
countsList = list(counts.items())
countsList.sort(key=lambda x:x[1], reverse=True)#按次数从大到小排序

#5.打印输出
for word,count in countsList:
    with open('output_2019.txt','a+',encoding='utf-8') as f:
        str1=word+':'+str(count)
        f.writelines(str1+'\n')
        f.close()
    #print('{0:<10}{1:>5}'.format(word,count))
