import pyvisa
import serial
import time


class PowerSupply:
    def __init__(self, 
                address=None, 
                port = None,
                baudrate = 9600,
                timeout = 1):
        if address:
            self.addres = address
            self.rm = pyvisa.ResourceManager('@py')
        else:
            self.port = port
            self.timeout = timeout
            self.dev_instance = None
            self.connect()


    def connect(self):
        if self.dev_instance:
            try:
                if address:
                    self.dev_instance = self.rm.open_resources(self.address)
                    print(f'{self.address} is connected')
                else:
                    self.dev_instance = serial.Serial( port = self.port,
                                                       baudrate = self.baudrate,
                                                       timeout = self.timeout)
                    print(f'{self.port} is connected!')
            except:
                print(f'An error occured connecting') 

        else:
            print(f'Connection is already open!')                                                   




if __name__ == "__main__":
    time.sleep(2)
