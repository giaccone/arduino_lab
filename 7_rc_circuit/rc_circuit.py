# libraries
import serial
import numpy as np
from drawnow import drawnow
import matplotlib.pyplot as plt

# plot function
def makeplot():
        # plot voltage vs time
        plt.plot(x, y, 'ko', markersize=8, markerfacecolor='none', markeredgewidth=2)
        plt.xlabel("time (s)", fontsize=18)
        plt.ylabel("voltage (V)", fontsize=18)
        plt.xticks(fontsize=18)
        plt.yticks(fontsize=18)
        plt.tight_layout()
    

# read from arduino
arduino = serial.Serial('/dev/ttyACM0', 9600)
# initialize measured data and figure
x = []
y = []
plt.figure(figsize=(10,8))
# start aquisition
while True:
    read = arduino.readline()
    time, voltage  = [float(k) for k in read.decode('ascii').split(";")]
    x.append(time * 1e-6)
    y.append(voltage)
    # make plot
    drawnow(makeplot)

