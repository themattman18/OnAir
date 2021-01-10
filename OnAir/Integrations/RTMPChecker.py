#!/usr/bin/env python

import sys
import time
import OnAir.broadcastStatus
import json
import librtmp

class RTMPChecker():
    
    def __init__(self, url):
        
        if not url:
            raise Exception("Please pass in a valid url")
        self.url = url

    # Gets the current status of the broad cast
    def GetBroadcastStatus(self):

        #currentStatus = Nothing # Current status of the broadcast
        

        # Create a connection
        conn = librtmp.RTMP("rtmp://1.live.phonelivestreaming.com:1935/live/", timeout=5, live=True)
        # Attempt to connect
        conn.connect()
        testConnection = conn.connected
        testPacket = conn.read_packet()
        print(testPacket)


        # Get a file-like object to access to the stream
        stream = conn.create_stream()

        
        # Read 1024 bytes of data
        data = stream.read(1024)

        return OnAir.broadcastStatus.BroadcastStatus.OffAir

        # res = requests.get(self.url)
        # jsonDictionary = self.ParseResponse(res.text)


        # currentTime = datetime.datetime.utcnow()
        # startsAt = datetime.datetime.strptime(jsonDictionary["broadcast"]["data"]["starts_at"], "%Y-%m-%dT%H:%M:%SZ")  
        # stopsAt = datetime.datetime.strptime(jsonDictionary["broadcast"]["data"]["stops_at"], "%Y-%m-%dT%H:%M:%SZ")  
        
        # if currentTime > startsAt and currentTime < stopsAt:
        #     currentStatus = broadcastStatus.broadcastStatus.OnAir
        # else :
        #     currentStatus = broadcastStatus.broadcastStatus.OffAir

        # return currentStatus

    # I currently don't have a good way to quit the Facebook checker
    def QuitProgram(self):
        return False

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






