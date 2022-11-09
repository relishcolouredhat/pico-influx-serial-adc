import machine
import utime
 
analog_value = machine.ADC(28)

def adc_loop():
    while True:
      reading = analog_value.read_u16()     
      print("micropy adc={}".format(reading))
      utime.sleep(0.1)
      
adc_loop()
