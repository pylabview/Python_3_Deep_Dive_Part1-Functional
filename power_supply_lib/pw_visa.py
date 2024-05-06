import pyvisa
import time


class PowerSupplyVisa:
    def __init__(self, address):
        self.address = address
        self.rm = pyvisa.ResourcesManager('@py')
        self.instrument = None
        self.connect()


    def connect(self):
        try:
            self.instrument = self.rm.open_resource(self.address)            
            print("Connected!!")
        except pyvisa.VisaIOError as e:
            print(f'Failed to connect: {e}')


    def set_voltage(self, value):
        command = f'VOLT {value}'
        try:
            self.instrument.write(command)
            print(f'VOLTAGE was set to {value}V')
        except pyvisa.VisaIOError as e:
            print(f'Failed to set VOLTAGE {value}V: {e}')      

    def set_current(self, value):
        command = f'CURR {value}'
        try:
            self.instrument.write(command)
            print(f'CURRENT was set to {value}A')
        except pyvisa.VisaIOError as e:
            print(f'Failed to set CURRENT {value}V: {e}')
            
    def enable_output(self):
        command = f'OUTP ON'
        try:
            self.instrument.write(command)
            print(f'PS was ENABLED')
        except pyvisa.VisaIOError as e:
            print(f'PS Failed to ENABLED: {e}')
     
    def disable_output(self):
        command = f'OUTP OFF'
        try:
            self.instrument.write(command)
            print(f'PS was DISABLE')
        except pyvisa.VisaIOError as e:
            print(f'PS Failed to DISABLE: {e}')

    def close(self):
        if self.instrument:
            self.instrument.close()


if __name__ == "__main__":
    pass
