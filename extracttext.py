import os
import PyPDF2

## Finds PDF, opens pdf, and creates a PDF File Reader object
path = "sample.pdf"
f = open(path, 'rb')
pdf = PyPDF2.PdfFileReader(f)

## getPage number, in this case is page 0 
pages = pdf.getPage(0)
print (pages.extractText())

## closes the source PDF
f.close()
