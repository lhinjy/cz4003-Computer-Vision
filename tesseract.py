# only need to change one line: the file name
from PIL import Image
import cv2
import numpy as np
import matplotlib.pyplot as plt
import pytesseract


# image_name = "sample02"

file_path = "C:/Users/User/Desktop/CV/sample02"

# Tesseract requirememt
pytesseract.pytesseract.tesseract_cmd = r'C:/Users/User/AppData/Local/Tesseract-OCR/tesseract.exe'


# def plot_histogram():
#   img = cv2.imread(image_name+".png" , 0)
#   # hist=cv2.calcHist([img],[0],None,[256],[0,256])
#   plt.hist(img.ravel(),256,[0,256]);
#   plt.savefig("histogram.png")
  

# return text from OCR 
def OCR(filename):
  text = pytesseract.image_to_string(Image.open(filename))
  print(text)
  return text


def base(name):
  text = OCR(name)
  f = open('text.txt','a')
  f.write("%s text: "%(name) + str(text) + '\n\n\n')
  f.close()


def main(image_name):
  base(image_name+".png")


if __name__ == '__main__':
  #plot_histogram()
  main(image_name)



