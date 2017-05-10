import collections

import io

# data = None
# with open('./g.data') as f:
#     data = f.read()

# print collections.Counter(data)
#
# # print len(data)
# # for i, c in enumerate(data):
# #     if not i % 11:
# #         print
# #     print hex(ord(c))[-2:],
#
# splited = data.split(b'\x55\x51')
# print len(splited)
#
# charcount = [len(sli) for sli in splited]
# print collections.Counter(charcount)

def ph(s):
    print ' '.join([hex(ord(c))[-2:] for c in s])
if __name__ == '__main__':

    stm = io.open('./g.data', 'rb')
    while stm.readable():

        d = stm.read(11)
        # print ' '.join([hex(ord(c))[-2:] for c in d])

        # Find first 0x55 which is the frame head
        idx55 = d.find('\x55')
        if idx55 != -1:
            # print idx55
            # print stm.tell()
            stm.seek(idx55-11, io.SEEK_CUR)

            d = stm.read(11)
            # print ' '.join([hex(ord(c))[-2:] for c in d])
            # print ph(d[1])

            # Check sum
            s = sum([ord(c) for c in d[0:10]])
            # print ph(chr(s & 0xff))
            if s & 0xff == ord(d[10]):
                # Extract angle of yaw
                # print ph(d)
                if d[1] == '\x53':
                    # print ph(d)
                    yaw = ord(d[7]) << 8 | ord(d[6])
                    yaw = yaw / 32768.0 * 180
                    print yaw

            # break

    stm.close()

def parse(stm):
    try:
        while stm.readable():

            d = stm.read(11)
            # print ' '.join([hex(ord(c))[-2:] for c in d])

            # Find first 0x55 which is the frame head
            idx55 = d.find('\x55')
            if idx55 != -1:
                # print idx55
                d = d[idx55:]+stm.read(idx55)

                # print ' '.join([hex(ord(c))[-2:] for c in d])
                # print ph(d[1])

                # Check sum
                s = sum([ord(c) for c in d[0:10]])
                # print ph(chr(s & 0xff))
                if s & 0xff == ord(d[10]):
                    # Extract angle of yaw
                    # print ph(d)
                    if d[1] == '\x53':
                        # print ph(d)
                        yaw = ord(d[7]) << 8 | ord(d[6])
                        yaw = yaw / 32768.0 * 180
                        print '\r', yaw,

                # break
    except KeyboardInterrupt:
        stm.close()


