#!/usr/bin/python
#-*-coding:utf-8-*-
#更新日志：
#1.添加输入判断，保证只输入数字。
#
print('\n****游戏程序版本三****')
print('Build By Jason\n')
temp = input('请输入一个个位数：')
c=['0','1','2','3','4','5','6','7','8','9']
while temp != c :
	print("check your input!")
	temp = input('请输入一个个位数：')
guess = int(temp)
i=2
while guess != 8 and i>0 :
	if guess == 8 :
	    print('答对了，很强势！')
	else:
		if guess >= 8 :
			print('整大了')
		else:
			print('整小了')
	temp = input('请重新输入一个值：')
	while temp != c :
		print("check your input!") 
		temp = input('请输入一个个位数：')
	guess=int(temp)
	i=i-1
print('game over')
