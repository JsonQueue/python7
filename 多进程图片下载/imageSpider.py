import requests
import re
from bs4 import BeautifulSoup
import os
from lxml import etree
from multiprocessing import Process,Pool

INDEX_URL = 'http://www.ivsky.com/tupian/ziranfengguang/'


class ImageSpider(object):
    
    def __init__(self):
        self.base_url = 'http://www.ivsky.com/tupian/ziranfengguang/'
        self.headers = {
           'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:60.0) Gecko/20100101 Firefox/60.0'
        }
    
    def get_html(self,url,title=None):
        '''
        :param url: 请求得分url地址
        :return: 响应数据
        '''
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.text,title
        except Exception as e:
            print('请求失败,失败原因{}'.format(e))
    # 解析列表页数据
    def parse_list_page(self,html):
        # 创建bs对象
        bs = BeautifulSoup(html,'lxml')
        # .ali div a
        a_list = bs.select('.ali div a')
        for a in a_list:
            # 找到详情页的链接地址
            href = a.get('href')
            title = a.get('title')
            # 创建文件夹目录
            path = 'images/'+title
            
            # yield 返回的是生成器对象,并且不会造成程序结束
            
            detail_url = 'http://www.ivsky.com' + href
            yield detail_url, title
            
            if os.path.exists(path):
                continue
            os.mkdir(path)
    def parse_detail_page(self,args):
        # 取出html 和 title
        html = args[0]
        title = args[1]
        print('开始下载:{}'.format(title))
        if html:
            
            # 解析数据
            doc = etree.HTML(html)
            imgs = doc.xpath('//ul[@class="pli"]/li/div/a/img/@src')
            for src in imgs:
                src = str(src)
                # 图片名称
                name = src.split('/')[-1]
                # 图片存放路径
                path = 'images/'+title+'/'+ name
                response= requests.get(src,headers = self.headers)
                with open(path,'wb') as f:
                    f.write(response.content)
                
    
            
    # 执行请求拿回html的回调函数
    def main(self,args):
        # 返回的数据是两个,0是html源代码
        html = args[0]
        if isinstance(html,tuple):
            html = html[0]
        next_page = re.search(re.compile(r"<a class='page-next' href='(.*?)'>"),html)
        if next_page:
            # 找到下一页的链接
            next_url = 'http://www.ivsky.com'+next_page.group(1)
            # 回调main函数
            next_html = self.get_html(next_url)
            self.main((next_html,None))
        else:
            print('已经到达最后一页了')
        
        # 解析列表页数据
        result = self.parse_list_page(html)
        detail_pool = Pool(3)
        for url,title in result:
            # 1.获取html  2.解析详情页
            detail_pool.apply_async(func=self.get_html,args=(url,title),callback=self.parse_detail_page)
        detail_pool.close()
        detail_pool.join()
            

if __name__ == '__main__':
    img = ImageSpider()
    
    pool = Pool(1)
    pool.apply_async(func=img.get_html,args=('http://www.ivsky.com/tupian/ziranfengguang/',),callback=img.main)
    pool.close()
    pool.join()















