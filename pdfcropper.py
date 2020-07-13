import os
import PyPDF2

## create path, reader, and writer object
path = "sample.pdf"
pdf = PyPDF2.PdfFileReader(path, 'rb')
writer = PyPDF2.PdfFileWriter()
page = pdf.getPage(0)

## gets coordinates in format (x,y), bottom left should be (0,0)
print(page.cropBox.getLowerLeft())
print(page.cropBox.getLowerRight())
print(page.cropBox.getUpperLeft())
print(page.cropBox.getUpperRight())

## create a box, coordinates format (x, y) 
page.mediaBox.lowerRight = (460, 450)
page.mediaBox.lowerLeft = (0, 450)
page.mediaBox.upperRight = (460, 792)
page.mediaBox.upperLeft = (0, 792)

## add the page with the mediabox to the writer
writer.addPage(page)

output = open("cropped.pdf", 'wb')
writer.write(output)
output.close()