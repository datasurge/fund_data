# -*- coding: utf-8 -*-

import time

from lxml import etree
from selenium import webdriver

history_url = 'http://stock.finance.sina.com.cn/fundInfo/view/FundInfo_LSJZ.php?symbol=000989'


def main():
    # jsCode = "var q=document.documentElement.scrollTop=300"
    driver = webdriver.Chrome()

    driver.get(history_url)
    # 等待5秒
    time.sleep(10)
    # WebDriverWait(driver, 10)
    # driver.implicitly_wait(10)
    # 滚动页面
    driver.execute_script("window.scrollTo(0,300)")
    # 总页数
    page_number = int(driver.find_element_by_xpath('//*[@id="right"]/div[1]/div/span[2]/em[2]').text)
    
    history_list = []
    # current_page = int(driver.find_element_by_xpath('//*[@id="right"]/div[1]/div/span[2]/em[1]').text)
    for page in range(page_number):
        html = etree.HTML(driver.page_source)
        # 获取表格整体
        table_tr = html.xpath('//*[@id="right"]/div[1]/table/tbody/tr')
        
        for i in range(2, len(table_tr)):
            history = table_tr[i].xpath('td/text()')
            history_list.append(history)
        
        next_button = driver.find_element_by_xpath('//*[@id="right"]/div[1]/div/a[last()]')
        # 点击下一页按钮
        next_button.click()
        time.sleep(5)
        print(page)
        
    return history_list

if __name__ == "__main__":
    
    tag_name = ['日期', '累计净值(元)', '累计净值(元)', '净值增长率']
    history_list = main()    
    with open('./history_qdll.txt', 'w') as f:
        f.write(','.join(tag_name) + '\n')
        for l in history_list:
            f.write(','.join(l) + '\n')
        f.close()
        
    # print(history_list)