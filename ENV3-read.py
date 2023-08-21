from machine import SoftI2C, Pin, #WDT

import sht30
import qmp6988

i2c=SoftI2C(sda=Pin(18), scl=Pin(19))
sht = sht30.SHT30(i2c=i2c)
prt = qmp6988.QMP6988(i2c)

temp, pressure = prt.measure()
print("QMP6988 Temp/Pressure: {:4.2f}°C/{:4.2f}Pa".format(temp, pressure))

temp,humid=sht.measure()
print('SHT30 Temperature/Humidity: {:4.2f}ºC/{:4.2f}%'.format(temp, humid))
