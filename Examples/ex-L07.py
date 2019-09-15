#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Для исполнения одного примера задайте его номер
в качестве параметра при запуске программы
"""

import sys

def pfi():
	"Print function information"
	caller_code = sys._getframe(1).f_code
	example_no = caller_code.co_name[-2:]
	h = '*' * 6
	print('\n       ', h, 'Example', example_no, h)
	print(caller_code.co_consts[0])

def example_01():
	"""
	Определение класса и наследование
	"""
	pfi()
	class Sample:
		def fun(self, n):
			print('Call ' + 'fun(', n, ') of', self.__class__)

	sample = Sample() # Скобки обязательны, это вызов класса как функции
	sample.fun(3)

	# Пустой класс без наследования
	class Empty:
		pass
	# Пустой класс без наследования, скобки допустимы
	class Empty2():
		pass
	# Пустой класс с наследованием
	class Empty3(Empty, Empty2, Sample):
		pass
	nonempty = Empty3()
	nonempty.fun(5)
	
	Empty.n = 12
	# Новая функция-атрибут класса
	Empty.amul = lambda self, a, b: a * b
	m = Empty()
	print('m.amul(2, 3) =>', m.amul(2, 3), ', m.n =', m.n)
	# Новая функция-атрибут объекта
	m.asub = lambda a, b: a - b
	print('m.asub(5, 4) =>', m.asub(5, 4))

	print(dir(type(Empty3)))
	# int это класс, он неявно наследует от класса object
	print('int.__bases__ =', int.__bases__)

def example_02():
	"""
	Создание атрибутов объекта
	"""
	pfi()
	class Sample:
		def __init__(self, a, b):
			self.a = a
			self.b = b 
		def divide(self):
			return self.a / self.b

	m = Sample(6, 2) # Параметры 6 и 2 передаются в метод  __init__()
	print('6 / 2 =', m.divide()) # => 3.0

def example_03():
	"""
	Явный вызов метода __init__() в методах дочерних классов
	"""
	pfi()
	# __init__(self) родительских классов вызывается явно
	class Parent1:
		def __init__(self):
			print('Parent1', end=',')
	class Parent2:
		def __init__(self):
			print('Parent2', end=',')
	class ChildA(Parent1, Parent2):
		def __init__(self):
			print('ChildA')
	class ChildB(Parent1, Parent2):
		def __init__(self):
			Parent1.__init__(self)
			print('ChildB')
	class ChildC(Parent1, Parent2):
		def __init__(self):
			Parent1.__init__(self)
			Parent2.__init__(self)
			print('ChildC')
	
	ca = ChildA()
	cb = ChildB()
	cc = ChildC()
	print('Parent1.__bases__ =', Parent1.__bases__)
	print('ChildC.__bases__ =', ChildC.__bases__)

def example_04():
	"""
	Дополненные свойства
	"""
	pfi()
	class A:
		def __init__(self, v):
			self.v = v

	a = A(5)
	# Придание объекту дополнительного атрибута
	a.pow2 = lambda : a.v ** 2
	print(a.pow2())
	b = A(3)
	#print(b.pow2()) # AttributeError: 'A' object has no attribute 'pow2'
	
	# Придание классу дополнительного атрибута
	A.counter = 9
	print('A.counter =', A.counter, ', a.counter =', a.counter, ', b.counter =', b.counter)
	A.counter -= 4
	print('A.counter =', A.counter, ', a.counter =', a.counter, ', b.counter =', b.counter)

def example_05():
	"""
	Атрибуты класса и атрибуты объекта
	"""
	pfi()
	class A:
		ca = 'A:ca'          # атрибут класса
		cz = 'A:cz'          # атрибут класса
		def __init__(self):
			self.a = 'A:a'   # атрибут объекта
			self.z = 'A:z'   # атрибут объекта
	class B:
		cb = 'B:cb'
		cz = 'B:cz'
		def __init__(self):
			self.b = 'B:b'
			self.z = 'B:z'
	class C(A, B):           # При создании объекта x:
		def __init__(self):  # объект x не имеет атрибутов, self это x
			A.__init__(self) # объект x получил атрибуты a и z
			B.__init__(self) # объект x получил атрибут b,
			                 # атрибуту z присвоено другое значение
			self.c = 'C:c'   # объект x получил атрибут c
	def fun3():
		return('C:fun3()')
	
	x = C() # => C.__init__(x)
	y = C() # => C.__init__(y)

	print('Attributes available = ', dir(x))
	print("Object's own attributes = ", [e for e in x.__dict__.keys()])
	print('x.a =', x.a)   # => A:a
	print('x.b =', x.b)   # => B:b
	print('x.c =', x.c)   # => C:c
	print('x.ca =', x.ca) # => A:ca
	print('x.cb =', x.cb) # => B:cb
	print('x.cz =', x.cz) # => A:cz
	print('x.z =', x.z)   # => B:z
	print('*** Assign new_cz to x.cz ***')
	x.cz = 'new_cz' # объект x получил собственный атрибут cz
	print("Object's own attributes = ", [e for e in x.__dict__.keys()])
	print('x.cz =', x.cz) # => new_cz
	print('y.cz =', y.cz) # => A:cz

	print('*** Add function fun1 to class C ***')
	C.fun1 = lambda self, x: self.a + self.b + str(x)
	print("Object's own attributes = ", [e for e in x.__dict__.keys()])
	print(x.fun1(111)) # => A:aB:b111

	print('*** Add function fun2 to object x ***')
	x.fun2 = lambda self, x: self.a + self.b + str(x)
	x.fun3 = 0

	print("Object's own attributes = ", [e for e in x.__dict__.keys()])
	# Функцию можно придать объекту, но она не становится методом
	#print(x.fun2(222)) # => TypeError: missing 1 required positional argument
	print(x.fun2(x, 222)) # => A:aB:b222
	# Поиск метода происходит по всем атрибутам независимо от их типа
	#print(x.fun3()) # => TypeError: 'int' object is not callable

def example_06():
	"""
	Документирование класса
	"""
	pfi()
	class Sample:
		"""
		Sample это простой класс, содержащий единственную функцию fun()
		Класс используется исключительно как пример
		"""
		# self это традиционное имя, оно не является зарезервированным
		def fun(not_a_self, n):
			"""
			Функция fun() печатает свой параметр и свой класс.
			Она также является примером необязательности имени self
			для первого аргумента метода
			"""
			print('Call ' + 'fun(', n, ') of', not_a_self.__class__)
	m = Sample()
	m.fun(5)
	# help(Sample) # Уберите символ '#' в начале строки что бы увидеть help
	print(Sample.__doc__, Sample.fun.__doc__)

if len(sys.argv) > 1 and sys.argv[1].isdigit() and int(sys.argv[1]) > 0:
	exec('example_%02d()' % int(sys.argv[1]))
else:
	tuple(map(lambda c: exec(c + '()'),
		(f for f in sys._getframe().f_code.co_names
			if f.startswith('example_'))))
