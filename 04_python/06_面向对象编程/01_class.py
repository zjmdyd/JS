#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
	"""docstring for Student"""
	def __init__(self, name, score):
		super(Student, self).__init__()		# 特殊方法“__init__”前后分别有两个下划线！！！
		self.name = name
		self.score = score
	def print_score(self):
		print('%s: %s' % (self.name, self.score))
	def get_grade(self):
		if self.score >= 90:
			return 'A'
		elif self.score >= 60:
			return 'B'
		else:
			return 'C'

# 注意到__init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身		
bart = Student('Simpson', 55)
print(bart)
print(bart.name, bart.score)
bart.print_score()
print(bart.get_grade())

# 和普通的函数相比，在类中定义的函数只有一点不同:
# 就是第一个参数永远是实例变量self，并且，调用时，不用传递该参数。除此之外，类的方法和普通函数没有什么区别，所以，你仍然可以用默认参数、可变参数、关键字参数和命名关键字参数
# 要调用一个方法，只需要在实例变量上直接调用，除了self不用传递，其他参数正常传入
##
# 面向对象编程的一个重要特点就是数据封装
##

# 类是创建实例的模板，而实例则是一个一个具体的对象，各个实例拥有的数据都互相独立，互不影响；

# 方法就是与实例绑定的函数，和普通函数不同，方法可以直接访问实例的数据；

# 通过在实例上调用方法，我们就直接操作了对象内部的数据，但无需知道方法内部的实现细节。

# 和静态语言不同，Python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同：

bart.age = 18
print('bart.age =', bart.age)

lisa = Student('Lisa', 99)	
# print(lisa.age) 	#'Student' object has no attribute 'age'

