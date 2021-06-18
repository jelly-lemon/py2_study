#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.cElementTree as ET

str_xml = """<note>
<to>George</to>
<from>John</from>
<heading>Reminder</heading>
<body>Don't forget the meeting!</body>
</note>"""


def test_0():
    """
    字符串转 XML 对象
    """
    # 如果转换失败，会报异常
    root = ET.fromstring(str_xml)


def test_1():
    """
    xml 对象转 str
    :return:
    """
    root = ET.fromstring(str_xml)
    s = ET.tostring(root)
    print s


if __name__ == '__main__':
    test_1()
