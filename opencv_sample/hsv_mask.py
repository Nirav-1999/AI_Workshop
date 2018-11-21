# -*- coding: utf-8 -*-
import cv2
import numpy as np

import color_picker as cp

def create_hsv_mask(min_value,max_value):
    cap=cv2.VideoCapture(0)
    while(1):
        ret_val, frame=cap.read()
        if ret_val==True:
            hsv_img=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
            lower_value=np.array(min_value)
            upper_value=np.array(max_value)
            mask=cv2.inRange(hsv_img,lower_value,upper_value)
            and_image=cv2.bitwise_and(frame,frame,mask=mask )
            cv2.imshow("Mask Image",and_image)
            if cv2.waitKey(1)==27:
                break
    cv2.destroyAllWindows()
    cap.release()
"""After calling cv2.inRange, a binary mask is returned, where white pixels 
(255) represent pixels that fall into the upper and lower limit range and
 black pixels (0) do not.
To create the output image, we apply our mask on Line 16. This line simply 
makes a call to cv2.bitwise_and which bitwise ands the pixels, 
showing only pixels in the image that have a corresponding white (255) value 
in the mask.
cv2.Canny creates canny image
"""
            
if __name__ == '__main__':
    min_value,max_value=cp.get_color_range()
    create_hsv_mask(min_value,max_value)
