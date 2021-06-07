#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
%(name)s 记录器的名称
%(levelno)s：打印日志级别的数值
%(levelname)s：打印日志级别的名称
%(pathname)s：打印当前执行程序的路径，其实就是sys.argv[0]
%(filename)s：打印当前执行程序名
%(funcName)s：打印日志的当前函数
%(lineno)d：打印日志的当前行号
%(asctime)s：打印日志的时间
%(thread)d：打印线程ID
%(threadName)s：打印线程名称
%(process)d：打印进程ID
%(message)s：打印日志信息
"""


import logging


def test_1():
    # level 设置为 logging.INFO 时，就不会显示 DEBUG 级别的日志
    # 只有设置为 logging.DEBUG 时才会显示
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s (L:%(lineno)d, d:%(thread)d)- %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)

    logger.info("Start print log")
    logger.debug("Do something")
    logger.warning("Something maybe fail.")
    logger.info("Finish")


if __name__ == '__main__':
    test_1()