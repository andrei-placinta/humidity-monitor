import serial															
import matplotlib.pyplot as plt
from drawnow import *
L1=[]
L2=[]
values = []
serialArduino=serial.Serial('com5',9600)
def plotValues():
    plt.title('Humidity sensor graph')
    plt.grid(True)
    plt.ylabel('VALUE!(Humidity sensor)')
    plt.plot(values, 'rx-', label='Humidity sensor=' +valueRead+'L1= '+L1+'L2= '+L2
             ,color='blue')
    plt.legend(loc='upper left')                                                            
    plt.xlabel('Time(s)')

for i in range(0,40):
    values.append(0)

while True:
    while(serialArduino.inWaiting()==0):
        pass
    valueRead,L1,L2=serialArduino.readline().decode('utf8').split(';')

    try:
        valueInInt=int(valueRead)
        print(valueInInt)
        if valueInInt <=1024:
            if valueInInt >=0:
                 values.append(valueInInt)
                 values.pop(0)
                 drawnow(plotValues)
            else:
                print("Negative number")
        else:
            print("The value received from Arduino is too high")
    except ValueError:
        print("The value cannot be parsed")
