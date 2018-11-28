#python 3.7.1
from urllib.request import urlopen
from urllib.request import urlretrieve
from bs4 import BeautifulSoup
import pymysql
from lxml import etree

#连接mysql数据库pmdb
conn = pymysql.connect(
	host='127.0.0.1',
	port=3306,
	user='root',
	passwd='root',
	db='spiderdb',
	charset='utf8'
	)

#获取游标
cur = conn.cursor()

#如果不存在href表将会新建href表，p_herf设置为UNIQUE，防止数据重复插入
'''cur.execute("CREATE TABLE IF NOT EXISTS \
 href	(pid INT NOT NULL AUTO_INCREMENT primary key,p_href varchar(50),p_name varchar(50),UNIQUE(p_href))")'''

#设置需要爬取的网站地址用urlopen(url)打开地址，用bs模块中的lxml解析地址。
url = "http://www.mm131.com/mingxing/"
html = urlopen(url)
soup = BeautifulSoup(html,"lxml")

 #因为class是python的关键字，所以在写过滤的时候，应该是这样写：soup.find_all('a',class_='xxx') 或soup.select(a[class='xxx'])
urllist = soup.find('dl',class_='list-left public-box') #获取class值为'list-left public-box'的dl标签
ddlist = urllist.find_all('dd',class_="")   #获取该dl下所有class为空值的dd标签

#用for in遍历所有rullist
for i in ddlist:
	jlist = i.find('a')['href']    #查找dd标签下面的所有的a标签里面的href地址
	title = i.get_text()   #获取a标签里面的title
	jliststr='\''+jlist+'\''      #将获取的href以字符串的形式保存
	titstr='\''+title+'\''	#将获取的title以字符串的形式保存
	print(jliststr)
	print(title)
	cur.execute("INSERT IGNORE INTO href(p_href,p_name) VALUES ("+jliststr+","+titstr+")")  #将获得的href地址及title存入数据库
	conn.commit()
cur.close()
conn.close()
print("\n以上图片URL保存成功！")