from urllib import request as rrr 
import time 
import re 
def xiazai ():
	n = input("请输入书号， 比如：斗破苍穹--") 
	u ="https://www.xs5200.com/"+str(n)+"/"
	a = rrr. urlopen(u) 
	a = a. read(). decode('gbk') 

	b = re. findall ('<dd><a href=\"(.*?) \">.*?</a></ dd>', a) 
	c = re. findall ('<dd><a href=\". */?\"> (.*?)</a><! dd>', a) 
	for i in range (21,31):
		d = rrr.urlopen(b[i]).read().decode('gbk')
		e = re. sub("<div id=\'content\"><>","<br/><>", d) 
		e = re. sub('<br/>','<brl><>', e) 
		e = re. sub ('\u3000\u3000',' ', e) 
		e = re. findall ('''<> (. *?) <br/>''', e) 
		file=open(c[i]+'.txt','w+') 
		for j in e: 
		    file. write (j+'\n') 
		file.close()
		time. sleep (2)
xiazai() 