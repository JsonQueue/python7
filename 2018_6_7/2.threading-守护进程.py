import threading
import time

'''
把子线程变成主线程中的守护线程,当主线程结束后,子线程也会随之结束,一旦主线程代码执行完毕,程序就结束了

如果没有添加守护线程,当主线程执行完毕之后,会等待子线程中的任务执行完成之后,再退出程序
'''
def run(num):
    # 在子线程中执行这个任务
    print('任务:{}'.format(num))
    if num == 1:
        time.sleep(10)
    else:
        time.sleep(1)
    print('任务:{},已完成!'.format(num))

# 创建5个分线程
for x in range(3):
    # 原子性  银行转账
    thd = threading.Thread(target=run,args=(x,))
    # 把子线程添加到守护进程中,必须在start之前完成
    if x == 1:
        thd.setDaemon(True)
    thd.start()
    # thd.join()

# print('线程活跃个数:{}'.format(threading.active_count()))
time.sleep(0.5)
print('线程活跃个数:{}'.format(threading.active_count()))