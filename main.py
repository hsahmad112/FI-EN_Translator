from PIL import ImageGrab, Image
#https://pillow.readthedocs.io/en/stable/handbook/tutorial.html
from pytesseract import pytesseract
#https://pypi.org/project/pytesseract/
from langdetect import detect
#https://pypi.org/project/langdetect/
from deep_translator import GoogleTranslator
#https://pypi.org/project/deep-translator/

#Define paths to tess.exe
path_to_tesseract = r"C:\Users\...\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
#Grab image
clipboard = ImageGrab.grabclipboard()

#extract text - set states for language detection below
pytesseract.tesseract_cmd = path_to_tesseract
text = pytesseract.image_to_string(clipboard, lang='fin')

#line below prints out the text extracted
print("Original Text: " + text[:-1])

translated_text = GoogleTranslator(source='auto', target='en').translate(text)
print("Translated text: " + translated_text)

input("Press enter to exit;")

