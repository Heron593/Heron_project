# coding=utf-8
 
import requests
from bs4 import BeautifulSoup as nn   #从bs4库中引入BeautifulSoup类 赋值到参数nn中（简单说就是用变量nn代替BeautifulSoup类）

# 获取html文档
def get_html(url):
    """get the content of the url"""
    response = requests.get(url)
    response.encoding = 'utf-8'
    return response.text

# 获取笑话
def get_certain_joke(html):
    """get the joke of the html"""
    soup =nn(html, 'lxml')
    joke_content = soup.select('div.content')[0].get_text()
    return joke_content

#选取网站并调用get_html函数和get_certain_joke函数获取关键值。
url_joke = "https://www.qiushibaike.com"
html = get_html(url_joke)
joke_content2 = get_certain_joke(html)
print (joke_content2)