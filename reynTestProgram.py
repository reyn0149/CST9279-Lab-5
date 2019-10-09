# A program that tests the functions in reynGfxLibrary.py
import random
inputInt = 0
var1 = 0
var2 = 0
var3 = 0
var4 = 0

print("Hello! Welcome to my test program")
print("Each function is tested with random variables!")
print("Because they're random, try each function multiple times!")
print("Please select one of the options below")
print("1: displayVerticalLine")
print("2: displayHorizontalLine")
print("3: displayStairCase")
print("4: randomPixel")
print("5: setBackLight")
print("6: clearBackLight")
print("7: Quit")

while inputInt != 7:
    inputString =input("Make a selection now! ")
    inputInt = int(inputString)
    if inputInt == 1:
        from reynGfxLibrary import displayVerticalLine
        print("Testing displayVerticalLine function!")
        var1 =random.randint(1,127)
        displayVerticalLine(var1)
    elif inputInt == 2:
        from reynGfxLibrary import displayHorizontalLine
        print("Testing displayHorizontalLine function!")
        var1 =random.randint(1,63)
        displayHorizontalLine(var1)
    elif inputInt == 3:
        from reynGfxLibrary import displayStaircase
        print("Testing displayStaircase function!")
        var1 =random.randint(1,60)
        var2 =random.randint(1,20)
        var3 =random.randint(1,30)
        var4 =random.randint(1,20)
        displayStaircase(var1,var2,var3,var4)
    elif inputInt == 4:
        from reynGfxLibrary import randomPixel
        print("testing randomPixel function!")
        var1 =random.randint(1,5)
        randomPixel(var1)
    elif inputInt == 5:
        from reynGfxLibrary import setBackLight
        print("Giving you a random backlight!")
        var1 =random.randint(0,255)
        var2 =random.randint(0,255)
        var3 =random.randint(0,255)
        setBackLight(var1,var2,var3)
    elif inputInt == 6:
        from reynGfxLibrary import clearBackLight
        print("Clearing your backlight!")
        clearBackLight()
    elif inputInt == 7:
        print("Thanks for testing!")
    else:
        print("Invalid input!")
