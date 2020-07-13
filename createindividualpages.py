import os
import PyPDF2

## creates path and reader object
path = "sample.pdf"
pdf = PyPDF2.PdfFileReader(path, 'rb')

## create loop to ouput each page individually, can replace pdf.numPages to get certain amount of pages
## or use list to get individual PDFs of select pages
for x in range (pdf.numPages):
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(pdf.getPage(x))
    
    ## use f string formatting to label x+1 in file name
    output = open (f'page_{x + 1}.pdf', 'wb')
    writer.write(output)
    output.close()
    
print("done")


