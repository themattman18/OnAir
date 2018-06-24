#!/usr/bin/env python

import sys
import urllib.request
import time
import broadcastStatus
import requests

class Request:

    # Gets the current status of the broad cast
    def GetBroadcastStatus(url):

        currentStatus # Current status of the broadcast


        if not url:
            raise Exception("Please pass in a valid url")
           

        res = requests.get(url)

        if res.status == "boadcasting":
            currentStatus = broadcastStatus.broadcastStatus.OnAir
        else :
            currentStatus = broadcastStatus.broadcastStatus.OffAir

        return currentStatus




