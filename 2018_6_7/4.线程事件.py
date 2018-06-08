import threading
import time
'''
线程事件,主线程控制其他线程的执行
'''
# 红绿灯
# 创建事件对象
event  = threading.Event()

def light():
    # 记录时间
    count = 0
    # 设置默认值为绿灯
    event.set() # Flag修改为True
    while True:
        if 10 <count < 20:
            # 红灯状态
            event.clear() # Flag值修改为False
            print('现在是红灯..')
        elif count > 20:
            event.set() # Flag值修改为True
            count = 0
        else:
            print('现在是绿灯')
        # 休眠1秒
        time.sleep(1)
        # 秒数+1
        count += 1

# 控制车辆行驶
def car(name):
    
    while True:
        # 判断当前是红灯还是绿灯
        # is_set() 返回flag的值,True或False
        if event.is_set():
            print('{},可以通过当前路口..'.format(name))
            time.sleep(1)
        else:
            print('{},当前不可通过,请等待.....'.format(name))
            # 等待,会一直等到event.Flag值发生修改,再继续向下执行
            event.wait()
            print('{},现在是绿灯了,可以通过这个路口..'.format(name))

# 定时器
def excute():
    
    print('这句话将在2秒后输出')
if __name__ == '__main__':

    # light = threading.Thread(target=light)
    # light.start()
    #
    # car = threading.Thread(target=car,args=('【兰博基尼】',))
    # car.start()
    # Timer()定时器
    # 1.多少秒之后执行  2.执行的操作
    timer = threading.Timer(2,excute)
    timer.start()



















