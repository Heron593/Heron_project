import requests
from bs4 import BeautifulSoup as bs

#以豆瓣‘编程’分类的一个连接URL为例子开始爬数据ID
url = 'https://book.douban.com/tag/编程?start=20&type=T'   #选取一个需要爬取数据的网址
res = requests.get(url)  #发送请求
#print(res.encoding)    #这个是用来查看网页编码的
#res.encoding = 'utf-8'   #跟上一个结合来用，如果编码有乱码，则可以通过这个定义编码来改变
html = res.text
#print(html)

IDs = []                                           #定义空列表IDs
soup  = bs(html,"html.parser")     #定义一个BeautifulSoup变量soup
items = soup.find_all('a',attrs={'class':'nbg'})  #用find_all函数查找网页中"class"为"nbg"的"a"所有标签，并将找到的标签赋变量items
#print(items)

for i in items:                
    idl = i.get('href')     #用变量"i"获取所有items中的"href"的网址字符串，并将其赋给变量"idl"
    #print(idl)
    id = idl.split('/')[4]   #将获取的网址从字符“/‘处切割，得到第4个分片并赋值给变量id
    print(id)                  #输出所有截取的id
    IDs.append(id)       #将获取的ID添加到列表变量IDs中
print('这一页收集到书籍ID数：%d' % len(IDs))   #统计列表IDs中的数据个数