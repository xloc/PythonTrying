import serial

# import serial.tools.list_ports as list_ports
# import time
#
# ports = [port.device for port in list_ports.grep(r'usbmodem')]
# assert len(ports) == 1
# mbed = ports[0]
import time

# s = serial.Serial('/dev/tty.usbmodem1422', baudrate=115200)
# print s

# time.sleep(1)
# s.flushOutput()
# s.flushInput()
# s.write('1')
# time.sleep(0.01)
# print s.read(1)

# print 'Start'
# s.write(b'hello\n'*10)
# s.flush()
# print 'Written'
# print repr(s.read(8))
# print 'Done'
#
# time.sleep(0.01)
#
# print s.read(8),

# s.write('hello\n')
# s.flush()
#
# s.readline()

s = serial.Serial()
s.port = '/dev/tty.usbmodem1412'
s.baudrate = 9600
s.open()

import parse_data as p

# print p.ph(s.read(100))

#
p.parse(s)





