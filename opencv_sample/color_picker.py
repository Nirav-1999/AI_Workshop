# -*- coding: utf-8 -*-
import cv2


colors=[]

def on_click(event,x,y,flags,frame):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        colors.append(frame[y,x].tolist()) #tolist creates a list
def get_color_range():
    cap=cv2.VideoCapture(0)
    while(len(colors)<10):
        ret_val, frame=cap.read()
        if ret_val==True:
            hsv_img=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
            cv2.imshow("HSV_COLOR_PICKER",hsv_img)
            cv2.setMouseCallback("HSV_COLOR_PICKER",on_click,hsv_img)
#Set mouse callback gives us the coordinates (x,y) for every mouse event
            if cv2.waitKey(1)==27:
                break

    cv2.destroyAllWindows()
    cap.release()
    min_value=[]
    max_value=[]
    for i in range(0,3):
        min_value.append(min(x[i] for x in colors))
        max_value.append(max(x[i] for x in colors))
    #min and max values are taken from each column of the colors list
    return min_value, max_value

if __name__== '__main__': #same as void main
    min_value,max_value = get_color_range() 