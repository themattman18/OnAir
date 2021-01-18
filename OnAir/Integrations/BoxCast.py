#!/usr/bin/env python

import requests
import json
import datetime
import base64
from .broadcastStatus import BroadcastStatus

class BoxCast:
    
    authUrl = "https://auth.boxcast.com/oauth2/token"
    broadcastUrl = "https://api.boxcast.com/"
    clientID = ""
    clientSecret = ""
    authToken = ""
    boxCasterID = ""

    def __init__(self, boxCasterID, clientID, clientSecret):
        
        if not clientID:
            raise Exception("Please pass in a valid clientID")

        if not clientSecret:
            raise Exception("Please pass in a valid client secret")

        if not boxCasterID:
            raise Exception("Please pass in a valid box caster ID")

        self.clientID = clientID
        self.clientSecret = clientSecret
        self.boxCasterID = boxCasterID

        response = requests.post(self.authUrl, data={
                                'grant_type': 'client_credentials',
                                'scope': 'owner',
                                }, 
                                auth=(self.clientID, self.clientSecret))
        print(response.json())
        self.authToken = response.json()['access_token']

    # Gets the current status of the broad cast
    def GetBroadcastStatus(self):
        
        testRsp = requests.get(self.broadcastUrl + "/account/boxcasters/", 
                                headers={'Authorization': 'Bearer ' + self.authToken})
        print("Got the status")
        print(testRsp.json()[0]['status'])
        print(testRsp.json()[0]['status'] == 'broadcasting')

        if testRsp.json()[0]['status'] == 'broadcasting' :
            currentStatus = BroadcastStatus.OnAir
        else :
            currentStatus = BroadcastStatus.OffAir

        return currentStatus