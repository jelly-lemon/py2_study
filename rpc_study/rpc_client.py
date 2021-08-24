#encoding:utf-8

import xmlrpclib


def test_0():
    """
    RPC 客户端
    """
    server = xmlrpclib.ServerProxy("http://localhost:8088")

    words = server.sayHello()

    print "result:" + words

if __name__ == '__main__':
    test_0()