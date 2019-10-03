# A fuction that displays a vertical line at a x coordinate
def displayVerticalLine(x):
    from gfxhat import lcd
    lcd.clear()
    i = 0
    while i < 64:
        lcd.set_pixel(x,i,1)
        lcd.show()
        i = i+1

# A function that displays a horizontal line at a y coordinate
def displayHorizontalLine(y):
    from gfxhat import lcd
    lcd.clear()
    i = 0
    while i < 128:
        lcd.set_pixel(i,y,1)
        lcd.show()
        i = i+1

#A fuction that displays a staircase at a specific cordinate, with each step being width wide and height tall
def displayStaircase(x,y,width,height):
    from gfxhat import lcd
    lcd.clear()
    while x < 127 and y < 63:
        for i in range(width):
            lcd.set_pixel(x,y,1)
            lcd.show()
            if y < 63 and x < 127:
                x = x+1
            else:
                break
        for i in range(height):
            lcd.set_pixel(x,y,1)
            lcd.show()
            if y < 63 and x <127:
                y = y+1
            else:
                break

#A fuction that displays a random pixel on the screen for a set amount of time
def randomPixel(waitTime):
    import random, time
    from gfxhat import lcd
    lcd.clear()
    x = random.randint(1,127)
    y = random.randint(1,63)
    lcd.set_pixel(x,y,1)
    lcd.show()
    time.sleep(waitTime)
    lcd.clear()
    lcd.show()

# A function that sets a backlight color
def setBackLight(r,g,b):
    from gfxhat import backlight
    backlight.set_all(r,g,b)
    backlight.show()

#A fuction that resets the backlight color
def clearBackLight():
    from gfxhat import backlight
    backlight.set_all(0,0,0)
    backlight.show()