#!/usr/bin/env python

import sys
import argparse
from Integrations import BoxCast
from Integrations import broadcastStatus
import time
#import RPi.GPIO as GPIO
from gpiozero import LED

try:
        parser = argparse.ArgumentParser()

        parser.add_argument("gpio")
        parser.add_argument("sleepTime")
        parser.add_argument("boxCasterID")
        parser.add_argument("clientID")
        parser.add_argument("clientSecret")

        args = parser.parse_args()


        #GPIO.setmode(GPIO.BOARD)
        #GPIO.setwarnings(False)
        #GPIO.setup(24, GPIO.OUT)
        # list of options tuple (opt, value)
        #print(f'Options Tuple is {opts}')

        #lightOutput = "GPIO24" #args.gpio
        sleepTime = args.sleepTime

        # Setup the io pins
        led = LED(24)

        # Create the object for checking the url
        checker = BoxCast.BoxCast(args.boxCasterID, args.clientID, args.clientSecret)
        print("here")
        while True:
                

                try:
                    print("About to check the status")
                    if checker.GetBroadcastStatus() == broadcastStatus.BroadcastStatus.OnAir :
                        # Turn on the light
                        #GPIO.output(24, GPIO.HIGH)
                        print("We are still streaming")
                        led.on()
                    else :
                        # Turn off the light
                        led.off()
                        print("Not streaming")
                        
                except:
                        #led.off()
                        exceptionType  = sys.exc_info()[0]
                        exceptionValue = sys.exc_info()[1]
                        exceptionTrace = sys.exc_info()[2]

                        if "HTTP Error 404" not in str(exceptionValue) :
                                print("Type: %s" % exceptionType)
                                print("Value: %s" % exceptionValue)
                                print("Trace: %s" % exceptionTrace)
                        
                time.sleep(3)
except:
        exceptionType  = sys.exc_info()[0]
        exceptionValue = sys.exc_info()[1]
        exceptionTrace = sys.exc_info()[2]
        print("Type: %s" % exceptionType)
        print("Value: %s" % exceptionValue)
        print("Trace: %s" % exceptionTrace)
finally:
        print("end")
