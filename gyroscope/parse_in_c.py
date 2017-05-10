import serial
import time


def ph(s):
    print ' '.join([hex(ord(c))[-2:] for c in s])

s = serial.Serial()
s.port = '/dev/tty.usbmodem1412'
s.baudrate = 9600
s.open()

time.sleep(0.01)
print s.read(11)


