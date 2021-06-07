# encoding=utf-8
import json


def test_1():
    """
    字符串查找
    """
    s = u"绿盟%code%"
    if s.find(u"code") != -1:
        print "yes"





def test_3():
    """
    字符串替换
    """
    s = u"name=%name%"
    s = s.replace(u"%name%", u"绿盟")
    print s


if __name__ == '__main__':
    test_2()
