#python 3.7.1
from urllib.request import urlopen
from urllib.request import urlretrieve
from bs4 import BeautifulSoup
import pymysql 

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

#如果不存在pic表将会新建href表
'''cur.execute("CREATE TABLE IF NOT EXISTS \
	pic(pid INT NOT NULL AUTO_INCREMENT primary key,p_href varchar(100),p_name varchar(50),UNIQUE(p_href))")'''

#设置需要爬取的网站地址用urlopen(url)打开地址，用bs模块中的lxml解析地址。
url = "http://desk.zol.com.cn/jieri/"
html = urlopen(url)
soup = BeautifulSoup(html,"lxml")

urllist = soup.find_all('a',{'class':'pic'}) #查找所有class值为pic的a标签,{}里面的内容为正则表达式，也可以用class_='pic'代替

#用for in遍历所有rullist
for i in urllist:
	hreflist=i.get('href')
	imgtitle =i.get_text() #获取a标签下面的title
	hrefliststr='\''+'http://desk.zol.com.cn'+hreflist+'\''   #将获取的href以字符串的形式保存
	imgtstr= '\''+ imgtitle +'\''         #将获取的a标签的title以字符串的形式保存
	print(hrefliststr +"-"+ imgtstr)

#将获得的href地址存入数据库(用唯一索引UNIQUE来防止数据重复)
	sql = "INSERT IGNORE INTO pic(p_href,p_name) VALUES ("+hrefliststr+", "+imgtstr+")"
	cur.execute(sql)
	conn.commit()
cur.close()
conn.close()
print("\n以上URL已成功保存到数据库！")