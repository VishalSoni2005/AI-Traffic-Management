import time
from gpiozero import LED

# Class Created
class led:
    # Creating Variables for GPIO Pins
    a = b = c = d = 0
    def __init__(self,a,b,c,d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    # Creating LED objects
    led1 = LED(a)
    led2 = LED(b)
    led3 = LED(c)
    led4 = LED(d)
    # Default is Green Signal
    def on(a=2):
        if a==0: # For red signal
            led1.on()
            led2.off()
            led3.off()
            led4.off()
        elif a==1: # For Yellow signal
            led1.off()
            led2.on()
            led3.off()
            led4.off()
        elif a==2: # For Green signal
            led1.off()
            led2.off()
            led3.on()
            led4.off()
        elif a==3: # For emergency (blue) signal
            led1.off()
            led2.off()
            led3.off()
            led4.on()
        else: # For every other parameter
            print("Wrong input...")