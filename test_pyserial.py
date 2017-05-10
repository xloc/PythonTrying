import serial

s = serial.Serial('/dev/tty.MS2016-DevB', baudrate=38400)

s.write('Hello World');