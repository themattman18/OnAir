#!/usr/bin/env python

from enum import Enum

class BroadcastStatus(Enum):
  OnAir = 1
  OffAir = 2
  AuthTimeout = 3