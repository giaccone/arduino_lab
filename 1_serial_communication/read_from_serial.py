# This code has to be used in together with
# `serial_example2.ino` running on the Arduino board

# import libraries
import serial
import time

# setup the serial communication 
arduino = serial.Serial('/dev/ttyACM0', 9600)
time.sleep(0.2)

# initialize list
data = []
num_data = []
# continous cyle (break it with crtl + C)
while True:
    # read data and decode them
    data.append((arduino.readline()).decode('ascii'))
    # split data and convert them into float
    num_data.append([float(k) for k in data[-1].split(";")])
    # print latest data
    print(num_data[-1])