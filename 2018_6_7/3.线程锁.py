'''
线程安全锁,用于锁定资源
'''
from threading import Lock,Thread,RLock,BoundedSemaphore
import time
import threading
num = 0

lock = Lock()

def f(n):
    # acqurie() 对资源进行加锁
    lock.acquire()
    global num
    num += 1
    print(n)
    # release() 释放资源 资源解锁
    lock.release()

# for x in range(200):
#
#     t = Thread(target=f,args=(x,))
#     t.start()
#     t.join()

# print('num的值为:{}'.format(num))


# RLock递归锁
# 用法和Lock用法一样,递归锁可以进行锁嵌套,
# rlock = RLock()

# 互斥锁只允许一个线程对资源进行修改  信号量允许一定量的线程对资源进行处理

def run(n):
    semaphore.acquire() # 资源加锁
    time.sleep(1)
    print('在第{}个线程中执行的操作......'.format(n))
    semaphore.release() # 资源解锁
    
num = 0
semaphore = BoundedSemaphore(3) # 最多允许三个线程同时运行

for x in range(20):
    t = Thread(target=run,args=(x,))
    t.start()

    
# 主线程阻塞
while threading.active_count() != 1:
    pass

print('任务执行完毕!')

    
    





