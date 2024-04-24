from RPiSim import GPIO
import time
import traceback

def RPiSim():
    GPIO.setmode(GPIO.BCM)
    
    GPIO.setwarnings(False)