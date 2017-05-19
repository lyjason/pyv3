#-*- coding:utf-8 -*-
#加载随机模块
import random 
#定义
def decide(x):
    pass
    
#正文
print("this is a python program\n")
print("now i have a numbers\n")
print("this is an integer from 0 to 10\n")
num=random.randint(0,10)
guess=input("Guess it:")
guess=int(guess)
t=3
while t>0:
    if guess==num :
        print("\nYes!You are right:",num,'\n')
        break
    else:
        if guess>num:
            print("\n====>Bigger<====\n")
        else:
            print("\n====>Smaller<====\n") 
    t-=1
    if t>0:
        guess=int(input("Please try again:"))
    else :
        print("\nSorry! your time has been run out of\n")
