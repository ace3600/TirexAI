# code to declare neural network and train it

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation
from random import shuffle
import numpy as np
import cv2

# name of neural network
MODEL_NAME = 'tirexu.h5'

# NEURAL NETWORK
model = Sequential()
model.add(Dense(64, input_shape=(2,), activation='relu'))

model.add(Dense(128, activation='relu'))
model.add(Dropout(0.2))

model.add(Dense(256, activation='relu'))
model.add(Dropout(0.4))

model.add(Dense(512, activation='relu'))
model.add(Dropout(0.4))

model.add(Dense(1024, activation='relu'))
model.add(Dropout(0.5))

model.add(Dense(2, activation='softmax'))

model.compile(loss='categorical_crossentropy',
                optimizer='adam', metrics=['accuracy'])

# train for 50 epoch
EPOCH = 50
FILES_NUMBER = 3

for e in range(EPOCH):

    print('-------------------EPOOOOOCH',e,'--------------------')
    
    # load data
    data_order = [i for i in range(1, FILES_NUMBER)]
    shuffle(data_order)

    for count, i in enumerate(data_order):
        try:
            # load data
            file_name = 'newData/training_data-{}.npy'.format(i)
            train_data = np.load(file_name)
            np.random.shuffle(train_data)

            print(file_name, len(train_data))

            # shape the data to be compatible with the neural network
            X = np.array([i[0] for i in train_data])
            y = np.array([i[1] for i in train_data])
            
            # train
            model.fit(X, y, epochs=3, verbose=2,
                        validation_split=0.1)

        except Exception as e:
            print(str(e))

# after training ends save the model
model.save(MODEL_NAME)