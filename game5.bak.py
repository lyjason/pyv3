#!/usr/bin/python
#-*-coding:utf-8-*-
#4.0增加了random函数,优化UI
#5.0新增输入检测机制,开始采用isinstance，后来采用for in循环
import random
answer = random.randint(1,9) 
print('\n****游戏程序版本四****')
print('Build By Jason\n')
i=3
c=2
temp = input('请输入一个个位数: ')
while not  isinstance(temp,int) :
	print('请检查你的输入！')
	temp = input('请输入一个个位数: ')
	c-=1
	if c==0:
		print('请稍后再试，程序已退出！')
		exit()
	else :
		continue
guess = int(temp)
while  i>0 :
	if guess == answer :
		print('答对了，很强势！')
		break
	else:
		if guess >= answer :
			print('整大了')
		else:
			print('整小了')
	i-=1 
	if i != 0 : 
		temp = input('请输入一个个位数: ')
		guess = int(temp)
	else:
		break
print('game over')
