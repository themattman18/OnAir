#!/usr/bin/env python

import sys
import onAirRequest
import broadcastStatus
import time
#import RPi.GPIO as GPIO
from gpiozero import LED


try:

        # Setup the io pins
        #GPIO.setmode(GPIO.BCM) 
        #GPIO.setwarnings(False)
        lightOutput = 24
        #GPIO.setup(lightOutput, GPIO.OUT)

        #led = LED(lightOutput)


        # Create the object for checking the url
        checker = onAirRequest.Request("https://boxcast.tv/view-embed/lbdzh9yeuwejrgyuhgij")
   
        while True:
                

                try:
                    
                    if checker.GetBroadcastStatus() == broadcastStatus.broadcastStatus.OnAir :
                            # Turn on the light
                            leg.on()
                            #print("We are still streaming")
                    else:
                            # Turn off the light
                            led.off()
                            #print("Not streaming")
                        
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