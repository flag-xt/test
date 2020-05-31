#wraps 原本返回内部函数的属性，加上之后返回原函数的属性

from functools import wraps

def outer_func(fun):
    @wraps(fun)
    def inner_func(fun):
        '''innner_func的doc'''
        fun()
    return inner_func


@outer_func
def test():
    '''test的doc'''
    print('hello world')

print(test.__name__)
print(test.__doc__)