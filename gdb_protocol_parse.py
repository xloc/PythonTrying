import time

import serial


PORT_REGEX = 'cu'


def get_port(port_regex):
    import serial.tools.list_ports as lp

    devs = [p for p in lp.grep(port_regex)]
    sport = None

    if len(devs) == 0:
        raise Exception('None of serial port satisfy condition')
    elif len(devs) == 1:
        sport = devs[0]
    else:
        for i, p in enumerate(lp.comports()):
            print '[{}]\t{}'.format(i, p)

        idx = raw_input('Choose one by index: ')
        sport = devs[int(idx)]

    print 'Chosen: ', sport.device

    return sport.device


def get_reply():
    reply = s.read_until('#') + s.read(2)
    start = reply.rfind('+$')
    if start != 0:
        # Some warning
        pass
    data = reply[start+2:-3]

    reply_sum = sum(map(ord, reply[start:-3])) & 0xff
    trans_sum = int(reply[-2:], base=16)
    return data if reply_sum == trans_sum else None


def send(data):
    cmd = '${}#{:0=2x}'.format(data, sum([ord(c) for c in '$'+data]) & 0xff)
    print cmd
    s.write(cmd)

    return get_reply()



port = get_port('usbmodem')
s = serial.Serial(port=port, baudrate=9600)

# try:
#     while True:
#         s.write('a')
#         print s.readline()[:-1]
#         time.sleep(0.2)
# except:
#     s.close()

print send('g')
