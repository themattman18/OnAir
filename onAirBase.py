#!/usr/bin/env python

import sys
import onAirRequest
import broadcastStatus
import time
import RPi.GPIO as GPIO

try:

        # Setup the io pins
        GPIO.setmode(GPIO.BCM) 
        GPIO.setwarnings(False)
        lightOutput = 24
        GPIO.setup(lightOutput, GPIO.OUT)

        # Create the object for checking the url
        checker = onAirRequest.Request("https://boxcast.tv/view/sunday-evening-service-875615")
   
        while True:
                

                try:
                    
                    
                    print(checker.GetBroadcastStatus())


                    if checker.GetBroadcastStatus("https://boxcast.tv/view/sunday-evening-service-875615") == broadcastStatus.broadcastStatus.OnAir :
                            # Turn on the light
                            GPIO.output(lightOutput, 1)
                            #print("We are still streaming")
                    else:
                            # Turn off the light
                            GPIO.output(lightOutput, 0)
                            #print("Not streaming")
                        
                except:
                        GPIO.output(lightOutput, 0)
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
        GPIO.cleanup()



