#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
section不能重复，里面数据通过section去查找，
每个seletion下可以有多个key和vlaue的键值对，
注释用英文分号(;)
"""

from ConfigParser import *


def test_0():
    """
    读取 config
    """
    # 创建管理对象
    conf = ConfigParser()

    # 读ini文件
    conf.read("./jit.ini")

    name = conf.get("system", "name") # 不存在该配置则会报错
    ip = conf.get("system", "ip")
    print ip

    # 获取所有的section
    sections = conf.sections()

    print sections

    # 获取 section 下的所有键值对
    items = conf.items("system")    # [('ip', '192.168.1.1'), ('port', '80')]
    print items

    # 转为字典
    config = {}
    for item in items:
        config[item[0]] = item[1]

    print config

def test_1():
    """
    修改配置文件
    """
    # 修改并保存
    conf = ConfigParser()
    conf.read("./jit.ini")
    conf.add_section("system")
    conf.set("system", "ip", "127.0.0.1")

    # 添加 section
    # conf.add_section("hello")

    # 设置参数
    # conf.set("test", "name", "goodman") # 没有该 section 会报错

    # 判断是否存在 section
    print conf.has_section("hello")

    # 写入文件
    with open("jit.ini", "w+") as f:
        conf.write(f)



if __name__ == '__main__':
    test_1()