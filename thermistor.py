# Import PyBBIO library:
from bbio import *
 
therm1 = AIN6 # pin 37 on header P9
 
def readThermistor():
    # Get the ADC values:
    adc_val = analogRead(therm1)
    # And convert to voltages:
    voltage1 = inVolts(adc_val)
    print "AIN6 ADC value: %i, voltage: %fv" % (adc_val, voltage1)
    delay(500)
 
# Start the loop:
while 1:
    readThermistor()
