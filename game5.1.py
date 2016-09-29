#!/usr/bin/python
#-*-coding:utf-8-*-
#4.0增加了random函数,优化UI
#5.0新增输入检测机制,开始采用isinstance，后来采用for in循环,后来采用def定义函数，不然代码过于冗长
#5.1新增次数提示功能
import random
answer = random.randint(1,9) 
print('\n****游戏程序版本五****')
print('Build By Jason\n')
dic=('0','1','2','3','4','5','6','7','8','9')

#定义一个函数检测输入有效性
def check(temp):		
	if temp  in dic:
		return True
	else:
		return False
#再定义一个函数，用于完整的检查
def test (x) :
	c = 3
	while not check(x) :
		c-=1
		if c==0:
			print('输入次数已超过三次，程序已停止')
			exit()
		else:
			print('请检查输入对象！还有',c,'次机会')
			temp=input('请输入一个个位数：')
#开始执行实体代码
temp=input('请输入一个个位数：')
test(temp)
guess = int(temp)
i=3
while  i>0 :
	if guess == answer :
		print('答对了，很强势！')
		break
	else:
		if guess >= answer :
			print('   整大了\n')
		else:
			print('   整小了\n')
	i-=1 
	if i != 0 : 
		print('你还有',i,'次机会')
		temp = input('请输入一个个位数: ')
		test
		guess = int(temp)
	else:
		break
print('game over')
