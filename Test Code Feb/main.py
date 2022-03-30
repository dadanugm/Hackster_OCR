import pyttsx3
import os
import time
import pytesseract
import cv2
from IPython.display import Audio
from threading import Thread
from multiprocessing import Process
from PIL import Image
from gtts import gTTS
from playsound import playsound

#image_path = 'text_ind.jpg'
image_path = 'test_cam.jpg'
threshold = True
blur = True
text = ""
start = False
play = False

######## get image from camera #########
def get_image():
    print("get image")
    cam = cv2.VideoCapture(0)
    cam.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 1024)
    ret, img = cam.read()
    image = cv2.rotate(img, cv2.cv2.ROTATE_90_CLOCKWISE)
    cv2.imwrite('test_cam.jpg', image)
    print("get image done")

########## Convert image to text ##############
def get_text():
    global text
    print("convert image to text")
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
    print("convert image to text done")

#########  TEXT to Speech ###############
def text_to_sound():
    global text
    print("convert text to MP3")
    tts = gTTS(text, lang='id')
    tts.save('text_gtts.mp3')
    print("convert text to MP3 done")


if __name__ == "__main__":
    # multitrhreading
    get_image()
    get_text()
    text_to_sound()
    playsound('/home/ubuntu/Documents/Test_playsound.mp3')
    

