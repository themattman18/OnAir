#!/usr/bin/env python

import sys
import urllib.request
import time
import RPi.GPIO as GPIO

try:

        # Setup the io pins
        GPIO.setmode(GPIO.BCM) 
        GPIO.setwarnings(False)
        lightOutput = 24
        GPIO.setup(lightOutput, GPIO.OUT)

        while True:
                
                try:
                    response = requests.get('https://api.boxcast.com/broadcasts', params={
                                  'q': 'timeframe:relevant',
                                  's': '-starts_at',
                                  'l': '5'
                                }, headers={'Authorization': 'Bearer YKLCJ-EJHnFXV4TThF7YNPdkyz3ia29UmCJY3vZOB'}
                    print response.json()
                    testing = 'https://boxcast.tv/channel/lbdzh9yeuwejrgyuhgij'
                    response = urllib.request.urlopen('http://lbctheodore.sermon.net/l/20137241')
                    responseCode = response.getcode()

                        if responseCode == 200 :
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



