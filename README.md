# PyPDF2

A bunch of PyPDF2 applications. Runs perfectly on Python 3.8

1. PDFMetadata returns title, author, and number of pages. 

2. Extracttext prints text on certain pages. This may or may not work, as PyPDF2's text extractor is not the best. 

3. Pagerotater rotates pages. 

4. Pdfcropper crops pages. 

5. Pdfmerger combines two pdfs. 

6. Extractpages takes certain pages and creates one PDF with only those pages.  

7. Encryptpdfs allows a 128-bit encryption password to be set. 

8. Createindividualpages takes certain pages and makes them each an individual PDF, titled with its page number. 

Sample.pdf is used for most of these, but dummy.pdf is used once or twice. Make sure to change the names of the PDFs in the file to whatever you're working with. 

I did not create PyPDF2, just as a disclaimer. Please see mstamy's work at https://mstamy2.github.io/PyPDF2/ . 
