from Adafruit_I2C import Adafruit_I2C
import numpy as np
import time
import threading

freq = 5

class DAC:
    
    RESOLUTION = 2**12 - 1
    WRITE_REGISTER = 0x40

    # Set the address to the default
    def __init__(self, address=0x60):
        self.i2c = Adafruit_I2C(address)
        
    # Send the voltage in two bytes
    def send_voltage(self, bits):
        bytes = [(bits >> 4) & 0xFF, (bits << 4) & 0xFF]
        self.i2c.writeList(self.WRITE_REGISTER, bytes)

    # Limit the max and min voltage that can be set
    # and convert to the resolution of the dac
    def set_voltage(self, voltage):
        if voltage > 100:
            voltage = 100
        elif voltage < 0:
            voltage = 0

        bits = int(voltage/100. * self.RESOLUTION)
        self.send_voltage(bits)

def user_input():
    global freq
    while True:
        try:
            freq = int(raw_input("Enter frequency : "))
        except:
            print "Please enter a valid integer"
            freq = 5
        
        

def test_run():
    dac = DAC()
    # sin(t*f*2*pi) w\ f = frequency
    sig = lambda t: 50*np.sin(t*freq*2*np.pi) + 50
    start_time = time.time()

    while True:
    #print "exec"
        dac.set_voltage(sig(time.time()-start_time))

if __name__ == "__main__":
    userI = threading.Thread(target=user_input, args=())
    userI.start()
    test_run()
