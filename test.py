import tensorflow as tf
from keras.models import load_model
from random import shuffle
import numpy as np
import cv2
from grabscreen import grab_screen
from getkeys import key_check
from directkeys import PressKey, ReleaseKey, SPACE
import os
import time
from math import sqrt, pow
from detectgame import detectGame
from gamepremitives import nightMode, detect_gameover, detect_object

MODEL_NAME = 'tirexu.h5'

# load our model
model = tf.keras.models.load_model(MODEL_NAME)

startTime = time.time()
speed = 1
distance = 0
go_img1 = cv2.imread('gameOver.png', cv2.IMREAD_GRAYSCALE)

# get game coordinates on screen
game_coordinates = detectGame()
               
while True:
    # grab the screen
    img = grab_screen(game_coordinates)
    ret, img = cv2.threshold(img, 100, 255,cv2.THRESH_BINARY_INV)

    # if the game is on night mode convert to day mode
    img = nightMode(img)

    go_img2 = img[0:10 , 220:]
    y, x = detect_object(img)
    distance = 0
    
    if not(detect_gameover(go_img2, go_img1)):
        if(y == 0 and x == 0):
            x = 0 # do nothing
        else:
            distance = sqrt(pow(y, 2) + pow(x, 2))
        
        elapsedTime = time.time() - startTime
        if(elapsedTime > 35 and elapsedTime < 40):
            if(speed == 1):
                speed += 1
        
        if(elapsedTime > 55):
            if(speed == 2):
                speed += 1

        if(elapsedTime > 75):
            if(speed == 3):
                speed += 1

        if(elapsedTime > 90):
            if(speed == 4):
                speed += 1

        if(elapsedTime > 105):
            if(speed == 5):
                speed += 1

    else:
        # if game over restart the game
        startTime = time.time()
        speed = 1
        distance = 99999
        ReleaseKey(SPACE)
        time.sleep(0.2)
        PressKey(SPACE)
        time.sleep(0.2)


    # get info
    info = np.array([distance, speed])

    # feed it to the neural network
    prediction = model.predict(info.reshape(-1, 2))

    # get output
    choice = np.argmax(prediction[0])

    if(choice == 0):
        PressKey(SPACE)
    else:
        ReleaseKey(SPACE)

    if cv2.waitKey(25) & ord('q') == 0xFF:
       break