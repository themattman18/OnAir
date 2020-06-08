#!/usr/bin/env python

import sys
import urllib.request
import time
import broadcastStatus
import requests
import json
import datetime

class FacebookStreamChecker():
    
    def __init__(self, url):
        
        if not url:
            raise Exception("Please pass in a valid url")
        self.url = url

    # Gets the current status of the broad cast
    def GetBroadcastStatus(self):

        #currentStatus = Nothing # Current status of the broadcast

        res = requests.get(self.url)
        jsonDictionary = self.ParseResponse(res.text)


        currentTime = datetime.datetime.utcnow()
        startsAt = datetime.datetime.strptime(jsonDictionary["broadcast"]["data"]["starts_at"], "%Y-%m-%dT%H:%M:%SZ")  
        stopsAt = datetime.datetime.strptime(jsonDictionary["broadcast"]["data"]["stops_at"], "%Y-%m-%dT%H:%M:%SZ")  
        
        if currentTime > startsAt and currentTime < stopsAt:
            currentStatus = broadcastStatus.broadcastStatus.OnAir
        else :
            currentStatus = broadcastStatus.broadcastStatus.OffAir

        return currentStatus


    def ParseResponse(self, input):

        jsonLocation = input.find("var BOXCAST_PRELOAD = ")
        jsonDictionary = None

        if jsonLocation != -1 :
            truncatedStart = input[jsonLocation + len("var BOXCAST_PRELOAD = "):]
            jsonEnd = truncatedStart.find("</script>")
            finalStr = truncatedStart[0:jsonEnd]
            finalStr = finalStr.replace("\n ", "")
            finalStr = finalStr.replace("channel:", "\"channel\":")
            finalStr = finalStr.replace("broadcast:", "\"broadcast\":")
            finalStr = finalStr.replace("broadcasts:", "\"broadcasts\":")
            finalStr = finalStr.replace("view:", "\"view\":")
            finalStr = finalStr.replace("},     };", "} }")
            jsonDictionary = json.loads(finalStr)
        
        return jsonDictionary






