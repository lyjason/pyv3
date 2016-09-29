#!/usr/bin/python
#-*-coding:utf-8-*-
#this script is used to convert different system

#定义函数用来提示如何输入数据
def example (x):	
	if x == 2:
		print('(2-system,for exmaple:10100010)')
	elif x == 8:
		print('(8-system,for exmaple:1234567)')
	elif x == 10:
		print('(10-system,for exmaple:1234567890)')
	elif x == 16:
		print('(16-system,for exmaple:abcd12133)')
#定义函数，任何进制转为10进制，10进制转为任何进制
def system (x,y,z):			
	a=int(y,x)	
	if x-z==0:
		r=y
	elif z == 2:
		r=bin(a)
	elif z == 8:
		r=oct(a)
	elif z == 10:
		r=int(a)
	elif z == 16:
		r=hex(a)
	print('this is your target munber:',r)
	
#代码开始
print('*************************************************')
sys1=input('which system is your inputed(2/8/10/16):')
sys1=int(sys1)
example(sys1)
num=input('please input any system number:')
sys2=input('which system is your want to convert(2/8/10/16):')
sys2=int(sys2)
print('*************************************************')
print("your input system",sys1,',your target system',sys2)
print('your input number:',num)
system(sys1,num,sys2)
