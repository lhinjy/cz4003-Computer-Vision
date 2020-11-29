# input -> otsu -> output
# change one line: file name
import math
import numpy as np
import cv2
from PIL import Image
import matplotlib.pyplot as plt

# change here
image_name="sample02"

image = cv2.imread('%s.png'%(image_name),0)
save_file_name="%s_otsu.png"%(image_name)

file_path = "/Users/User/Desktop/CV/sample02"

width = 0
height = 0
u1_l = []
w1_l = []
v1_l = []

u2_l = []
w2_l = []
v2_l = []

c_index = []
aw_l = []
ab_l = []


histogram = cv2.calcHist([image],[0],None,[256],[0,256])

# alot of NaN values
np.seterr(divide='ignore', invalid='ignore')

# N = n1 + n2 + ... + nl 
# Total number of pixels
def N_pixels():
  N = 0
  for i in range(len(histogram)):
    if (histogram[i]>0):
      N = N + histogram[i]
  
  return N
  

# probability at gray level i
def prob(i):
  N = N_pixels()
  p = histogram[i]/float(N)

  return p

# weight of class 1 : range of 0 to t 
# weight of class 2: range of t to L-1
# gray level possibility distributions 
def weight(a,b):
  w = 0
  for j in range(a,b):
    p = prob(j)
    w = w +p

  return w

# mean of class 1: range of a to b
def mean(a,b):
  w = weight(a,b)
  m = 0
  u = 0
  for j in range(a,b):
    p = prob(j)
    m = m + p
  
  u = m/float(w)

  return u


# gray level probability distributions
def gray_lvl(w1,u1,w2,u2):
  ut = w1 * u1 + w2 * u2

  return ut

# total mean of gray levels
def gray_lvl(w1,u1,w2,u2):
  ut = w1 * u1 + w2 * u2

  return ut

# class variance
def class_var(a,b):
  v = 0
  a = 0
  u = mean(a,b)
  w = weight(a,b)
  for j in range(a,b):
    p = prob(j)
    v = v + ((j - u)**2) * p
  
  a = v/float(w)
  
  return a


# within-class variance
def within_class_var(k,m):
  aw = 0
  for j in range(k,m):
    w = weight(j,m)
    a = class_var(j,m)
    aw = aw + w*a

  return aw

# between class var
def betw_class_var(w1,u1,w2,u2):
  ut = gray_lvl(w1,u1,w2,u2)
  if (math.isnan(ut)):
    ut = 0
  print(ut)
  ab = (w1 * (u1 - ut)**2) + (w2(u2-ut)**2)
  print(ab)
  return ab



def threshold(histogram):
  N = N_pixels()
  # go through every single possible threshold, 1 - 254

  for i in range(1,len(histogram)):
    v1 = class_var(0,i)
    w1 = weight(0,i)
    u1 = mean(0,i)

    v2 = class_var(i,len(histogram))
    w2 = weight(i,len(histogram)) 
    u2 = mean(i,len(histogram))

    # variance within class
    aw = w1 * v1 + w2 * v2
    
    # variance between class
    ab = w1 * w2 * (u1 - w2)**2
   
    if (not (math.isnan(v1) or math.isnan(u1) or math.isnan(w1) or math.isnan(ab) or math.isnan(aw))):
      c_index.append(i)

      v1_l.append(v1)
      u1_l.append(u1)
      w1_l.append(w1)

      v2_l.append(v2)
      u2_l.append(u2)
      w2_l.append(w2)

      ab_l.append(ab)
      aw_l.append(ab)
      print(ab)

  return ab_l, aw_l


# Maximize between class variance or minimize within-class variance
def optimal_threshold():
  ab_list, aw_list = threshold(histogram)
  print("1")
  #maximize between class varance
  ab_list.sort()
  optimal_ab = ab_list[-1]
  print("between")
  print(optimal_ab)

  # minimize within class 
  aw_list.sort()
  optimal_aw = aw_list[0]
  print("within")
  print(optimal_aw)

  f = open("otsu_data.txt",'w') 
  f.write("index = " + str(c_index))
  f.write("v1 = " + str(v1_l) + '\n\n')
  f.write("u1 = " + str(u1_l) + '\n\n')
  f.write("w1 = " + str(w1_l) + '\n\n')
  f.write("v2 = " + str(v2_l) + '\n\n')
  f.write("u2 = " + str(u2_l) + '\n\n')
  f.write("w2 = " + str(w2_l) + '\n\n')
  f.write("ab = " + str(ab_l) + '\n\n')
  f.write("aw = " + str(aw_l) + '\n\n')
  f.write("max between class variance " + str(optimal_ab))
  f.write("min within class variance " + str(optimal_aw))
  f.close()

  return math.floor(optimal_ab*1000)

def reconstruct_otsu():
  threshold = optimal_threshold()

  # this process takes some time, so printing it out can show that its progressing
  print(threshold)

  output_otsu = np.zeros((len(image), len(image[0])))
  for i in range(len(image)):
    for j in range(len(image[0])):
      if (image[i][j] > threshold):
        output_otsu[i][j] = 255
      else:
        output_otsu[i][j] = 0

  return output_otsu  

def main():
  output = reconstruct_otsu()
  cv2.imwrite(save_file_name, output)  

   
if __name__ == '__main__':
  main()

  







