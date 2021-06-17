#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.cElementTree as ET

def test_0():
    """
    字符串转 XML 对象
    """
    # 如果转换失败，会报异常
    root = ET.fromstring("hello")


if __name__ == '__main__':
    test_0()