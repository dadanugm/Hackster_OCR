import pyttsx3
import os
import time
import pytesseract
import cv2
import os
from PIL import Image
from gtts import gTTS
from playsound import playsound
from kv260 import BaseOverlay
from pynq.lib.pmod.pmod_io import Pmod_IO

#pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
#image_path = 'text_ind.jpg'
image_path = 'test_cam.jpg'
threshold = True
blur = True
text = ""

#base = BaseOverlay('base.bit')
#led=Pmod_IO(base.PMODA,index=0,direction='out')
#led.write(0)

######## TEST CAMERA #########
def test_cam():
    cam = cv2.VideoCapture(0)
    cam.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 1024)
    #cam.open(0, cv2.CAP_ANY)
    ret, img = cam.read()
    image = cv2.rotate(img, cv2.cv2.ROTATE_90_CLOCKWISE)
    cv2.imwrite('test_cam.jpg', image)
    #time.sleep(5)

def test_tesseract():
    global text
    img = cv2.imread(image_path)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    if threshold == True:
        gray_img = cv2.threshold(gray_img, 0, 225, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    elif blur == True:
        gray_img = cv2.medianBlur(gray_img, 5)
    cv2.imwrite('grey_img.jpg', gray_img)
    filename = "{}.png".format(os.getpid())
    cv2.imwrite(filename, gray_img)

    text = pytesseract.image_to_string(Image.open(filename))
    os.remove(filename)
    print(text)
    print("done")

def test_gtts():
    global text
    tts = gTTS(text, lang='en')
    tts.save('text_gtts.mp3')
    #play sound
    playsound('text_gtts.mp3')
    print("done")

test_cam()
test_tesseract()
test_gtts()


