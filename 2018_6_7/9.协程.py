'''
协程
协程可以认为是一个微线程,就是只有一个线程,对一个线程进行分解,在一个线程中规定某些任务执行的顺序

当有些任务不需要使用cpu操作时(IO),可以使用协程

greenlet 第三方包   pip install python-greenlet下载第三方包
gevent 在greenlet的基础 又封装了一次
'''
from greenlet import greenlet
import time
def test1():
    
    print('现在正在执行test1的第一个操作')
    # 从test1中跳转到test2中执行
    g2.switch()
    print('现在正在执行test1的第二个操作')
    g2.switch()
    print('任务执行完毕....')

def test2():
    print('现在正在执行test2的第一个操作')
    g1.switch()
    print('现在正在执行test2的第二个操作')
    g1.switch()
    
if __name__ == '__main__':
    # 指定协程执行的任务
    g1 = greenlet(test1)
    g2 = greenlet(test2)
    # 手动切换到g1去执行
    g1.switch()