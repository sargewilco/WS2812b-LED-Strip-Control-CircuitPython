# Long Light Strip Pattern with WS2812B "pixels"
# Tom Cannon Feb 27th, 2018

#Import the required libraries.  Board is required to address the microcontroller
#neopixel provides functions related to driving the LEDs
#time is timey wimey and can be used to handled relative timing for fades, etc...
#random is used to pick the LEDs for twinkling effects.
import board
import neopixel
#import time
#import random

#Establish the pixels variable to use when addressing the strip of LEDs.
#Set the control pin on the board and the length of the pixel strip.
pixels = neopixel.NeoPixel(board.D6, 300, brightness=0.1, auto_write=False)

#break the stip into chunks that can be painted with a pattern.
#interating through the chunks with the pattern will provide a full strip.
#change the number to the number of pixels required in each pattern.
#e.g. 3 for a pattern that has three colors like Yellow, Orange, Green.
chunks = [pixels[x:x+3] for x in range(0, len(pixels), 3)]

#set the list of colors that you want to use in your pattern.
#these will be addressed as their element position. colors[0], colors[1], etc
colors = ["0,255,0", "255,0,0", "0,0,255"]

pixels[4] = (0, 255, 255)
pixels.write()
while True:
    for p in chunks:
        n=0
        for subp in p:
            pixels(p[n]) = (colors[n])
            pixels.write()
            
        n=n+1
    
    
    #print(range(pixels))
    #print(range(pixels))
    #for g in sgroup:
    #pixels[0] = (0, 255, 255)
      #  print("Test")
       # pixels.show()
        #time.sleep(.0001)
        
    
    

