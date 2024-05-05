# The id function returns the memory address 
#Exmaple
import ctypes
import sys

class CountReference:
    def __init__(self, address):
        self.address = address
    
    @property
    def address(self):
        """The address property."""
        return self._address

    @address.setter
    def address(self, value: int):
        self._address = ctypes.c_long.from_address(value).value


a = 10
print(f'This is the address of a: {hex(id(a))}')

a = [1,2,3]

print(f'a memory address as int {id(a)}')

print(f'Get referece count using getrefcount: {sys.getrefcount(a)}')

a_mem = CountReference(id(a))

print(f'Count referece using ctypes {a_mem.address}')

# Lets assign b
b = a 
print(f' a memory address is the same as b {id(a) == id(b)}')
print(f"Let's get the reference count of a or b {CountReference(id(a)).address}")



