import random
rand = random.randint(1,10)
print("----------猜猜数字----------")
xn = 0
n=3
while xn<3:
	print("你有 %d 次机会,加油！" %(n))
	guess = int(input("请输入你的答案："))
	if  guess > rand:
		print("输入的数字大了大了")
	else:
		if guess <rand:
			print("输入的数字小了小了")
		else:
			print("恭喜你猜对了！")
			break
	xn +=1
	n -=1
else:
	print("阿哦，次数用完~~~")