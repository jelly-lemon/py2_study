# encoding=utf-8
import json


def test_1():
    """
    字符串查找
    """
    s = u"绿盟%code%"
    if s.find(u"code") != -1:
        print "yes"

def test_2():
    """
    在 python2 中，str 就是 python3 中的 byte
    unicode 就是 python3 中的 str
    """
    b = "你好"
    print type(b)

    s = b.decode("utf-8")
    print type(s)


def test_3():
    """
    字符串替换
    """
    s = u"name=%name%"
    s = s.replace(u"%name%", u"绿盟")
    print s

def test_4():
    """
    解释器遇到 \r 时，在字节串中会替换 \r 为对应的数值。
    """
    s1 = "hello\r\nworld"
    print s1
    print len(s1)

    s2 = """hello
world"""

    print s2

def test_5():
    """
    字节串替换
    """
    s1 = "hello\\r\\nworld\\r\\n"
    # 默认全部替换
    s1 = s1.replace('\\r', "\r")
    print s1

def test_6():

    s1 = input()
    print s1


if __name__ == '__main__':
    test_5()
