#!/usr/bin/python
#-*-coding:utf-8-*-
# Author : Jason lya1b2333@hotmail.com
import dns.resolver 
domain=input('Please input an domain: ')
MX=dns.resolver.query(domain,'MX')
#指定查询类型为MX
for i in MX:
#遍历回应结果，输出MX记录的preference及exchanger信息
	print('MX preference=',i.preference,'| mail exchanger=',i.exchange)
