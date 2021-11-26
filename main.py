import pyttsx3
import os
from PIL import Image
import pytesseract
import cv2
import os

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
image_path = 'test/test.jpg'
threshold = True
blur = True
text = ""

def test_tesseract():
    global text
    img = cv2.imread(image_path)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    if threshold == True:
        gray_img = cv2.threshold(gray_img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    elif blur == True:
        gray_img = cv2.medianBlur(gray_img, 3)
    filename = "{}.png".format(os.getpid())
    cv2.imwrite(filename, gray_img)

    text = pytesseract.image_to_string(Image.open(filename))
    os.remove(filename)
    print(text)
    # show the output images
    #cv2.imshow("Image", img)
    #cv2.imshow("Output", gray_img)
    cv2.waitKey(0)

def test_pyttsx3():
    global text
    synthesizer = pyttsx3.init()
    voices = synthesizer.getProperty('voices')
    for voice in voices:
        print("Voice: %s" % voice.name)
        print(" - ID: %s" % voice.id)
        print(" - Languages: %s" % voice.languages)
        print(" - Gender: %s" % voice.gender)
        print(" - Age: %s" % voice.age)
        print("\n")

    synthesizer.setProperty('rate', 100)
    synthesizer.say(text)
    synthesizer.runAndWait()
    synthesizer.stop()

test_tesseract()
test_pyttsx3()