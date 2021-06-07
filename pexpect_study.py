#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
发送：
sendline() 和 send() 唯一的区别就是在发送的字符串后面加上了回车换行符
sendcontrol() - 发送控制信号
sendeof() - 发送 EOF 信号
sendintr() - 发送终止信号，向子程序发送 SIGINT 信号，相当于 Linux 中的 kill 2 ，它会直接终止掉子进程。

交互：
# interact() 表示将控制权限交给用户（或者说标准输入）。一般情况下 pexpect 会接管所有的输入和输出，但有的时候还是希望用户介入，或者仅仅是为了完成一部分工作的时候， interact() 就很有用了。

读取：
next() - 返回下一行内容
read() - 返回剩下的所有内容，read() 的使用很不同，它期待一个 EOF 信号，然后将直到这个信号之前的所有输出全部返回，就像读一个文件那样。
readline() - 返回一行输出
readlines() - 返回列表模式的所有输出

当 expect() 过程匹配到关键字（或者说正则表达式）之后，系统会自动给3个变量赋值，分别是 before, after 和 match
process.before - 保存了到匹配到关键字为止，缓存里面已有的所有数据。也就是说如果缓存里缓存了 100 个字符的时候终于匹配到了关键字，那么 before 就是除了匹配到的关键字之外的所有字符
process.after - 保存匹配到的关键字，比如你在 expect 里面使用了正则表达式，那么表达式匹配到的所有字符都在 after 里面
process.match - 保存的是匹配到的正则表达式的实例，和上面的 after 相比一个是匹配到的字符串，一个是匹配到的正则表达式实例
如果 expect() 过程中发生错误，那么 before 保存到目前位置缓存里的所有数据， after 和 match 都是 None
"""

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