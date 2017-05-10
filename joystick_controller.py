import pygame.joystick as joys
import pygame as pg
import time

JOYSTICK_ID = 0


def trans(rvelo, rangle):
    limit = lambda x, low, up: sorted([up,x,low])[1]

    velo = -0.5 * rvelo
    angle = -30 * rangle - 2

    return velo, angle

import serial
s = serial.Serial('/dev/tty.MS2016-DevB', baudrate=38400)
'''
while True:
    try:
        (velocity, angle) = trans(0.3, -30)

        s.write("# %6.3f %7.3f\r\n" % (velocity, angle))

        time.sleep(0.05)

    except KeyboardInterrupt:
        break
'''

pg.init()
ctr = joys.Joystick(JOYSTICK_ID)
ctr.init()


done = False

while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True

    getval = ctr.get_axis
    (velocity, angle) = trans(getval(1), getval(2))

    s.write("# %6.3f %7.3f\r\n" % (velocity, angle))
    print '\r v = %6.3f a = %7.3f' % (velocity, angle),

    time.sleep(0.05)


# print joys.get_count()

# print ctr.get_init()

# print ctr.get_name()

# print 'Axes count\t\t = ', ctr.get_numaxes()
# print 'Trackball count\t = ', ctr.get_numballs()
# print 'Button count\t = ', ctr.get_numbuttons()
# print 'Hat count\t\t = ', ctr.get_numhats()




# import time
# for xid in range(ctr.get_numaxes()):
#     while True:
#         try:
#             print '\rAxis %d = %f' % (xid, ctr.get_axis(xid))
#             time.sleep(1)
#         except KeyboardInterrupt:
#             break

