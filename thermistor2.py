import Adafruit_BBIO.ADC as ADC
import time
ADC.setup()

while True:
	mV = ADC.read('P9_40')*3300
	celsius = mV / 10
	fahrenheit = (celsius * 9/5) + 32
	print round(fahrenheit, 1)
	time.sleep(1)
