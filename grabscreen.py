# Done by Frannecklp

#CODE TO CAPTURE THE SCREEN
import cv2
import time
import math
import numpy as np
import win32gui, win32ui, win32con, win32api


def grab_screen(region=(160,305,800,450)):

    hwin = win32gui.GetDesktopWindow()

    if(region):
        left,top,x2,y2 = region
        width = x2 - left + 1
        height = y2 - top + 1
    else:
        width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
        height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
        left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
        top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)

    hwindc = win32gui.GetWindowDC(hwin)
    srcdc = win32ui.CreateDCFromHandle(hwindc)
    memdc = srcdc.CreateCompatibleDC()
    bmp = win32ui.CreateBitmap()
    bmp.CreateCompatibleBitmap(srcdc, width, height)
    memdc.SelectObject(bmp)
    memdc.BitBlt((0, 0), (width, height), srcdc, (left, top), win32con.SRCCOPY)
    
    signedIntsArray = bmp.GetBitmapBits(True)
    img = np.fromstring(signedIntsArray, dtype='uint8')
    img.shape = (height,width,4)

    srcdc.DeleteDC()
    memdc.DeleteDC()
    win32gui.ReleaseDC(hwin, hwindc)
    win32gui.DeleteObject(bmp.GetHandle())

    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

'''
startTime = time.time()
speed = 0

while True:
    img = grab_screen((115,190,400,220))
    img = img[0: , 0:40]
    ret, img = cv2.threshold(img, 100, 255,cv2.THRESH_BINARY_INV)
    cv2.imwrite('tirex.png', img)

    break

    # calculate moments of binary image
    M = cv2.moments(img)

    # calculate x,y coordinate of center
    cX = 0
    cY = 0

    endTime = time.time()

    if(M["m00"] != 0 and endTime - startTime > 1 and endTime - startTime < 1.5):
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])

    if(endTime - startTime > 3):

        cX1 = 0
        cY1 = 0
        
        if(M["m00"] != 0):
            cX1 = int(M["m10"] / M["m00"])
            cY1 = int(M["m01"] / M["m00"])

        distance = math.sqrt(math.pow(cX-cX1, 2)+math.pow(cY-cY1, 2))
        speed = distance/2
        startTime = endTime
        print('Speed : ', speed)
        
    cv2.imshow('Streaming', img)
    if cv2.waitKey(25) & ord('q') == 0xFF:
       break
'''