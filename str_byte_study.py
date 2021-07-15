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


if __name__ == '__main__':
    test_2()
