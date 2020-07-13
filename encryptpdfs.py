import os
import PyPDF2

## create path, reader, and writer objects
path = "sample.pdf"
pdf = PyPDF2.PdfFileReader(path, 'rb')
writer = PyPDF2.PdfFileWriter()

## loop to add all pages in PDF to writer object
for x in range(pdf.numPages):
    page = pdf.getPage(x)
    writer.addPage(page)

## encrypt method, set user password, owner password, and use 128 bit vs 40 bit encryption
writer.encrypt(user_pwd = 'password', owner_pwd = None, use_128bit = True)

output = open("encrypted.pdf", 'wb')
writer.write(output)

print ("Done")
output.close()