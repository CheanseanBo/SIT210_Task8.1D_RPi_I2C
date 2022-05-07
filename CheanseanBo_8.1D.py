#Reference: https://www.raspberrypi-spy.co.uk/2015/03/bh1750fvi-i2c-digital-light-intensity-sensor/

#Use smbus library to interact with I2C address bus
import smbus
import time
import math

#0x23 is BH1750 Sensor Address Bus when connected with Ground pin
I2C = 0x23 

#This will trigger the sensor to measure once only
Register = 0x23

#This will start the I2C interface
bus = smbus.SMBus(1)

def LightData(data):
	#Formula to convert 2 bytes of data into value
	lightValue = (data[1] + (256 * data[0])) / 1.2
	return lightValue

def LightSensor():
	#This function is used to read the 2 bytes of data 
	#Data receive from sensor address bus once due to Register type
	lightValue = bus.read_i2c_block_data(I2C, Register)
	return LightData(lightValue)
	
try:
	while 1:
		#Loop to turn on and off LED curcuit on PIN 10 every 0.25s
		lightValue = math.floor(LightSensor())
		#Print out lightValue 
		print(lightValue, end = "")
		#Depending on the value, the program will print out the category
		if 25 <= lightValue <= 80:
			print(" Medium")
		elif 10 <= lightValue < 25:
			print(" Dark")
		elif 0 <= lightValue < 10:
			print(" Too Dark")
		elif 80 <lightValue <= 400:
			print(" Bright")
		else:
			print(" Too bright")
		time.sleep(0.5)



except KeyboardInterrupt:
	GPIO.cleanup()
