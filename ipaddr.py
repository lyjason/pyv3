#!/usr/bin/python
#-*-coding:utf-8-*-
# Author : Jason lya1b2333@hotmail.com 
from IPy import IP
ip_s=input('Please input an IP or net-range:')
#接收用户的输入，参数为IP地址或网段
ips=IP(ip_s)
if len(ips) > 1 :
#若为同一个网络地址
	print('net:%s'%ips.net())
	print('netmask:%s'%ips.netmask())
	print('broadcast:%s'%ips.broadcast())
	print('reverse address:%s'%ips.reverseNames())
	print('subnet:%s'%len(ips))
else:
	print('reserve address:%s'%ips.reverseNames()[0])
	print('hexadecimal:%s'%ips.strHex())
	print('binary ip:%s'%ips.strBin())
	print('iptype:%s'%ips.iptype())
