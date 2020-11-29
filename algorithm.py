import numpy as np
import cv2 
from scipy import ndimage
from PIL import Image, ImageEnhance

from matplotlib import pyplot as plt
import os
from tesseract import main

file_path = "C:/Users/User/Desktop/CV/sample02"

# change here
image_name="sample02"

img = cv2.imread('%s.png'%(image_name),0)

# Canny edge
def canny(lower,higher):
  edges = cv2.Canny(img,lower,higher)
  cv2.imwrite('%s/canny_%s_%s_%s.png'%(file_path,image_name,lower,higher),edges)
  print("saved")

# Invert color
def invertcol():
  imgi = (255-img)
  cv2.imwrite('%s/inverted_%s.png'%(file_path,image_name),imgi)
  print("saved")
  
# Bilateral filtering
def bi_filter(d,sc,ss):
  bi_f = cv2.bilateralFilter(img,d,sc,ss)
  cv2.imwrite('%s/bilateral_%s_%s_%s_%s.png'%(file_path, image_name,d,sc,ss),bi_f)
  print("saved")

# median blurring
def medi_filter(kernel):
  median = cv2.medianBlur(img,kernel)
  cv2.imwrite('%s/median_%s_%s.png'%(file_path,image_name,kernel),median)
  print("saved")

# Increase contrast
def increase_contrast(factor):
  imag = Image.open('sample02.png')
  enhancer = ImageEnhance.Contrast(imag)
  imoutput = enhancer.enhance(factor)
  imoutput.save('%s/contrast_%s_%s.png'%(file_path,image_name,factor))
  print("saved")

# morphological transformation
def morph_closing(value):
  kernel = np.ones((value,value),np.uint8)
  closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE,kernel)
  cv2.imwrite('%s/morph_closing_%s_%s.png'%(file_path,image_name,value),closing)
  print("saved")

  
# morphological transformation
def morph_erosion(value):
  kernel = np.ones((value,value), np.uint8)
  erosion = cv2.erode(img,kernel,iterations=1)
  cv2.imwrite('%s/morph_erosion_%s_%s.png'%(file_path,image_name,value),erosion)
  print("saved")

# morphological transformation
def morph_opening(value):
  kernel = np.ones((value,value), np.uint8)
  opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
  cv2.imwrite('%s/morph_opening_%s_%s.png'%(file_path,image_name,value),opening)
  print("saved")

# morphological transformation
def morph_dilation(value):
  kernel = np.ones((value,value), np.uint8)
  dilation = cv2.dilate(img,kernel, iterations=1)
  cv2.imwrite('%s/morph_dilation_%s_%s.png'%(file_path,image_name,value),dilation)
  print("saved")

# Adaptive Mean thresholding
def adapt_mean():
  image = cv2.medianBlur(img,1)
  th2 = cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,13,5)
  cv2.imwrite('%s/adaptm_%s.png'%(file_path,image_name),th2)
  print("saved")

# Adaptive Gaussian Thresholding
def adapt_gauss():
  image = cv2.medianBlur(img,1)
  th3 = cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,13,4)
  cv2.imwrite('%s/adaptgauss_%s.png'%(file_path,image_name),th3)
  print("saved")


def histo_equal():
  dst = cv2.equalizeHist(img)
  cv2.imwrite('%s/histo_e_%s.png'%(file_path,image_name),dst)
  print("saved")


def get_text():
  #bi_filter(17,10,15)
  canny(50,70)
  #medi_filter(3)
  #increase_contrast(1.2)
  #morph_opening(10)
  #morph_erosion(2)
  #morph_closing(2)
  #morph_dilation(2)
  #invertcol()
  #adapt_mean()
  #adapt_gauss()
  #histo_equal()

  main(image_name)
  


if __name__ == "__main__":
  get_text()