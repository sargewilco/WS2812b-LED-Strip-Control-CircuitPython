import board
import neopixel
import random
import time

pixels = neopixel.NeoPixel(board.D6, 100, brightness=.3, auto_write=False)
testcol = (255, 255, 255)
ttype=type(testcol)
print(ttype)
#pixels[4] = (testcol)
pixels.show()

#colors = {0:(0, 255, 75), 1:(0, 255, 0), 2:(255, 255, 255)} #St. Patrick's/March
colors = {0:(255, 0, 0), 1:(255, 0, 75), 2:(255, 255, 255)} #St. Patrick's/March - Weird Alitove String
#colors = {0:(255, 0, 75), 1:(255, 0, 0), 2:(255, 255, 255)} #St. Valentine's/February
#colors = {0:(255, 0, 0), 1:(255, 255, 255), 2:(0, 0, 255)} #Fourth of July
#colors = {0:(0, 255, 0), 1:(0, 255, 0), 2:(0, 0, 255), 3:(0, 0, 255)} #Seahawks
#colors = {0:(255, 0, 0), 1:(255, 165, 0), 2:(255, 255, 0), 3:(0, 255, 0), 4:(0, 0, 255), 5:(0, 35, 200), 6:(255, 0, 255)}
ccount = len(colors)
#print (ccount)
# print(colors[2])

data = range(0,100)
chunks = [data[x:x+ccount] for x in range(0, len(data), ccount)]
# print ("hello")
# print ("this is a chunk:", chunks[3])

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

while True:
    t = random.randrange(1, 100, 2)
    oc = pixels[t]
    pixels[t] = (174, 255, 0) #Alitove String modification for GRB
    #pixels[t] = (255, 174, 0) #Standard LED RGB 
    print("LED:", t, "has been twinkled")
    pixels.show()
    time.sleep(.15)
    pixels[t] = (255, 255, 255)
    pixels.show()
    time.sleep(.01)
    pixels[t] = oc
    pixels.show()
    
    