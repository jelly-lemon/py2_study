# encoding:utf-8

"""
SimpleXMLRPCServer
    _marshaled_dispatch: Dispatches an XML-RPC method from marshalled (XML) data


server.register_function(adder_function,'add')##adder_function是服务点定义的函数，add是客户端调用时用的函数。
server.register_introspection_functions()##如果用到内部函数，需要把内部函数注册到服务端。
server.register_instance(MyFuncs())##如果要注册的是一个类，可以利用这个函数把类中的方法全部注册到server端。

"""

from SimpleXMLRPCServer import SimpleXMLRPCServer
from SocketServer import ThreadingMixIn


class MyRPCSeverFunctions:
    """
    把允许远程调用的函数封装到一个类里面
    """
    def sayHello(self):
        return "hello XMLRPC"


class ThreadXMLRPCServer(ThreadingMixIn, SimpleXMLRPCServer):
    """
    继承两个类 = 继承父类的 成员 + 函数
    """
    pass


def test_0():
    """
    SimpleXMLRPCServer 是一个单线程的服务器。
    这意味着，如果几个客户端同时发出多个请求，其它的请求就必须等待第一个请求完成以后才能继续。
    """
    print "SimpleXMLRPCServer"
    RPCFunctions = MyRPCSeverFunctions()
    server = SimpleXMLRPCServer(("localhost", 8088))
    server.register_instance(RPCFunctions)

    print "Listening on port 8088"
    server.serve_forever()


def test_1():
    """
    多线程 RPC 服务端
    """
    print "ThreadXMLRPCServer"
    RPCFunctions = MyRPCSeverFunctions()
    # TODO 继承了两个类，默认构造函数是什么？
    server = ThreadXMLRPCServer(('localhost', 8088), allow_none=True)
    server.register_instance(RPCFunctions)

    print "Listening on port 8088"
    server.serve_forever()


if __name__ == '__main__':
    test_1()
