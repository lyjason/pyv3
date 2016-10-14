#!/usr/bin/env python
#-*-coding:utf-8-*-
# Author : Jason lya1b2333@hotmail.com
import dns.resolver
domain=input('Please input an domain: ')
ns=dns.resolver.query(domain,'NS')
#指定查询为NS记录
for i in ns.response.answer:
	for j in i.items:
		print(j.to_text())
#只限输入一级域名，如baidu.com，而www.baidu.com就是错误的
