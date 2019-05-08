# CODE TO BALANCE DATA

import numpy as np
import cv2
from random import shuffle
import os

starting_value = 1
file_name = 'newData/training_data-{}.npy'.format(starting_value)

while os.path.isfile(file_name):    

    training_data = np.load(file_name)

    jump = []
    nokey = []

    np.random.shuffle(training_data)

    for data in training_data:
        
        choice = data[1]
        print(choice)
        if list(choice) == [1,0]:
            jump.append(data)
        else:
            nokey.append(data)


    if len(jump) < len(nokey):
        nokey = nokey[:len(jump)]
    else:
        jump = jump[:len(nokey)]

    training_data = jump + nokey

    np.random.shuffle(training_data)
    np.save(file_name, training_data)

    starting_value += 1
    file_name = 'newData/training_data-{}.npy'.format(starting_value)












