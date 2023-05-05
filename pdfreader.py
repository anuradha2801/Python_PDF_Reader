#adding required libraries
import pyttsx3
import PyPDF2

#reading any pdf file and storing the total number of pages in it.
book=open('C:/Users/91930/Desktop/SEPM_anuradha.pdf','rb')
pdfReader = PyPDF2.PdfReader(book)
pages = len(pdfReader.pages)

#initializing the speaker
speaker = pyttsx3.init()

#loop for reading all the pages of the pdf with indexing zero
for num in range(0, pages):
    page = pdfReader.pages[num] 
    txt = page.extract_text()
    speaker.say(txt)
    speaker.runAndWait()
    
