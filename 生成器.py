from collections import Iterable,Iterator
#列表、字典、字符串、元组、集合、列表具有迭代性，可不是迭代器，通过iter可将其变为生成器
lis=[1,2,3,4]
dic={'a':1}
st='1234'
tup=(1,2)
se={1,2,3}
lis=iter(lis)
print(isinstance(lis,Iterable))
print(isinstance(dic,Iterable))
print(isinstance(st,Iterable))
print(isinstance(tup,Iterable))
print(isinstance(se,Iterable))


print(isinstance(lis,Iterator))
print(isinstance(dic,Iterator))
print(isinstance(st,Iterator))
print(isinstance(tup,Iterator))
print(isinstance(se,Iterator))