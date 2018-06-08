from multiprocessing import Pool
import requests

def send_req(idx,url):
    print('任务{},请求访问:{}'.format(idx,url))
    response =  requests.get(url)
    return {'idx':idx,'response':response}
def process_response(args):
    print('任务{},下载内容:{}'.format(args.get('idx'),args.get('response')))
if __name__ == '__main__':
    pool = Pool(5)
    url_list = ['http://www.baidu.com','http://www.zhiyou100.com','http://www.zhiyou100.com:1888','http://www.taobao.com','http://www.meituan.com','http://www.alipay.com','http://www.vip.com','http://www.baidu.com','http://www.baidu.com']
    for x in range(len(url_list)):
        pool.apply_async(func=send_req,args=(x,url_list[x]),callback=process_response)
    pool.close()
    pool.join()
