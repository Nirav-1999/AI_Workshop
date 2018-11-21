# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 15:29:56 2018

@author: PRAMOD
"""
import cv2
image=cv2.imread("standard_test_images/Lena_color_512.tif",) #reads the image
cv2.imshow("Lena",image)#Display the image
cv2.waitKey(0)#Time for which the image appears
cv2.destroyAllWindows()#Close all the windows

rgb_img=cv2.imread("standard_test_images/Lena_color_512.tif",)
gray=cv2.cvtColor(rgb_img,cv2.COLOR_BGR2GRAY)#cvtColor is used to change the colour
cv2.imshow("Lena",gray)
cv2.waitKey()
cv2.destroyAllWindows()

hsv_img=cv2.cvtColor(rgb_img,cv2.COLOR_BGR2HSV)
cv2.imshow("Lena",hsv_img)
cv2.waitKey()
cv2.destroyAllWindows()

rect_img=cv2.rectangle(rgb_img,(50,10),(450,450),(250,0,0),10)#Creating rectangle
cv2.imshow("Lena",rect_img)
cv2.waitKey()
cv2.destroyAllWindows()

text_img=cv2.putText(rgb_img,"Lena",(100,100),cv2.FONT_ITALIC,1.5,(0,0,0),3)#Enters text in the image
cv2.imshow("Lena",text_img)
cv2.waitKey()
cv2.destroyAllWindows()

bk_img=cv2.imread("standard_test_images/bookpage.jpg",0)
ret_val, threshold=cv2.threshold(bk_img,9,150,cv2.THRESH_BINARY)
"""
ret_val returns 0 or 1 corresponding to the points on the image
and threshold keeps the rgb code(specified inside the function) in the image 
and removes all the other rgb valued points
"""
cv2.imshow("Thresholded image",threshold)
cv2.waitKey()
cv2.destroyAllWindows()

bk_img=cv2.imread("standard_test_images/bookpage.jpg",0)
thresh=cv2.adaptiveThreshold(bk_img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                      cv2.THRESH_BINARY,115,2)
"""adaptive threshold adjusts the threshold values according to the surrounding
where 255 is the max value of rgb, 115 is the frame size and 1 is the random value 
for standard deviation"""
cv2.imshow("Thresholded image",thresh)
cv2.waitKey()
cv2.destroyAllWindows()

cv2.adaptiveThreshold()
