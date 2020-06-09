'''写注释是不可能写注释的
这辈子都不可能写注释的'''
import csv
import time
import codecs
import requests
from lxml import etree

# 定义爬虫类
class PGH:
    def __init__(self, page):
        '''
        初始化类
        '''
        # 起始URL
        self.url = 'http://sz.xiaozhu.com/search-duanzufang-p{}-0/'.format(page)
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                                      'Chrome/76.0.3809.100 Safari/537.36'
                        }
    
    # 网页请求
    def get_html(self, url):
        res = requests.get(self.url, headers=self.headers).text
        return res
    
    # 数据解析
    def get_hotel(self, res):
        html = etree.HTML(res)
        hotel = html.xpath('//*[@id="page_list"]/ul/li')   # 这一步获取的是包含所有租房信息的大标签
        time.sleep(1)
        return hotel
    
    # 写入文件呢
    def writer_in_file(self, hotel):
        with open('house2.csv', 'ab+')as fp:
            fp.write(codecs.BOM_UTF8)
        fp = open('house2.csv', 'a+', newline='', encoding='utf-8')
        writer = csv.writer(fp)
        # 分别从全部租房信息中取出相应内容
        for i in hotel:
            title = i.xpath('./div[2]/div[2]/a/span/text()')[0]
            price = i.xpath('./div[2]/div[1]/span/i/text()')[0]
            describe = i.xpath('./div[2]/div[2]/em/text()')[0].strip()
            writer.writerow([title, price, describe])

    def run(self):
        res = self.get_html(url)
        hotel = self.get_hotel(res)
        self.writer_in_file(hotel)

if __name__ =="__main__":
    for page in range(1, 6):
        pg = PGH(page)
        pg.run()
