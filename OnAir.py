#!/usr/bin/env python

import sys
import argparse
from FacebookStreamChecker import FacebookStreamChecker
from TestStreamChecker import TestStreamChecker
import broadcastStatus
import time
from gpiozero import LED


try:
        parser = argparse.ArgumentParser(description='Starts the On Air light')
        parser.add_argument("--mode", help="The mode to start the program in. T for test, F for facebook", choices=["F", "T"], default="T")
        parser.add_argument("--gpio", help="The GPIO pin on the PI that controls the light", default=24)
        parser.add_argument("--url", help="If using Facebook, this is the url for the stream", default="")
        # parser.add_argument("sleep", help="Time in seconds to sleep in between checking the stream")
        args = parser.parse_args()


        # Setup the io pins
        lightOutput = args.gpio
        led = LED(lightOutput)
        #led = 0
        streamChecker = TestStreamChecker()

        if args.mode == "F":
                if not args.url :
                        raise Exception("Url is requried if using Facebook")

                streamChecker = FacebookStreamChecker(args.url)
        else:
                steamChecker = TestStreamChecker()
       

        # Create the object for checking the url
        #checker = TestStreamChecker() #onAirRequest.Request("https://boxcast.tv/view-embed/lbdzh9yeuwejrgyuhgij")
        #steamChecker = StreamChecker(checker)

        while not streamChecker.QuitProgram():
                

                try:
                    
                    if streamChecker.GetBroadcastStatus() == broadcastStatus.broadcastStatus.OnAir :
                            # Turn on the light
                            #led = 1
                            led.on()
                    else:
                            # Turn off the light
                            #led = 0
                            led.off()                        
                except:
                        led.off()
                        exceptionType  = sys.exc_info()[0]
                        exceptionValue = sys.exc_info()[1]
                        exceptionTrace = sys.exc_info()[2]

                        if "HTTP Error 404" not in str(exceptionValue) :
                                print("Type: %s" % exceptionType)
                                print("Value: %s" % exceptionValue)
                                print("Trace: %s" % exceptionTrace)
                        
                #time.sleep(60)
except:
        exceptionType  = sys.exc_info()[0]
        exceptionValue = sys.exc_info()[1]
        exceptionTrace = sys.exc_info()[2]
        print("Type: %s" % exceptionType)
        print("Value: %s" % exceptionValue)
        print("Trace: %s" % exceptionTrace)
finally:
        print("end")
