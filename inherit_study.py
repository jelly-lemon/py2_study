#encoding: utf-8

class A:
    # 在函数外定义的变量是静态变量
    count = 0

    def __init__(self, name, age):
        print "A init"
        self.name = name
        self.age = age

    def sayHello(self):
        print "A: hello"

class B:
    def __init__(self, brand):
        print "B init"
        self.brand = brand

    def get_brand(self):
        return self.brand

class C(B, A):
    """
    多继承时，如果不写构造函数，那么有一个默认构造函数，
    传递的参数是第一个父类的参数。不会调用第二个父类的构造函数。
    """
    pass

class D(A, B):
    """
    单继承时：初始化父类：super(xxx,self)._ _init _ _(*args)
    多继承时，通过：父类._ _ init _ _(*args)来初始化父类的属性
    """
    def __init__(self):
        A.__init__(self, "tim cook", 50)
        B.__init__(self, "apple")

def test_0():
    """
    访问类属性
    """
    print A.count

def test_1():
    c1 = C("")
    print c1.get_brand()
    c1.sayHello()



if __name__ == '__main__':
    test_1()