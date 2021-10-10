# This code has to be used in together with
# `serial_example2.ino` running on the Arduino board

# import libraries
import serial
import time

# setup the serial communication
arduino = serial.Serial("COM9", 9600)
time.sleep(0.2)

# initialize list
data = []
num_data = []

# continous cyle (break it with crtl + C)
while True:
    # read data, decode and split the string 
    data.append(((arduino.readline()).decode('ascii')).split(";"))
    # convert them into float
    num_data.append([float(k) for k in data[-1]])
    # print latest data
    print(num_data[-1])

# after "ctrl + c": remember to close the serial communication with:
# arduino.close()