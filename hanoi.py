#!/usr/bin/python
#-*-coding:utf-8-*-
# Author : Jason lya1b2333@hotmail.com 

def hanoi(n,x,y,z):
	if n==1 :
		print(x,'->',z)
	else:
		hanoi(n-1,x,z,y)
		print(x,'->',z)
		hanoi(n-1,y,x,z)

n=int(input('Please input the Hanoi numbers: '))
hanoi(n,'x','y','z')
