import sys
import broadcastStatus

class TestStreamChecker():

	def GetBroadcastStatus(self):

		if(self.userInput == "1"):
			rtn = broadcastStatus.broadcastStatus.OnAir
		else:
			rtn = broadcastStatus.broadcastStatus.OffAir

		return rtn

	def QuitProgram(self):

		self.userInput = input("1 = ON; 0 = OFF; Q = Quit:   ")
		return self.userInput.upper() == "Q"