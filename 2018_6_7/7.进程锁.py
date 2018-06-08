from multiprocessing import Process,Lock
import time
# 进程锁,防止数据出现混乱的情况
def func(l,num):
    l.acquire() # 资源上锁
    print('这是第{}个进程'.format(num))
    time.sleep(1)
    l.release() # 资源解锁
    
if __name__ == '__main__':
    lock = Lock()
    
    for x in range(10):
        p = Process(target=func,args=(lock,x))
        p.start()
        


    