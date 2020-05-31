def insert_sort(list):
  Length=len(list)
  for i in range(1,Length):                   #默认第一个元素已经在有序序列中，从后面元素开始插入
      for j in range(i,0,-1):                 #逆向遍历比较，交换位置实现插入
          if list[j] < list[j-1]:  
              list[j],list[j-1] = list[j-1],list[j]
  return list

a=[10,1,35,61,89,36,55]
print('after sort:',insert_sort(a))
