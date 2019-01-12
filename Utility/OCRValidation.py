from PIL import Image
from Utility.SilentDownloader import download_file
import pytesseract
def verify_OCR(url):
    download_file(url, 'ocr.png')

    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

    text_extracted = pytesseract.image_to_string(Image.open('../DownloadedFiles/TELE.png'))
    return text_extracted
