import os
import time
from multiprocessing import Pool

def task(n):
    print('{} is running'.format(os.getpid()))
    time.sleep(2)
    print('{} is done'.format(os.getpid()))
    return n**2

if __name__ == '__main__':
    # print(os.cpu_count())  #查看cpu个数
    ret_lis = []
    p = Pool(4) # 最大四个进程
    for i in range(1,7): # 开7个任务
        ret = p.apply_async(task,args=(i,))  # 异步的，一个运行完才执行另一个
        ret_lis.append(ret)
    p.close() # 禁止往进程池内在添加任务
    p.join() # 等待进程池
    # print('主进程')
    print(_.get() for _ in ret_lis)