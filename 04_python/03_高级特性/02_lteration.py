#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import Iterable

d = {'a' : 1, 'b' : 2, 'c' : 3}
for key in d:
	print(key)

for value in d.values():
	print(value)

for k, v in d.items():
	print(k, v)

print(isinstance('abc', Iterable))
print(isinstance([1, 2, 3], Iterable))
print(isinstance(123, Iterable))

# enumerate函数可以把一个list变成索引-元素对
for i, value in enumerate(['A', 'B', 'C']):
	print(i, value)

for x, y in [(1, 1), (2, 4), (3, 9)]:
	print(x, y)