#斐波那契数列特点 从第三项起后一项是前两项之和  前三项为1，1，2
#从第三项开始储存

#生成器方法
def fn(items):
    a,b,n=1,1,3
    while n<=items:
        a,b=b,a+b
        yield b
        n+=1
    return b

lis=[1,1]
for i in fn(10):
    lis.append(i)
print(lis)
print()
print('#####################################')
d=fn(10)
print(d.__next__())
print(d.__next__())
print(d.__next__())



#迭代器方法
def fn(n):
    if n==1 or n==2:
        return 1
    else:
        return fn(n-1)+fn(n-2)

print(fn(10))