# TirexAI
Neural Network play T-Rex

To run this programme without error you need

Python 3.6 and libraries

pywin32, numpy, opencv, tensorflow, keras

you can install them by running these commands on cmd or terminal

pip install pywin32
pip install numpy
pip install opencv-python
pip install tensorflow
pip install keras

to launch the AI you need to open tirex game put the window of chrome to the left most and start the game
and click on another window so the game will be paused then launch test.py and wait for the script to detect the game
after the game is detected just click on the chrome window and let the AI play

this AI is trained on this game
https://github.com/wayou/t-rex-runner

you can dowload it and use it
if you use another game you can face issus where the AI can't play well
you can always retrain your model by running the script extract_info.py don't forget to pause the game
until the script detect your game and delete all data in newData folder then play for while like 15min
then run the script balance_data.py to balance data then run train.py and wait for training to end
then you can play the game

the probleme with this scripts is detecting the game to capture the video, the game can be anywhere in the screen you can always set
your settings to capture the screen and set your gameover detector and retrain the model

if you set your own settings to capture the screen try to not capture t-rex capture what's in front of him and
don't capture the highest flying bird

