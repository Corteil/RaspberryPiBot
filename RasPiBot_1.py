# basic program for the Raspberry Pi Robot
#
# thrown together by Brian Corteil, a 45 year old script kiddie for the Raspberry Pi
# This is free software, enjoy!!!! if you improve it please share it
# 
# the robot uses the Pibrella library for Pimoroni, because it uses the Pibrella for control and sensing 


# import the pibrella library

import pibrella

# import time functions

import Date

# functions

# move forward for 'n' seconds

def forward(seconds):
    timeStart = date.time()
    flag = True
    while (flag):
        timeNow = date.time()
        if timeNow <= (timeStart + seconds): 
            pibrella.output.E.on()
            pibrella.output.F.on()
        else:
            pibrella.output.E.off()
            pibrella.output.F.off()
            flag = Flase
            
def left(seconds):
    timeStart = date.time()
    flag = True
    while (flag):
        timeNow = date.time()
        if timeNow <= (timeStart + seconds):
            pibrella.output.E.on()
        else:
            pibrella.output.E.off()
            flag = Flase

def right(seconds):
    timeStart = date.time()
    flag = True
    while (flag): 
        timeNow = date.time()
        if timeNow <= (timeStart + seconds):
            pibrella.output.F.on()
        else:
            pibrella.output.F.off()
            flag = Flase

# main program

# move in a square.

for counter in range(1,4):
    forward(2)
    left(1)
    


