
import pyttsx3
import PyPDF2

book=open('C:/Users/91930/Desktop/SEPM_anuradha.pdf','rb')
pdfReader = PyPDF2.PdfReader(book)
pages = len(pdfReader.pages)
speaker = pyttsx3.init()

for num in range(0, pages):
    page = pdfReader.pages[num] 
    txt = page.extract_text()
    speaker.say(txt)
    speaker.runAndWait()
    
