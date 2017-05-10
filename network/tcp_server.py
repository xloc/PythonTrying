# coding=utf-8
import socket
import string
import threading

import random

import time


def tcp_link(sock, addr):
    print 'Accept new connection from %s:%s...' % addr

    # Receive message from a socket
    for i in range(10):
        r_str = ''.join(random.sample(
            string.ascii_letters, random.randint(10, 60))
        )

        sock.send(str(len(r_str)).ljust(16))
        sock.send(r_str)

        time.sleep(0.5)

    sock.close()
    print 'Connection from %s:%s closed.' % addr


# Create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 9999))
s.listen(1)

# Service Loop
while True:
    # Accept a new connection
    sock, addr = s.accept()

    # Use a new daemon thread to handle the connection
    t = threading.Thread(target=tcp_link, args=(sock, addr))
    t.setDaemon(True)
    t.start()