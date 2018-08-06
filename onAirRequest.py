#!/usr/bin/env python

import sys
import urllib.request
import time
import broadcastStatus
import requests

class Request:
    
    def __init__(self, url):
        
        if not url:
            raise Exception("Please pass in a valid url")
        self.url = url

    # Gets the current status of the broad cast
    def GetBroadcastStatus(self):

        #currentStatus = Nothing # Current status of the broadcast

        res = requests.get(self.url)
        
        print(res)

        if res.status == "boadcasting":
            currentStatus = broadcastStatus.broadcastStatus.OnAir
        else :
            currentStatus = broadcastStatus.broadcastStatus.OffAir

        return currentStatus




