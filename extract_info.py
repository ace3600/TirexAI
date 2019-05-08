#CODE TO CAPTURE THE SCREEN AND EXTRACT INFORMATION

import cv2
import time
from math import sqrt, pow
import numpy as np
from grabscreen import grab_screen
from getkeys import key_check
import os

space = [1,0]
nokey = [0,1]

# convert keypressed to output for neural network
def keys_to_output(keys):
    output = [0,0]

    if ' ' in keys:
        output = space
    else:
        output = nokey

    return output

starting_value = 1
file_name = 'newData/training_data-{}.npy'.format(starting_value)

while os.path.isfile(file_name):
    starting_value += 1
    print('Cheking ...')
    file_name = 'newData/training_data-{}.npy'.format(starting_value)

if(starting_value == 1):
    print('Starting fresh')
else:
    print('Resuming')

print('Starting in ')
for i in reversed(range(1,4)):
    print(i)
    time.sleep(1)

training_data = []

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
    if(np.array_equal(img, go)):
        return True
    return False

startTime = time.time() # calculate time to increase speed
speed = 1 # init speed
distance = 0 # init distance
go_img1 = cv2.imread('gameOver.png', cv2.IMREAD_GRAYSCALE)

# get game coordinates on screen
game_coordinates = detectGame()

while True:
    # grab the screen
    img = grab_screen(game_coordinates)
    ret, img = cv2.threshold(img, 100, 255,cv2.THRESH_BINARY_INV)
    go_img2 = img[0:10 , 220:]

    # detect object incoming
    y, x = detect_object(img)
    distance = 0

    if not(detect_gameover(go_img1, go_img2)):
        # if not game over
        if(y == 0 and x == 0):
            #print('No Object detected')
            distance = 0
        else:
            distance = sqrt(pow(y, 2) + pow(x, 2))
            #print('Object detected   Distance ', distance,'  Speed  ', speed)
        
        # calculate time to increase the speed
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
                elapsedTime = 0

    else:
        # if game over then reinit speed and time
        print('Game Over')
        startTime = time.time()
        speed = 1
        distance = 99999

    # store distance and speed as input
    info = np.array([distance, speed])

    # check keypressed and store it as output
    keys = key_check()
    output = keys_to_output(keys)
    training_data.append([info, output])

    # after collecting 10000 sample store data
    if len(training_data)%100 == 0:
        print(len(training_data))
        if(len(training_data) == 10000):
            print('Saving')
            np.save(file_name, training_data)
            starting_value += 1
            file_name = 'newData/training_data-{}.npy'.format(starting_value)
            training_data = []
    
    if cv2.waitKey(25) & ord('q') == 0xFF:
       break



    
