import os
import PyPDF2

## Finds PDF, opens pdf, and creates a PDF File Reader and Writer object, since we are creating a new PDF
path = "sample.pdf"
f = open(path, 'rb')
pdf = PyPDF2.PdfFileReader(f)
writer = PyPDF2.PdfFileWriter()

## example loop to rotate every even page, use getPage(pagenum) and use .rotateClockwise(angle) or .rotateCounterClockwise(angle)
for pagenum in range(pdf.numPages):
    page = pdf.getPage(pagenum)
    if pagenum % 2:
        page.rotateClockwise(180)
        ## page.rotateCounterClockwise(angle) can work too
    writer.addPage(page)

## opens a new pdf, with name newfile
output = open("newfile.pdf", 'wb')

## uses the writer object to create output file
writer.write(output)

## closes the source pdf and the newly written pdf
output.close()
f.close()
