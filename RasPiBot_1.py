# basic program for the Raspberry Pi Robot
#
# thrown together by Brian Corteil, a 45 year old script kiddie for the Raspberry Pi
# This is free software, enjoy!!!! if you improve it, please share it
# 
# the robot uses the Pibrella library for Pimoroni, because it uses the Pibrella for control and sensing 


# import the pibrella library

import pibrella

# import time functions

from time import sleep

# functions

# move forward for 'n' seconds

def forward(seconds):
    
    pibrella.output.E.on()
    pibrella.output.F.on()
    sleep(seconds)
    pibrella.output.E.off()
    pibrella.output.F.off()
            
def left(seconds):
    
    pibrella.output.E.on()
    sleep(seconds)
    pibrella.output.E.off()
    
def right(seconds):
    
    pibrella.output.F.on()
    sleep(seconds)
    pibrella.output.F.off()
    
# main program

# move in a square.

for counter in range(1,4):
    forward(2)
    left(1)
    


