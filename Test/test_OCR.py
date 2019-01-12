from Utility.OCRValidation import verify_OCR

text= verify_OCR('http://jeroen.github.io/images/testocr.png')
print(text)

if text.find('fox'):
    print('Text found...')