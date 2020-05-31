#__slot__限制实例属性（类成员属性不限制）
#__slot__限制实例方法（类方法不限制）
#不限制子类添加属性或方法

import types


class A:
    __slots__ = ('name','age')
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def only(self):
        pass

class B(A):
    pass


def test():
    print('hello world')

b=B('xt',25)
b.gender='男'
b.test=types.MethodType(test,b)