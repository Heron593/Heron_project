import requests
from bs4 import BeautifulSoup
url="https://www.cnblogs.com/gopythoner/p/6390381.html" #这里是需要爬取的网页
html=requests.get(url).text#这里是使用urllib模块的open函数打开url 再使用read函数读取网页内容 赋值给content

codes = []
soup=BeautifulSoup(html,'html.parser') #这里是将content内容转化为BeautifulSoup格式的数据
item=soup.find_all('span',attrs={'cnblogs_code'})

'''for i in item:
	copre = i.get('pre')'''

print (item)#这里是输出网页html的内容