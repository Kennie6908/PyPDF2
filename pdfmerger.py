import os
import PyPDF2

## list of pdf names, can be more than 2
paths = ['sample.pdf', 'dummy.pdf']

## create pdfwriter object
writer = PyPDF2.PdfFileWriter()

## create loop to go through paths list, get all pages and add to writer object
for x in paths:
    pdf = PyPDF2.PdfFileReader(x, 'rb')
    for page in range(pdf.numPages):
        writer.addPage(pdf.getPage(page))

## create output pdf and write to it
output = open('merged.pdf', 'wb')
writer.write(output)

print ("Done")

output.close()