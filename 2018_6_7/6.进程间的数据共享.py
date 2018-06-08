from multiprocessing import Process,Manager
'''
Manager可以用来实现进程中的数据共享,manager会通过一个进程,来使其他的进程通过代理的方式操作python对象的
'''
def func(dic,li):
    dic['age'] = 20
    dic['name'] = '张三'
    li.append(1)
if __name__ == '__main__':
    # 创建manager对象
    manager = Manager()
    list_2 = ['你好','我不好']
    # 支持dict/list/Lock/RLOCK/Semaphore/Queue/Event
    dic = manager.dict()
    # 根据主进程中的列表,创建manager管理的列表
    list_1 = manager.list(list_2)
    # 创建10个进程
    for x in range(10):
        p = Process(target=func,args=(dic,list_1))
        p.start()
        p.join()
    print(dic)
    print(list_1)
    




