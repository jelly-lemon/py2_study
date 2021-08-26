#encoding:utf-8


def test_0():
    """
    获取带转义字符的输入

    s = input()

    如果输入：abc\r\nabc，会报错：
    unexpected character after line continuation character

    s = raw_input()
    输入：abc\r\nabc
    print s 会出现：abc\r\nabc
    很明显 \r\n 给我变成了 \\r\\n
    我期望我输入 abc\r\nabc 后输出：
    abc
    abc
    """
    s = raw_input()
    s = s.replace("\\r\\n", "\r\n")
    print s

if __name__ == '__main__':
    test_0()