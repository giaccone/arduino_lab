# libraries
import serial
import numpy as np
from drawnow import drawnow
import matplotlib.pyplot as plt

# decorator
def add_measurement(function):

    def wrapper():
        # plot power locus
        function()
        # add measurement
        plt.plot(x, y, 'ko', markersize=8, markerfacecolor='none', markeredgewidth=2)
        plt.tight_layout()
    
    return wrapper


# plot function
@add_measurement
def power_locus():
    # potentiometer range
    r = np.linspace(0, 10, 100) * 1e3
 
    # generator parameters
    E = 5
    R1 = 2e3
    power1 = r * (E / (R1 + r))**2
    R2 = 4e3
    power2 = r * (E / (R2 + r))**2
    
    # plot
    plt.plot(r*1e-3, power1 * 1e3, 'r--', label='R = 2 k$\Omega$', linewidth=2)
    plt.plot(r*1e-3, power2 * 1e3, 'g--', label='R = 4 k$\Omega$', linewidth=2)
    plt.xlabel('resistance (k$\Omega$)', fontsize=18)
    plt.ylabel('power (mW)', fontsize=18)
    plt.xticks([0, 2, 4, 10], fontsize=18)
    plt.yticks([0, 5**2 / (4*4), 5**2 / (4*2)], fontsize=18)
    plt.grid()
    plt.legend(fontsize=18)
    #plt.gcf().set_size_inches(10,8)
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
    current, resistance, power = [float(k) for k in read.decode('ascii').split(";")]
    print("I = {} mA    -    R = {} kohm    -    P = {} mW".format(current, resistance, power))
    x.append(resistance)
    y.append(power)
    # make plot
    drawnow(power_locus)