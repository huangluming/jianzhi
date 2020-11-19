from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage, PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams

import io

class PDFUtils():

    def __init__(self):
        pass

    def pdf2txt(self, path):
        output = io.StringIO()
        with open(path, 'rb') as f:
            praser = PDFParser(f)

            doc = PDFDocument(praser)

            if not doc.is_extractable:
                raise PDFTextExtractionNotAllowed

            pdfrm = PDFResourceManager()

            laparams = LAParams()

            device = PDFPageAggregator(pdfrm, laparams=laparams)

            interpreter = PDFPageInterpreter(pdfrm, device)

            for page in PDFPage.create_pages(doc):
                interpreter.process_page(page)
                layout = device.get_result()
                for x in layout:
                    if hasattr(x, "get_text"):
                        content = x.get_text()
                        output.write(content)

        content = output.getvalue()
        output.close()
        return content


if __name__ == '__main__':
    path = u'D:\\学习资料\\2010-2020年考研英语二真题\\2020年英语二真题.pdf'
    pdf_utils = PDFUtils()
    print (pdf_utils.pdf2txt(path))