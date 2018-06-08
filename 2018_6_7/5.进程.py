# Process进程类
from multiprocessing import Process,Queue,Pipe
import os
# 什么是进程?
# 一个程序运行的实例就是一个进程,每一个进程都提供了程序运行所需要的一些资源
# 每一个进程都会产生一个线程,即主线程,在主线程中再创建一些子线程

# 进程之间的数据是不共享的,如果要进行数据通信可以通过Queue或Pipe
def func(q):
    q.put(['hello','world',2,0.2])
    # getpid() 进程id
    print('子进程id:{}'.format(os.getpid()))
    
def eat(coon):
    # 子进程中发送数据
    coon.send([56,None,'world'])
    print('主进程id:{}'.format(os.getpid()))
if __name__  == "__main__":
    # q = Queue()
    # # 主进程调用 函数
    # eat('在主进程中执行:')
    # # 创建子进程
    # p = Process(target=func,args=(q,))
    # p.start()
    # p.join()
    # Pipe() 返回两个进程链接
    # 父进程连接  子进程连接
    parent,child = Pipe()
    p = Process(target=eat,args=(child,))
    p.start()
    # 接收传过来的数据
    print(parent.recv())
    p.join()
