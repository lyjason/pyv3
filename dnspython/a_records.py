#!/usr/bin/env python
#-*-coding:utf-8-*-
# Author : Jason lya1b2333@hotmail.com
import dns.resolver
domain=input('Please input an domain: ')
#输入域名
A=dns.resolver.query(domain,'A')
#指定查询为A记录
for i in A.response.answer:
#通过response.answer方法获取查询回应信息
	for j in i.items:
#遍历回应信息
		print (j.address)
