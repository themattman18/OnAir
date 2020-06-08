#!/usr/bin/env python

import sys
import argparse
from FacebookStreamChecker import FacebookStreamChecker
from TestStreamChecker import TestStreamChecker
import broadcastStatus
import time
#from gpiozero import LED


try:
        
        # parser = argparse.ArgumentParser(description='Starts the On Air light')
        # parser.add_argument("url", help="The embed URL for the boxcast stream")
        # parser.add_argument("sleep", help="Time in seconds to sleep in between checking the stream")
        # # parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer for the accumulator')
        # # parser.add_argument('--sum', dest='accumulate', action='store_const', const=sum, default=max, help='sum the integers (default: find the max)')
        # args = parser.parse_args()

        # print(args.url)
        #args = parser.parse_args()
        #print args.accumulate(args.integers)
        #print args.accumulate(args.integers)

        #args = sys.argv[1:]
        #fffff = getopt.getopt(args, "-p -t")
        #getopt.getopt(args, options, [long_options])

        # Setup the io pins
        lightOutput = 24
        #led = LED(lightOutput)
        foo = 0
        led = 0
        streamChecker = TestStreamChecker()

        # if foo == 1:
        #         streamChecker = FacebookStreamChecker()
        # else:
        #         steamChecker = TestStreamChecker()
       

        # Create the object for checking the url
        #checker = TestStreamChecker() #onAirRequest.Request("https://boxcast.tv/view-embed/lbdzh9yeuwejrgyuhgij")
        #steamChecker = StreamChecker(checker)

        while not streamChecker.QuitProgram():
                

                try:
                    
                    if streamChecker.GetBroadcastStatus() == broadcastStatus.broadcastStatus.OnAir :
                            # Turn on the light
                            led = 1
                            #led.on()
                    else:
                            # Turn off the light
                            led = 0
                            #led.off()                        
                except:
                        led.off()
                        exceptionType  = sys.exc_info()[0]
                        exceptionValue = sys.exc_info()[1]
                        exceptionTrace = sys.exc_info()[2]

                        if "HTTP Error 404" not in str(exceptionValue) :
                                print("Type: %s" % exceptionType)
                                print("Value: %s" % exceptionValue)
                                print("Trace: %s" % exceptionTrace)
                        
                time.sleep(60)
except:
        exceptionType  = sys.exc_info()[0]
        exceptionValue = sys.exc_info()[1]
        exceptionTrace = sys.exc_info()[2]
        print("Type: %s" % exceptionType)
        print("Value: %s" % exceptionValue)
        print("Trace: %s" % exceptionTrace)
finally:
        print("end")