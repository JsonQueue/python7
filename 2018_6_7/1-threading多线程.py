# threading 线程内置包
# Process 进程内置包
from multiprocessing import Process
import threading
import time

# 什么是线程 ?
# 线程就是操作系统中能够进行运算的最小单位,被包含在进程当中的,线程是进程的实际操作单位

def download(name,seconds):

    print('正在下载:{} '.format(name))
    # 休眠  模拟下载的过程
    time.sleep(seconds)
    print('{} 下载完成,消耗{}秒'.format(name,seconds))

# 开了三个分线程执行任务
# t1 = threading.Thread(target=download,args=('葫芦娃',3))
# t2 = threading.Thread(target=download,args=('变形金刚',6))
# t3 = threading.Thread(target=download,args=('西游记',5))
# start_time = time.time()
# 启动线程
# t1.start()
# t2.start()
# t3.start()
# 必须等待所有的分线程执行完成之后,再继续执行主线程
# t1.join() # 添加阻塞  等待分线程中的内容执行完成后继续执行主线程内容
# t2.join()
# t3.join()
# print('下载完成,共消耗{}秒'.format(time.time()-start_time))
# 1.比较耗时的任务可以使用分线程去做
# 2.同时进行多个任务,可以开启多个分线程
# 同步 异步  阻塞  非阻塞


# 自定义线程类
class MyThread(threading.Thread):
    def __init__(self,m_name,s):
        # 重载父类的初始化函数
        super(MyThread, self).__init__()
        self.m_name = m_name
        self.s = s
    def run(self):
        # 当线程启动的时候,会自动调用执行这个run函数
        # threading.current_thread() 获取当前所在线程信息
        print('开始下载:{},当前线程:{}'.format(self.m_name,threading.current_thread()))
        time.sleep(self.s)
        print('{} 下载完成,耗时{}秒'.format(self.m_name,self.s))
        
if __name__ == '__main__':
    
    t1 = MyThread('葫芦娃-大娃',3)
    t1.name = '下载大娃的线程'
    t2 = MyThread('葫芦娃-二娃',5)
    t3 = MyThread('葫芦娃-三娃',7)
    start_time = time.time()
    t1.start()
    t2.start()
    t3.start()
    print('当前活跃线程数:{}'.format(threading.active_count()))
    t1.join()
    t2.join()
    t3.join()
    print('全部下载完成,共消耗:{}秒'.format(time.time() - start_time))
    print('当前活跃线程数:{}'.format(threading.active_count()))
    
    



    





