# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 09:47:45 2018

@author: Tom
"""

import board
import neopixel

pixels = neopixel.NeoPixel(board.D6, 300, brightness=0.1, auto_write=False)
testcol = (255, 255, 255)
ttype=type(testcol)
print(ttype)
pixels[4] = (testcol)
pixels.show()

data = range(0,300)
chunks = [data[x:x+3] for x in range(0, len(data), 3)]
# print ("hello")
# print ("this is a chunk:", chunks[3])

colors = {0:(255, 0, 50), 1:(255, 0, 200), 2:(255, 255, 255)}

# print(colors[2])

for p in chunks:
        
    n = 0
    for subp in p:
        print ("this is chunks",p, "subpart", n,":",p[n], colors[n])
        wp = p[n]
        print ("this is wp:", wp)
        color = colors[n]
        print(color)
        pixels[wp] = (color)
        print(p)
        pixels.show()
            
            
        n = n+1