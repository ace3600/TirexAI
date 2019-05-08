import numpy as np
import cv2
from grabscreen import grab_screen

def detectGame():
    img = grab_screen((0, 0, 1600, 900))
    ret, img = cv2.threshold(img, 100, 255,cv2.THRESH_BINARY_INV)

    tirex = cv2.imread('tirex.png', cv2.IMREAD_GRAYSCALE)

    rows, cols = img.shape

    for i in range(0, rows):
        for j in range(0, cols):
            if i+31 < rows:
                if j+40 < cols:
                    img_to_test = img[i:i+31, j:j+40]
                    if np.array_equal(img_to_test, tirex):
                        print('Game detected')
                        return(j+40 , i, j+40+245, i+30)
            else:
                print('Game not detected')
                return (0, 0, 0, 0)

print(detectGame())  