#!/usr/bin/env python
# -*- coding: utf-8 -*-

from a import say_hello


# 在 b 中间导入 a 文件中的任何函数，都会执行一遍 a
say_hello()