import os
import PyPDF2

## Finds PDF, opens pdf, and creates a PDF File Reader object
path = "sample.pdf"
f = open(path, 'rb')
pdf = PyPDF2.PdfFileReader(f)

## Get document information, calls getDocumentInfo, and prints author/title
information = pdf.getDocumentInfo()
print(information.author)
print(information.title)

## returns number of pages of PDF
print (pdf.getNumPages())

## closes the source PDF
f.close()
