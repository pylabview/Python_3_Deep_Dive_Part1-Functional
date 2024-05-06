import serial
import time

class PowerSupply:
    def __init__(self, 
                port,
                model, 
                boudrate=9600,
                timeout = 1):
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.serial_connection = None
        self.model = model
        self.connect()

    def connect(self):
        try:
            self.serial_connection = serial.Serial(
                                        port = self.port,
                                        baudrate = self.baudrate,
                                        timeout = self.timeout)
            print(f'PS Model ({self.model}) connected!')
        except serial.SerialException as e:
            print(f'Failed to connect: {e}')


    def disconnect(self):
        if self.serial_connection:
            self.serial_connection.close()
            print(f"PS {self.model} disconnected")

    def set_voltage(self, value):
        if self.serial_connection:            
            command = f'VOLT {value}\r\n'    
            try:
                self.serial_connection.write(command.encode())
                print(f'Voltage value {value} was set!')
            except serial.SerialException as e:
                print(f"Voltage value {value}V can't be set, check manual: {e}")

    def set_current(self, value):
        if self.serial_connection:
            command = f'CURR {value}\r\n'
            try:
                self.serial_connection.write(command.encode())
                print(f'Current {value}A was set!!')
            except serial.SerialException as e:
                print(f"Current {value}A can't be set, check manual: {e}")

    def enable_output(self):
        if self.serial_connection:
            command = f'OUTP ON\r\n'
            try:
                self.serial_connection.write(command.encode())
                print(f'OUTPUT is ENABLED')
            except serial.SerialException as e:
                print(f"PS cannot be ENABLED; {e}")
                
    def disable_output(self):
        if self.serial_connection:
            command = f'OUTP OFF\r\n'
            try:
                self.serial_connection.write(command.encode())
                print(f'OUTPut is DISABLED!')
            except serial.serialException as e:
                print(f"OUTPut can't be DISABLE: {e}")

    def read_voltage(self):
        if self.serial_connection:
            command = f'MEAS:VOLT?\r\n'
            try:
                self.serial_connection.write(command.encode())
                voltage = self.serial_connection.readline().strip()
                print(f'VOLTAGE set to: {voltage}')    
            except serial.SerialException as e:
                print("VOLT can't be read: {e}")

    def read_current(self):
        if self.serial_connection:
            command = f'MEAS:CURR?\r\n'
            try:
                self.serial_connection.write(command.encode())
                voltage = self.serial_connection.readline().strip()
                print(f'CURRENT set to: {voltage}')    
            except serial.SerialException as e:
                print("CURRENT can't be read: {e}")

    def close(self):
        if self.serial_connection:
            self.serial_connection.close()



if __name__ == "__main__":
    pass
                                        
