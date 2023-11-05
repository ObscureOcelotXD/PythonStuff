
import pyttsx3,PyPDF2,re

#to get your pdf read all you have to do is put the file in the same folder as this main.py file and then add the name of the file to the bookname variable
bookName = "The_Art_Of_War"
pdfreader = PyPDF2.PdfReader(open(bookName + '.pdf','rb'))
speaker = pyttsx3.init()
clean_text = ""

for page_num in range(len(pdfreader.pages)):
    text = pdfreader.pages[page_num].extract_text()

    textCleanedOne = text.strip().replace('\n',' ')
    textCleanedTwo = re.sub(r"\/[G]\d{2}","",textCleanedOne)
    textCleanedThree = re.sub(r"\/[G]\d{1}\w{1}","",textCleanedTwo)
    textCleanedFour = re.sub(r"\/[G]\w{1}\d{1}","",textCleanedThree)
    clean_text += textCleanedFour
    print(clean_text)

speaker.save_to_file(clean_text,bookName + '.mp3')
speaker.runAndWait()

speaker.stop()
