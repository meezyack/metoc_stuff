#!/usr/bin/env python3
#This is a generic script for logging sensor data from a sensor connected to a raspberry pi.
#To run this as a background process on the CLI, type 'python3 file_write_TSM.py &'
#type 'kill -9' followed by PID number to terminate process

#The script does the following.
#1)Creates a file for the sensor data onboard the computer companion
#2)Reads the incoming Serial data and stores it in a variable
#3)Creates a mavlink packet to forward to the ardupilot flight controller.

#!/usr/bin/env python
import time
import serial
import datetime
from os.path import exists
from pymavlink import mavutil

#Set Up Serial Port for the sensor
#Ensure you are using the correct header name in '/dev' which the component is plugged in to. If the ETHUSB Hub Hat is attached, the ttyUSB number sometimes changes between zero and one.
ser = serial.Serial(
        '/dev/ttyUSB0',
        baudrate = 115200,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
)

ser0 = serial.Serial(
	'/dev/serial0',
	baudrate = 912600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
)

ser1 = serial.Serial(
        '/dev/serial1',
        baudrate = 912600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
)

#The program will continue to write into the file until it is terminated.
while 1:
    data_in = ser.read(100)
    if ser0:
        print("Sending to serial0: \n%s" % data_in)
        ser0.write(data_in)
        data_out= ser0.write(data_in)
        time.sleep(2)
    else:
        print("Sending to serial1: \n%s" % data_in)
        ser1.write(data_in)
        data_out= ser1.write(data_in)
        time.sleep(2)
