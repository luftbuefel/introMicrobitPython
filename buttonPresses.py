from microbit import *


images = [Image.HAPPY, Image.SAD, Image.MEH]
imagePointer = 0

while True:
    #this only triggers when you let the button up
    #it will not give you multiple positive results with one button press like .is_pressed() can
    if button_a.was_pressed():
        display.show(images[imagePointer])
        imagePointer  += 1
        if(imagePointer>=len(images)):
            imagePointer = 0
