import os
import PyPDF2

path = "sample.pdf"
pdf = PyPDF2.PdfFileReader(path, 'rb')
## pdf2 = PyPDF2.PdfFileReader('Dear_America.pdf', 'rb')
writer = PyPDF2.PdfFileWriter()

writer.addPage(pdf.getPage(1))

## pages = [2,4,5,9]

## for x in pages:
    ## writer.addPage(pdf2.getPage(x))

output = open("extracted.pdf", 'wb')
writer.write(output)

print("Done")
output.close()

## commented out way to extract select pages from two pdfs, or use a list 
## to get multiple select pages from one PDF. 