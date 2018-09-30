#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from io import StringIO
f = StringIO()
print(f.write('hello'))
print(f.getvalue())		# getvalue()方法用于获得写入后的str

# 要读取StringIO，可以用一个str初始化StringIO，然后，像读文件一样读取

f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
	s = f.readline()
	if s == '':
		break
	print(s.strip())

##	
# BytesIO
##

# StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO。

# BytesIO实现了在内存中读写bytes，我们创建一个BytesIO，然后写入一些bytes：
from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())
# 请注意，写入的不是str，而是经过UTF-8编码的bytes。

# 和StringIO类似，可以用一个bytes初始化BytesIO，然后，像读文件一样读取：
from io import BytesIO 
f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
f.read()
v = f.getvalue()
print(v)
print(v.decode('utf-8'))