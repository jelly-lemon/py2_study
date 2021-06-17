#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pexpect

def test_1():
    # spawn() 方法用来执行一个程序，它返回这个程序的操作句柄，以后可以通过操作这个句柄来对这个程序进行操作
    # 程序被启动之后会有输出，我们也会在脚本中检查输出中的关键字是否是已知并处理的，如果指定时间内没找到程序就会出错返回。
    process = pexpect.spawn('ftp sw-tftp', timeout=60)

    # pattern_list      正则表达式列表，表示要匹配这些内容
    # timeout           不设置或者设置为-1的话，超时时间就采用self.timeout的值，默认是30秒。也可以自己设置。
    # searchwindowsize  默认情况下是 None，也就是每从子进程中获取一个字符就做一次完整匹配，如果子进程的输出很多的话……性能会非常低。
    pattern_list = ['Permission Denied', 'Terminal type', 'ftp>', ]
    index = process.expect(pattern_list, timeout=-1, searchwindowsize=None)

    # 上面的关键字一旦匹配，就会返回0表示匹配成功，但是如果一直匹配不到呢？默认是会一直等下去，但是如果设置了 timeout 的话就会超时。
    if index == 0:
        print "Permission denied at host, can't login."
        process.kill(0)
    elif index == 1:
        print "Login ok, set up terminal type…"
        process.sendline('vty100')
        process.expect("ftp>")
    elif index == 2:
        print "Login Ok, please send your command"
        process.interact()



if __name__ == '__main__':
    test_1()