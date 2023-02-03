import pyttsx3
import PyPDF3

book = open('Data-com.pdf','rb')
pdfReader = PyPDF3.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)


mamu = pyttsx3.init()
for num in range(0, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    mamu.say(text)
    mamu.runAndWait()
