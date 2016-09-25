#!/usr/bin/python
#-*-coding:utf-8-*-
print('游戏程序版本二')
print('Build By Jason')
temp = input('请输入一个个位数：')
guess = int(temp)
if guess == 8 :
    print('答对了，很强势！')
else:
    if guess >= 8 :
     print('整大了')
    else:
     print('整小了')
print('game over')
