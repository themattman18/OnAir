import time
from gpiozero import LED
import sys

try:

	# Setup the io pins
	lightOutput = 24
	led = LED(lightOutput)
	
	userInput = input("1 = ON; 0 = OFF; Q = Quit:   ")

	while userInput.upper() != "Q":


		try:
			print("User entered: %s" % userInput)

			if userInput == "1" :
				# Turn on the light
				led.on()
				print("Turned the light on")
			else:
				# Turn off the light
				led.off()
				print("Turned the light off")

		except:
			led.off()
			exceptionType  = sys.exc_info()[0]
			exceptionValue = sys.exc_info()[1]
			exceptionTrace = sys.exc_info()[2]

			if "HTTP Error 404" not in str(exceptionValue) :
				print("Type: %s" % exceptionType)
				print("Value: %s" % exceptionValue)
				print("Trace: %s" % exceptionTrace)

		userInput = input("1 = ON; 0 = OFF; Q = Quit:   ")

	       
except:
	exceptionType  = sys.exc_info()[0]
	exceptionValue = sys.exc_info()[1]
	exceptionTrace = sys.exc_info()[2]
	print("Type: %s" % exceptionType)
	print("Value: %s" % exceptionValue)
	print("Trace: %s" % exceptionTrace)
finally:
	print("end")
	#GPIO.cleanup()



