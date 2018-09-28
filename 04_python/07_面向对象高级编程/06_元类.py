#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from hello import Hello
h = Hello()
h.hello()

#
## type()
#

# 当Python解释器载入hello模块时，就会依次执行该模块的所有语句，执行结果就是动态创建出一个Hello的class对象
print(type(Hello))	# <class 'type'>
print(type(h))		# <class 'hello.Hello'>
# type()函数可以查看一个类型或变量的类型，Hello是一个class，它的类型就是type，而h是一个实例，它的类型就是class Hello

# 我们说class的定义是运行时动态创建的，而创建class的方法就是使用type()函数。

# type()函数既可以返回一个对象的类型，又可以创建出新的类型，比如，我们可以通过type()函数创建出Hello类，而无需通过class Hello(object)...的定义

def fn(self, name='world'):
	print('Hello, %s.' % name)
Hello = type('Hello', (object,), dict(hello=fn))
# 要创建一个class对象，type()函数依次传入3个参数：
# class的名称；
# 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
# class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
# 通过type()函数创建的类和直接写class是完全一样的，因为Python解释器遇到class定义时，仅仅是扫描一下class定义的语法，然后调用type()函数创建出class。
h = Hello()
h.hello()
print(type(Hello))
print(type(h))

# 正常情况下，我们都用class Xxx...来定义类，但是，type()函数也允许我们动态创建出类来，也就是说，动态语言本身支持运行期动态创建类，这和静态语言有非常大的不同，
# 要在静态语言运行期创建类，必须构造源代码字符串再调用编译器，或者借助一些工具生成字节码实现，本质上都是动态编译，会非常复杂。

##
# metaclass
##

# 除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass。

# metaclass，直译为元类，简单的解释就是：

# 当我们定义了类以后，就可以根据这个类创建出实例，所以：先定义类，然后创建实例。

# 但是如果我们想创建出类呢？那就必须根据metaclass创建出类，所以：先定义metaclass，然后创建类。

# 连接起来就是：先定义metaclass，就可以创建类，最后创建实例。

# 所以，metaclass允许你创建类或者修改类。换句话说，你可以把类看成是metaclass创建出来的“实例”。

# metaclass是Python面向对象里最难理解，也是最难使用的魔术代码。正常情况下，你不会碰到需要使用metaclass的情况，所以，以下内容看不懂也没关系，因为基本上你不会用到。

# 我们先看一个简单的例子，这个metaclass可以给我们自定义的MyList增加一个add方法：

# 定义ListMetaclass，按照默认习惯，metaclass的类名总是以Metaclass结尾，以便清楚地表示这是一个metaclass：

# metaclass是类的模板，所以必须从`type`类型派生：
class ListMetaclass(type):
	def __new__(cls, name, bases, attrs):
		attrs['add'] = lambda self, value: self.append(value)
		return type.__new__(cls, name, bases, attrs)

# 有了ListMetaclass，我们在定义类的时候还要指示使用ListMetaclass来定制类，传入关键字参数metaclass
class MyList(list, metaclass=ListMetaclass):
	"""docstring for MyList"""
	def __init__(self):
		super(MyList, self).__init__()
# 当我们传入关键字参数metaclass时，魔术就生效了，它指示Python解释器在创建MyList时，要通过ListMetaclass.__new__()来创建，
# 在此，我们可以修改类的定义，比如，加上新的方法，然后，返回修改后的定义

# __new__()方法接收到的参数依次是：

# 当前准备创建的类的对象；

# 类的名字；

# 类继承的父类集合；

# 类的方法集合。

L = MyList()
L.add(1)
print(L)

# 动态修改有什么意义？直接在MyList定义中写上add()方法不是更简单吗？正常情况下，确实应该直接写，通过metaclass修改纯属变态。

# 但是，总会遇到需要通过metaclass修改类定义的。ORM就是一个典型的例子。

# ORM全称“Object Relational Mapping”，即对象-关系映射，就是把关系数据库的一行映射为一个对象，也就是一个类对应一个表，这样，写代码更简单，不用直接操作SQL语句。

# 要编写一个ORM框架，所有的类都只能动态定义，因为只有使用者才能根据表的结构定义出对应的类来。

# 让我们来尝试编写一个ORM框架。

# 编写底层模块的第一步，就是先把调用接口写出来。比如，使用者如果使用这个ORM框架，想定义一个User类来操作对应的数据库表User，我们期待他写出这样的代码：

##
# ORM框架
##
class Field(object):
	"""docstring for Field"""
	def __init__(self, name, column_type):
		super(Field, self).__init__()
		self.name = name
		self.column_type = column_type

	def __str__(self):
		return '<%s:%s>' % (self.__class__.name, self.name)

# 在Field的基础上，进一步定义各种类型的Field，比如StringField，IntegerField等等：
class StringField(Field):
	"""docstring for StringField"""
	def __init__(self, name):
		super(StringField, self).__init__(name, 'varchar(100)')

class IntegerField(Field):
	"""docstring for IntegerField"""
	def __init__(self, name):
		super(IntegerField, self).__init__(name, 'bigint')

# 下一步，就是编写最复杂的ModelMetaclass了
class ModelMetaclass(type):
	"""docstring for ModelMetaclass"""
	def __new__(cls, name, bases, attrs):
		if name == 'Model':	# 排除掉对Model类的修改
			return type.__new__(cls, name, bases, attrs)
		print('Found cls: %s' % cls)
		print('Found model: %s' % name)
		print('Found bases: %s' % bases)
		print('Found attrs: %s' % attrs)
		mappings = dict()		
		for k, v in attrs.items():
			if isinstance(v, Field):
				print('Found mapping: %s ==> %s', (k, v))
				mappings[k] = v

		for k in mappings.keys():
			attrs.pop(k)
		attrs['__mappings__'] = mappings 	# 保存属性和列的映射关系
		attrs['__table__'] = name 			# 假设表名和类名一致
		return type.__new__(cls, name, bases, attrs)
class Model(dict, metaclass=ModelMetaclass):
	"""docstring for Model"""
	def __init__(self, **kw):
		super(Model, self).__init__(**kw)
	def __getattr__(self, key):
		try:
			return self[key]
		except Exception as e:
			raise AttributeError(r"'Model' object has no attribute '%s'" % key)
	def __setattr__(self, key, value):
		self[key] = value
	def save(self):
		fields = []
		params = []
		args = []
		for k, v in self.__mappings__.items():
			fields.append(v.name)
			params.append('?')
			args.append(getattr(self, k, None))
		sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
		print('SQL: %s' % sql)
		print('ARGS: %s' % str(args))

# 当用户定义一个class User(Model)时，Python解释器首先在当前类User的定义中查找metaclass，如果没有找到，就继续在父类Model中查找metaclass，找到了，就使用Model中定义的metaclass的ModelMetaclass来创建User类，也就是说，metaclass可以隐式地继承到子类，但子类自己却感觉不到。

# 在ModelMetaclass中，一共做了几件事情：

# 排除掉对Model类的修改；

# 在当前类（比如User）中查找定义的类的所有属性，如果找到一个Field属性，就把它保存到一个__mappings__的dict中，同时从类属性中删除该Field属性，否则，容易造成运行时错误（实例的属性会遮盖类的同名属性）；

# 把表名保存到__table__中，这里简化为表名默认为类名。

class User(Model):
	id = IntegerField('id')
	name = StringField('username')
	email = StringField('email')
	password = StringField('password')
u = User(id=12345, name='Lisa', email='test@orm.org', password='my-pwd')
u.save()
# metaclass是Python中非常具有魔术性的对象，它可以改变类创建时的行为。这种强大的功能使用起来务必小心