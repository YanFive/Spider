'''写注释是不可能写注释的
这辈子都不可能写注释的'''
import csv
import time
import codecs
import requests
from lxml import etree

class PGH(object):
    def __init__(self, page):
        self.url = 'http://sz.xiaozhu.com/search-duanzufang-p{}-0/'.format(page)
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                                      'Chrome/76.0.3809.100 Safari/537.36'
                        }

    def get_html(self, url):
        res = requests.get(self.url, headers=self.headers).text
        return res

    def get_hotel(self, res):
        html = etree.HTML(res)
        hotel = html.xpath('//*[@id="page_list"]/ul/li')
        time.sleep(1)
        return hotel

    def writer_in_file(self, hotel):
        with open('house2.csv', 'ab+')as fp:
            fp.write(codecs.BOM_UTF8)
        fp = open('house2.csv', 'a+', newline='', encoding='utf-8')
        writer = csv.writer(fp)
        for i in hotel:
            title = i.xpath('./div[2]/div[2]/a/span/text()')[0]
            price = i.xpath('./div[2]/div[1]/span/i/text()')[0]
            describe = i.xpath('./div[2]/div[2]/em/text()')[0].strip()
            writer.writerow([title, price, describe])

    def run(self):
        res = self.get_html(self.url)
        hotel = self.get_hotel(res)
        self.writer_in_file(hotel)

if __name__ =="__main__":
    for page in range(1, 6):
        pg = PGH(page)
        pg.run()
