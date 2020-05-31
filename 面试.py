#列出 5 个常用 Python 标准库？
import os ,math,time,sys,re


#当前时刻延时两天
from datetime import datetime,timedelta

n=datetime.now()
d=timedelta(2)
print('过期时间:',n+d)

#Python的内建数据类型有哪些?
#str int bool list tuple dict


#一行代码实现1--100之和 python2 range返回的是迭代器，python3返回的是列表
print(sum(range(101)))


#字典如何删除键和合并两个字典
dic1={'a':97,'b':98}
dic2={'c':99,'d':100}
dic1.pop('a')
del dic2['d']
print(dic1)
print(dic2)
dic1.update(dic2)
print(dic1)


#简述 with 方法打开处理文件帮我我们做了什么？
'''
with方法不论文件运行遇到什么样的异常都能保证必要的‘清理操作’，调用__exit__方法释放资源
'''


#Python的可变和不可变数据类型？
'''
可变类型:list dict set
不可变类型:int str tuple
'''

#谈下python的GIL
'''
全局解释器锁，一个进程中有多个线程时，当一个线程运行时会霸占python解释器，
只有此线程运行结束后，其他线程才能运行，如果一个线程运行时间过长，解释器锁
自动解开，让其他线程运行，所以python中的多线程是伪多线程，要想提高运行速度
可以使用多进程，但那样会消耗资源
'''

#不可变类型 无论深复制还是浅复制都只是把原有地址复制过去
#可变数据类型 无论是深复制还是浅复制 都是开辟新内存把数据复制过去。
# 1、可变数据类型浅复制时只复制第一层的地址，如果里面还有可变数据类型，当复制的数据修改内层地址，原数据也被修改
# 2、可变数据类型深复制时把原数据全复制，当复制的数据修改内层地址，原数据不被修改

import copy

# a='123'
# a1=copy.copy(a)
# a2=copy.deepcopy(a)
# print(id(a))
# print(id(a1))
# print(id(a2))

b=[1,2,3,[1,2]]
b1=copy.copy(b)
b2=copy.deepcopy(b)
print(id(b))
print(id(b1))
print(id(b2))
b2[3][0]=4
print(b)
print(b2)


#单例模式 当对象被第一次调用时，实例被创建，当对象再次被调用时，返回第一次创建的实例
#__new__(cls)是object被调用时创建实例self用的

class A:
    __pol=None
    def __new__(cls, *args, **kwargs):
        if cls.__pol==None:
            cls.__pol=object.__new__(cls)
        return cls.__pol

a=A()
b=A()
print(id(a))
print(id(b))


#[[1,2],[3,4],[5,6]]一行代码展开该列表，得出[1,2,3,4,5,6]
a=[[1,2],[3,4],[5,6]]
b=[j for i in a for j in i]
print(b)


#funcs(*args,**kwargs)
'''
*args和kwargs合在一起通常被叫做万能参数，*args表示把可变数量的参数列表
传递给函数，**kwargs表示把不定长度的键值对传递给函数

'''


#一句话解释什么样的语言能够用装饰器?
'''
函数作为参数传递的语言，可以使用装饰器
@test   demo=test(demo)
def demo():
    pass

def test(func):
    def inner_fun():
        func()
    return inner_fun 

闭包三要素：
1、需要有内部函数和外部函数
2、外部函数返回内部函数名
3、内部函数使用外部函数的参数
'''


#简述面向对象中__new__和__init__区别
'''
__init__在对象创建时自动调用，可接收参数，不需要有返回值

__new__
1、至少有一个参数cls
2、必须有返回值，返回实例化的实例
'''

#以单个下划线开头的变量或方法仅供内部使用。
'''
双下划线前缀会导致Python解释器重写属性名称，以避免子类中的命名冲突。
当使用 from my_module import * 导入时，单下划线开头的变量和方法是不会被导入的。
但使用 import my_module 导入的话，仍然可以用 my_module._var 这样的形式访问属性或方法。
class A:
    _init_set=None
    __fol=1

class B(A):
    __fol = 2

a=A()
b=A()
c=B()
print(dir(a))
print(dir(b))
print(dir(c))
'''


#哪些不能作为字典的健
'''
字典中的键是不可变类型，可变类型list和dict不能作为字典键 一个对象能不能作为字典的key，就取决于其有没有__hash__方法
'''


#如何交换字典 {"A"：1,"B"：2}的键和值？
a={"A":1,"B":2}
b={v:k for k,v in a.items()}
print(b)


#python 字典和 json 字符串相互转化方法
import json

json.load(str)#字符串转化为字典
json.dump(dict)#字典转化为字符串


#举例 sort 和 sorted 的区别
'''
sort方法无返回值 a.sort(reversed=False)默认升序 
sorted方法有返回值  sorted(a)

a={'sonme':5,'a':54,'d':99,'c':97}
b=sorted(a.items(),key=lambda i : i[0])
print(b)
'''


#将字符串未出现在26个字母中的返回出小写，原字符串不分大小写
'''
def get_missing_letter(s):
    items = 'abcdefghijklmnopqrstuvwxyz'
    items=[i for i in items]
    s=s.lower()
    s = [i for i in s]
    for i in s:
        if i in items:
            items.remove(i)
    return ''.join(items)

s1 = set("abcdefghijklmnopqrstuvwxyz")
s2=set("A quick brown for jumps over the lazy dog")
ret="".join(sorted(s1-s2))
print(ret)
'''

##统计一段字符串中字符出现的次数
from collections import Counter
s='sghjksfuheiaefwiocvxmnb'
dic=Counter(s)
print(dict(dic))

#写一个函数找出一个整数数组中，第二大的数
a=[2,342,654,432,6754,3214]

def fn(a):
    max_first=max(a)
    a.remove(max_first)
    max_second=max(a)
    return max_second

print(fn(a))

#@wraps用法  test.__name__指向的是闭包内部函数名，使用@wraps后是本身的函数名
from functools import wraps
def fun(func):
    @wraps(func)
    def inner_fun(*args,**kwargs):
        '''inner_fun的doc'''
        print(func.__name__)
        func()
    return inner_fun

@fun
def test():
    '''test的doc'''
    print('hello world')

print(test.__name__)
print(test.__doc__)

#偏函数  xx
from functools import wraps,partial

test=partial(int,base=2)
print(test('100'))

#map()函数返回的是一个迭代器
def func(n):
    return n*n

a=[1,2,3,4,5]
d=map(func,a)
for i in d:
    print(i)

#filter()函数返回的是迭代器
a=filter(lambda x:x>5,[1,2,3,5,6,7,8,9,0])
for i in a:
    print(i,end='\t')

#reduce()函数的作用就是迭代求和
from functools import reduce

a=[1,2,3,4,5]
print(reduce(lambda x,y:x+y,a))
b=(6,7,8,9)
print(sum(b))































































