from multiprocessing import Process,Pool
import time
'''
进程的开启是需要消耗一定资源的,使用多进程的时候回消耗大量的内存功能,为了防止上面这种情况,使用进程池开启多进程

线程的开启占用的资源比较少,多线程只会导致cpu切换线程频繁时,导致系统变慢,卡顿等情况...
'''

def func(i):
    time.sleep(2)
    print('任务:{}'.format(i))
    return i
def cb(args):
    print('异步任务完成了...',args)
if __name__ == '__main__':
    # 创建进程池
    pool = Pool(5)  # 指定最多允许放入几个进程
    for x in range(10):
        # 进程池执行同步任务
        # 多进程的同步任务
        # 先下载  解压  执行
        # pool.apply(func=func,args=(x,))
        # 进程池执行异步任务
        # callback 回调函数,只有子进程任务执行完成之后,才会执行callback,否则就不会执行callback
        pool.apply_async(func=func, args=(x,), callback=cb)
        
        
    # 进程池任务执行结束后,关闭进程池
    pool.close()
    # 主进程等待子进程执行结束
    pool.join()

    




