import cv2 
import numpy as np
from PIL import ImageGrab
from PIL import Image
import pytesseract
import clipboard
import winsound
import time
src=''
clipboard.copy('')
def metinOku(image):
    #gri tona çevir
    image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    #Resmi temizle
    kernel=np.ones((1,1),np.uint8)
    image=cv2.erode(image,kernel,iterations=1)
    image=cv2.dilate(image,kernel,iterations=1)

    #gri 2 siyah
    image=cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,31,2)

    #OCR
    sonuc1=pytesseract.image_to_string(image,lang='tur')
    sonuc1 = sonuc1[:-1]
    lines = sonuc1.split("\n")
    sonuc1 = [line for line in lines if line.strip() != ""]
    sonuc=""
    for line in sonuc1:
        sonuc += line + "\n"
    if (src!=sonuc)and sonuc!=None:
        clipboard.copy(sonuc)
        winsound.Beep(550, 100)
        print(sonuc)
    return sonuc

while (True):
    try:
        img = ImageGrab.grabclipboard()
        if ( img != None):
            img = np.array(img)
            img = img[:, :, ::-1].copy()
            *_,img = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)
            src=(metinOku(img))
        time.sleep(0.25)
    except:
        continue