#!/usr/bin/python
#-*-coding:utf-8-*-
#增加了random函数
import random
answer = random.randint(1,9) 
print('\n****游戏程序版本四****')
print('Build By Jason\n')
i=3
temp = input('请输入一个个位数: ')
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
	i=i-1 
	if i != 0 : 
		temp = input('请输入一个个位数: ')
		guess = int(temp)
	else:
		break
print('game over')
