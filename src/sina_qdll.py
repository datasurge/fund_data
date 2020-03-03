# -*- encode: utf-8 -*-

import os
import time

import requests
from lxml import etree

def get():

    # 请求页面
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
    request = requests.get("http://finance.sina.com.cn/fund/quotes/000989/bc.shtml", headers=header)
    # 设置页面编码
    request.encoding = 'gbk'
    return request


def parse(request):
    # 结构化页面，并进行查询
    html = etree.HTML(request.text)

    # 搜索数据
    fund_name = html.xpath('//*[@id="box-fund-hq"]/div[1]/h1[1]/text()')[0]

    table = html.xpath('//*[@id="box-hq"]/table/tr')
    fund_desc = {}
    for tr in table:
        table_hline = tr.xpath('th')
        for th in table_hline:
            # print(th.text[:-1] + ',')
            fund_desc[th.text[:-1]] = th.xpath('span/text()')[0]
    return fund_desc
    

if __name__ == "__main__":
    
    file_name = 'sina_fund.txt'
    if not os.path.exists(file_name):
        req = get()
        data = parse(req)
        with open(file_name, 'w+',) as f:
            f.write(','.join(data.keys()) + '\n')
            f.write(','.join(data.values()) + '\n')
        print('1111', data.values())
    while True: 
        req = get()
        data = parse(req)
        with open(file_name, 'a+') as f:
            f.write(','.join(data.values()) + '\n')
            f.close()
