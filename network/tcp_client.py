import socket

ADDRESS = 'localhost'
PORT = 9999

# Establish a connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ADDRESS, PORT))

# Use try-finally block to properly close sockets
try:
    while True:
        l = s.recv(16)

        print l
        if not l:
            print 'no data'
            break

        dat = s.recv(int(l))

        print dat
finally:
    s.send('exit')
    s.close()
