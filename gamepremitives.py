import numpy as np
import cv2

# detect object incoming
def detect_object(img):
    height, width = img.shape
    for i in range(0, width):
        for j in range(0, height):
            if img[j, i] == 255:
                return (j, i)
    
    return (0, 0)

# detect if player lost "Game over"
def detect_gameover(img, go):
    a = np.sum(img == go)
    if a > 159 and a < 261:
        return True
    return False

# detect if the game is on night mode
def nightMode(img):
    a = np.sum(img == 255)
    if a > 2000:
        ret, img = cv2.threshold(img, 100, 255,cv2.THRESH_BINARY_INV)
        img = img[10: , 0: ]
    return img