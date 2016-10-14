#!/usr/bin/env python
#-*-coding:utf-8-*-
# Author : Jason lya1b2333@hotmail.com
import dns.resolver
domain=input('Please input an domain: ')
cname=dns.resolver.query(domain,'CNAME')
for i in cname.response.answer:
#结果将回应cname后的目标名
	for j in i.items:
		print(j.to_text())
