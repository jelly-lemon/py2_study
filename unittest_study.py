# encoding:utf-8
"""
简单单元测试
"""
import unittest

def my_abs(n):
    if n < 0:
        return -n
    else:
        return n

# 单元测试类必须继承自 unittest.TestCase 类
class MyTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_my_abs(self):
        # 第一个参数是期望值，第二个参数是实际值
        self.assertEqual(10, my_abs(-10))

    def test_dict(self):
        d1 = {"name": '农夫山泉'}
        d2 = {}
        d2["name"] = "农夫山泉"
        self.assertEqual(d1, d2)


if __name__ == '__main__':
    # 运行所有测试用例
    unittest.main()
