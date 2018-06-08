from greenlet import greenlet
from threading import Thread,BoundedSemaphore
import requests

def run(x,url):
    semaphore.acquire()
    print('任务{}  下载{}'.format(x,url))
    g1 = greenlet(send_req)
    g2 = greenlet(process_rsp)
    g3 = greenlet(save_data)
    g1.switch(url,g2,g3)
    semaphore.release()
def send_req(url,g2,g3):
    response = requests.get(url)
    g2.switch(response,g3)
    
    
def process_rsp(response,g3):
    print('请求{}成功,开始进行解析数据'.format(response.url))
    print('正在解析数据..请稍后.....')
    data = '这是解析好的数据'
    g3.switch(data)
    
def save_data(data):
    print('数据解析完成,正在保存数据....')
    print(data)


    
if __name__ == '__main__':
    url_list = ['http://www.baidu.com','http://www.taobao.com','http://www.zhihu.com','http://www.zhiyou.com','http://www.vip.com']
    semaphore = BoundedSemaphore(3)
    for x in range(len(url_list)):
        th = Thread(target=run,args=(x,url_list[x]))
        th.start()
        th.join()














