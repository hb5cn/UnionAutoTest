# !/usr/local/python
# -*- coding: UTF-8 -*-
import socket


class SocketMain(object):
    def __init__(self):
        pass

    def bindsocket(self):
        print(socket.gethostbyname(socket.getfqdn(socket.gethostname())))


if __name__ == '__main__':
    a = SocketMain()
    a.bindsocket()
