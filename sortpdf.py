import PyPDF2
import re,string
frequency={}
# pdfFileObj=open('F:\\ziqianbeifen\\zhuomian\\英文电子书\\批判性思维\\Asking the Right Questions.pdf','rb')

# pdfFileObj=open('D:\\学习资料\\2010-2020年考研英语二真题\\2020年英语二真题.pdf','rb')
# pdfReader=PyPDF2.PdfFileReader(pdfFileObj)
pdfReader=PyPDF2.PdfFileReader('D:\\学习资料\\2010-2020年考研英语二真题\\2020年英语二真题.pdf')

print(pdfReader.getNumPages())
# for pageNum in range(1,15):
#     pageObj=pdfReader.getPage(pageNum)

pageObj=pdfReader.getPage(3)
text_string=pageObj.extractText().lower()
print(len(text_string) )

print(text_string)
# match_pattern=re.findall(r'\b[a-z]{6,15}\b',text_string)

# for word in match_pattern:
#     count=frequency.get(word,0)
#     frequency[word]=count+1

# l=[]
# for a,b in frequency.items():
#     l.append((b,a))
# l.sort(reverse=True)

# for words,frequency[words] in l:
#     print(words,frequency[words])


    