
'''进程池节省了进程创建和销毁所用的时间'''
from multiprocessing import Pool

p=Pool(5)
p.apply_async()#异步阻塞 callback返回值
p.close()#关闭进程池
p.join()#等待进程池的关闭


