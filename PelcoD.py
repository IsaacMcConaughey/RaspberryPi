# Pelco-D-Raspberry-Pi
# How to implementing the Pelco D Protocol on the Raspberry Pi with Python
# Written by Isaac McConaughey

# Requirements:
# - Raspberry Pi with Python installed
# - Rotating bracket connected via USB

import serial

ser = serial.Serial(
    port="/dev/ttyUSB0",
    baudrate=2400,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)

help_message = "0 exit ; 1 left ; 2 right ; 3 stop ; 4 set preset ; 5 go to preset ; 6 clear preset"
print help_message
ser.open()

while True:
    a = input("command:")
    
    if a == 0:
        print "closing...       FF 01 00 00 00 00 01"
        ser.write("\xFF\x01\x00\x00\x00\x00\x01")
        ser.close()
        exit()
    
    if a == 1:
        print "pan left ;       FF 01 00 04 00 00 05"
	      ser.write("\xFF\x01\x00\x04\x00\x00\x05")
    
    if a == 3:
        print "pan stop ;       FF 01 00 00 00 00 01"
        ser.write("\xFF\x01\x00\x00\x00\x00\x01")
    
    if a == 4:
        print "set preset ;     FF 01 00 03 00 01 05"
        ser.write("\xFF\x01\x00\x03\x00\x01\x05")
    
    if a == 5:
        print "go to preset ;   FF 01 00 07 00 01 09"
        ser.write("\xFF\x01\x00\x07\x00\x01\x09")
    
    if a == 6:
        print "clear preset ;   FF 01 00 05 00 01 07"
        ser.write("\xFF\x01\x00\x05\x00\x01\x07")
