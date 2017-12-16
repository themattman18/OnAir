import time
import RPi.GPIO as GPIO
import sys

try:

	# Setup the io pins
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	lightOutput = 24
	GPIO.setup(lightOutput, GPIO.OUT)
	
	userInput = input("1 = ON; 0 = OFF; Q = Quit:   ")

	while userInput.upper() != "Q":


		try:
			print("User entered: %s" % userInput)

			if userInput == "1" :
				# Turn on the light
				GPIO.output(lightOutput, 1)
				print("Turned the light on")
			else:
				# Turn off the light
				GPIO.output(lightOutput, 0)
				print("Turned the light off")

		except:
			GPIO.output(lightOutput, 0)
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



