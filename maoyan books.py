import requests
from lxml import etree
import json

def main():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
    page = 10
    with open('info.txt', 'w+')as f:
        for i in range(page):
            url = 'http://maoyan.com/board/4?offset='+str(i*10)
            html = requests.get(url, headers=headers)
            html.encoding = 'utf-8'
            tree = etree.HTML(html.text)
            title = tree.xpath('//*[@id="app"]/div/div/div[1]/dl/dd/div/div/div[1]/p[1]/a/text()')
            star = tree.xpath('//*[@id="app"]/div/div/div[1]/dl/dd/div/div/div[1]/p[2]/text()')
            time = tree.xpath('//*[@id="app"]/div/div/div[1]/dl/dd/div/div/div[1]/p[3]/text()')
            #score1 = tree.xpath('//*[@id="app"]/div/div/div[1]/dl/dd/div/div/div[2]/p/i[1]/text()')
            for j in range(len(title)):
                #temp = (title[j], star[j].strip(), time[j])
                #print(temp)
                f.write('《{}》 {}--{}\n'.format(title[j], star[j].strip(), time[j]))

if __name__ =='__main__':
    main()
