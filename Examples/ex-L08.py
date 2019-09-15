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

def shdr(s):
	"Section header"
	h = '*' * 6
	print('\n   ', h, s, h, '\n')

def phdr(s):
	"Paragraph header"
	h = '=' * 3
	print('   ', h, s, h)

def m(s):
	"Print mark at line begin"
	print(s + ' => ', end='')

import math

def example_01():
	"""
	Атрибут __dict__ это словарь, хранящий атрибуты объекта
	"""
	pfi()
	class Point():
		def __init__(self, x, y):
			self.x = x
			self.y = y
		def distance(self):
			return math.sqrt(self.x ** 2 + self.y ** 2)

	m('Point.__dict__'); print(Point.__dict__)
	p = Point(3, 4)
	m('p.__dict__'); print(p.__dict__)
	attribite_name = 'color'
	p.__dict__[attribite_name] = 'red'
	m('p.__dict__'); print(p.__dict__)

	p.get_x = lambda a: a.x
	p.__dict__['get_y'] = lambda a: a.y
	m('p.__dict__'); print(p.__dict__)

	print(p.get_x(p), p.get_y(p), p.distance(), p.color)

def example_02():
	"""
	Объект и его класс. Атрибуты __bases__ и __module__.
	Является ли объект воплощением класса ? Функция isinstance().
	"""
	pfi()

	phdr('Class Empty')
	class Empty:
		pass
	e = Empty()
	print(isinstance(Empty, object)) # => True, класс это объект класса type,
	                                 # => который наследует от object
	print(isinstance(e, object)) # => True
	print(isinstance(e, Empty)) # => True
	print(Empty.__bases__) # => (<class 'object'>,)
	#print(e.__bases__) # => 'Empty' object has no attribute '__bases__'
	print(Empty.__module__) # => __main__
	print(e.__module__) # => __main__

	phdr('Class Empty2')
	class Empty2(Empty):
		pass
	e2 = Empty2()
	print(isinstance(Empty2, object)) # => True
	print(isinstance(Empty2, Empty)) # => False, наследует, но не является элементом
	print(isinstance(e2, object)) # => True
	print(isinstance(e2, Empty2)) # => True
	print(isinstance(e2, Empty)) # => True
	print(isinstance(e2, (Empty, Empty2, object))) # => True
	print(Empty2.__bases__) # => (<class '__main__.example_02.<locals>.Empty'>,)

def example_03():
	"""
	Является ли класс субклассом ? Функция issubclass().
	"""
	pfi()
	m('issubclass(int, object)'); print(issubclass(int, object)) # => True
	m('issubclass(int, int)');    print(issubclass(int, int))    # => True
	m('issubclass(int, str)');    print(issubclass(int, str))    # => False
	m('issubclass(int, (str, object))'); print(issubclass(int, (str, object))) # => True

def example_04():
	"""
	Атрибут класса __doc__ хранит документацию класса.
	Объект наследует атрибут __doc__ от своего класса.
	"""
	pfi()
	phdr('Class Empty')
	class Empty:
		'Пустой класс'
	print(Empty.__doc__)
	e = Empty()
	print(e.__doc__)

def example_05():
	"""
	Атрибуты класса и атрибуты объекта
	"""
	pfi()
	class Sample:
		def fun(self, n):
			print('Call ' + 'fun(', n, ') of', self.__class__)

	sample = Sample()
	sample.fun(3)
	print(dir(object))

	# Metod __sizeof__
	phdr('object.__sizeof__(object)')
	print(object.__sizeof__(object))

	shdr('Атрибуты класса Sample')
	phdr('dir(Sample)')
	print(dir(Sample))
	phdr('Sample.__dict__')
	print(Sample.__dict__)
	phdr('Sample.__bases__')
	print(Sample.__bases__)
	phdr('object')

	shdr('Атрибуты объекта sample')
	phdr('dir(sample)')
	print(dir(sample))
	phdr('sample.__class__')
	print(sample.__class__)
	phdr('sample.__class__.__name__')
	print(sample.__class__.__name__)
	phdr('sample.__ge__')
	print(sample.__ge__)
	phdr('sample.__getattribute__')
	print(sample.__getattribute__)
	phdr('sample.__gt__')
	print(sample.__gt__)
	phdr('sample.__hash__')
	print(sample.__hash__)
	phdr('sample.__init__')
	print(sample.__init__)
	phdr('sample.__le__')
	print(sample.__le__)
	phdr('sample.__lt__')
	print(sample.__lt__)
	phdr('sample.__ne__')
	print(sample.__ne__)
	phdr('sample.__new__')
	print(sample.__new__)
	phdr('sample.__reduce__')
	print(sample.__reduce__)
	phdr('sample.__reduce_ex__')
	print(sample.__reduce_ex__)
	phdr('sample.__repr__')
	print(sample.__repr__)
	phdr('sample.__setattr__')
	print(sample.__setattr__)
	phdr('sample.__sizeof__')
	print(sample.__sizeof__)
	phdr('sample.__str__')
	print(sample.__str__)
	phdr('sample.__subclasshook__')
	print(sample.__subclasshook__)

	shdr('Атрибуты класса int')
	phdr('dir(int)')
	print(dir(int))

	class C1:
		pass
	class C2:
		pass
	class C3(C1, C2, Sample):
		pass

	shdr('Родительские классы класса C3')
	phdr('C3.__bases__')
	print(C3.__bases__)

class Device:
	"""
	Класс демонстрирующий перегрузку операторов
	для example_06()
	"""
	if True:
	#if False:
		# Явная фиксация типов атрибутов
		def __init__(self, serial, precision):
			self.serial = int(serial)
			self.precision = float(precision)
	else:
		# Тип атрибутов может оказаться любым
		def __init__(self, serial, precision):
			self.serial = serial
			self.precision = precision
	def __gt__(self, other):
		return self.serial > other.serial
	if True:
	#if False:
		def __str__(self):
			return 'Device No ' + str(self.serial) + \
			' with precision ' + str(self.precision) + ' %'
	def __repr__(self):
		return '<Object of class Device, serial = ' + \
		str(self.serial) + ', precision = ' + str(self.precision) + '>'
	def __int__(self):
		return self.serial
	def __float__(self):
		return self.precision
	def __add__(self, other):
		return int(self) + int(other)
	def __sub__(self, other):
		return int(self) - int(other)
	def __mul__(self, other):
		return int(self) * int(other)
	def __mod__(self, other):
		return int(self) % int(other)
	def __rmod__(self, other):
		print('Call to __rmod__() => ', end='')
		return int(other) % int(self)
	def __call__(self, a, b):
		print('Class Device called with arguments a =', a, 'b =', b)

def example_06():
	"""
	Перегрузка операторов
	"""
	pfi()
	d = Device(serial=830274, precision=0.02)
	e = Device(serial=316839, precision=0.01)
	if d > e:
		print('d is greater than e')
	else:
		print('d is NOT greater than e')
	print(d)            # => 'Device No 830274 with precision 0.02 %'
	print(repr(d))      # => '<Object of class Device, serial = 830274, precision = 0.02>
	n = d + e           # => Объекты интерпретируются как два целых, см. __add__()
	print(n.__class__)  # => <class 'int'>
	print(n)            # => 1147113
	f = d + float(e)    # => d интерпретируются как целoe, см. __add__()
	print(f.__class__)  # => <class 'int'>
	print(f)            # => 830274
	print(d + e)        # => 1147113
	print(d - e)        # => 513435
	print(d * e)        # => 263063183886
	print(d % e)        # => 196596
	print(d % 7)        # => 4
	print(12394727 % d) # => Call to __rmod__() => 770891
	# print(str(d) + e) # => TypeError: Can't convert 'Device' object to str implicitly
	print(str(d) + str(e)) # => 'Device No 830274 with precision 0.02 %Device No 316839 with precision 0.01 %'
	d(1, 2)             # => 'Class Device called with arguments a = 1 b = 2'
	m = Device(d, 0.25) # => serial взят из d, благодаря явному вызову int(serial) в __init__()
	print('m:', m)
	# print(d / 2)     # => TypeError: unsupported operand type(s) for /: 'Device' and 'int'
	print(int(d) / 2)  # => 415137.0

def example_07():
	"""
	Прокси-класс, устанавливающий порядок в словаре
	и позволяющий обращение к величинам по индексу.
	Реализация оператора [].
	"""
	pfi()
	class DictToList:
		def __init__(self, content):
			self.d = content
		def __getitem__(self, index):
			return self.d[sorted(self.d.keys())[index]]
		def __setitem__(self, index, value):
			self.d[sorted(self.d.keys())[index]] = value
		def __len__(self):
			return len(self.d)
		def __str__(self):
			return str(self.d)

	x = {'a': 0, 'b': 1, 'c': 2}
	c = DictToList(x)
	print('c =', c) # => {'a': 0, 'c': 2, 'b': 1}
	print('len(c) =', len(c)) # => 3
	print('c[2] =', c[2]) # => 2
	c[2] = 22
	print('c[2] =', c[2]) # => 22
	#print('c[3] =', c[3]) # => IndexError: list index out of range
	print('c =', c) # => {'a': 0, 'c': 22, 'b': 1}
	print('x =', x) # => {'a': 0, 'c': 22, 'b': 1}

def example_08():
	"""
	Вызов объекта как функции.
	Проверка возможности вызова объекта.
	Проверка наличия атрибута.
	"""
	pfi()
	class Simple:
		def __init__(self):
			self.x = 1
		def __call__(self):
			print('I am object of class Simple')
	s = Simple()
	m("s()"); s() # => 'I am object of class Simple'
	phdr('Check object of class Simple')
	m("print(callable(s))");     print(callable(s))            # => True
	m("hasattr(s, '__call__')"); print(hasattr(s, '__call__')) # => True
	m("hasattr(s, 'x')");        print(hasattr(s, 'x'))        # => True
	m("hasattr(s, 'y')");        print(hasattr(s, 'y'))        # => False

	phdr('Check class Simple')
	m("callable(Simple)");            print(callable(Simple))       # => True
	m("hasattr(Simple, '__call__')"); print(hasattr(Simple, '__call__')) # => True
	m("hasattr(Simple, 'x')");        print(hasattr(Simple, 'x'))   # => False
	m("hasattr(Simple, 'y')");        print(hasattr(Simple, 'y'))   # => False
	
	class Empty:
		pass
	e = Empty()
	phdr('Check object of class Empty')
	m("callable(e)");            print(callable(e))            # => False
	m("hasattr(e, '__call__')"); print(hasattr(e, '__call__')) # => False
	m("hasattr(e, 'x')");        print(hasattr(e, 'x'))        # => False
	m("hasattr(e, 'y')");        print(hasattr(e, 'y'))        # => False

	phdr('Check class Empty')
	m("callable(Empty)");            print(callable(Empty))       # => True
	m("hasattr(Empty, '__call__')"); print(hasattr(Empty, '__call__')) # => True
	m("hasattr(Empty, 'x')");        print(hasattr(Empty, 'x'))   # => False
	m("hasattr(Empty, 'y')");        print(hasattr(Empty, 'y'))   # => False

def example_09():
	"""
	Реализация фрагментов. Класс slice.
	"""
	pfi()
	a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	print(a[2:8:2]) # => [2, 4, 6]
	print(a[slice(2,8,2)]) # => [2, 4, 6]
	
	class ReversedList:
		def __init__(self, a):
			self.a = list(reversed(a))
		def __str__(self):
			return str(self.a)
		def __getitem__(self, index):
			if isinstance(index, slice):
				print('index is the', index, end=' => ')
			return self.a[index]

	r = ReversedList(a)
	print('r =', r)
	print('r[2] =', r[2])
	print('r[1:9:2] =', r[1:9:2])

def example_10():
	"""
	Функции getattr и setattr. Доступ к атрибутам.
	"""
	pfi()
	class Sample:
		def __init__(self):
			self.x = 1
			self.y = 2

	a = Sample()
	m('x'); print(a.x, getattr(a, 'x'))
	m('y'); print(a.y, getattr(a, 'y'))
	a.x = 11
	setattr(a, 'y', 22)
	setattr(a, '*z*', 33) # Атрибут с недопустимым именем
	m('x'); print(a.x, getattr(a, 'x'))
	m('y'); print(a.y, getattr(a, 'y'))
	m('*z*'); print(getattr(a, '*z*'))
	# m('*z*'); print(a.*z*) # => SyntaxError: invalid syntax

# Remote device emulation functions for example_11()
remote_voltage = 0
def get_voltage_from_remote_device():
	global remote_voltage
	print('getter: Voltage  is', remote_voltage, 'V')
	return remote_voltage
def set_voltage_on_remote_device(v):
	global remote_voltage
	remote_voltage = v
	print('setter: Set voltage', remote_voltage, 'V')
def error():
	print('deleter: ERROR: Device disconnected')

def example_11():
	"""
	Виртуальные атрибуты
	"""
	pfi()
	class VoltageRegulator:
		def __init__(self):
			self.v_exists = True
		def get_v(self):
			return get_voltage_from_remote_device() if self.v_exists else error()
		def set_v(self, v):
			set_voltage_on_remote_device(v) if self.v_exists else error()
		def del_v(self):
			self.v_exists = False
		v = property(get_v, set_v, del_v, "Voltage property")

	r = VoltageRegulator()
	r.v = 215
	print('Remote device voltage is', r.v, 'V')
	del r.v
	print('After del r.v voltage is', r.v)
	# help(r) # См. описание атрибута v в общей документации класса

def example_12():
	"""
	Управление созданием атрибутов
	"""
	pfi()
	class Sample:
		def __getattr__(self, name):
			return 'Unknown'
		def __setattr__(self, name, value):
			self.__dict__[name] = value.upper()

	d = Sample()
	m('d.__dict__'); print(d.__dict__) # => {}

	m('d.color 1'); print(d.color) # => Unknown
	d.color = 'green'
	m('d.color 2'); print(d.color) # => GREEN

	m('d.mode  1'); print(d.mode) # => Unknown
	d.mode = 'simple'
	m('d.mode  2'); print(d.mode) # => SIMPLE

	m('d.__dict__'); print(d.__dict__) # => {'color': 'GREEN', 'mode': 'SIMPLE'}

def example_13():
	"""
	Модификация процедуры создания атрибутов.
	Трассировка вызова методов. Необходимость
	непосредственного присваивания элементам
	словаря __dict__ для избежания бесконечной
	рекурсии.
	"""
	pfi()
	class Sample:
		def __init__(self):
			self.precision = '.5e-1'

		def __getattr__(self, name):
			"Вызывается для несуществующих атрибутов"
			print('<Trace: get', name, end='> ')
			return 'Unknown'

		def __setattr__(self, name, value):
			"Вызывается для всех атрибутов"
			print('<Trace: set', name, '=', value, end='>\n')
			# setattr(self, value, value.upper()) # => RecursionError: maximum recursion depth exceeded ...
			self.__dict__[name] = value.upper()

	d = Sample() # => <Trace: set precision = .5e-1>
	m('d.__dict__'); print(d.__dict__)
	m('d.color 1'); print(d.color) # => <Trace: get color> Unknown
	d.color = 'green' # => <Trace: set color = green>
	m('d.color 2'); print(d.color) # => d.color 2 => GREEN
	m('d.mode  1'); print(d.mode) # => d.mode  1 => <Trace: get mode> Unknown
	d.mode = 'simple' # => <Trace: set mode = simple>
	m('d.mode  2'); print(d.mode) # => d.mode  2 => SIMPLE
	m('d.precision'); print(d.precision) # => d.precision => .5E-1
	m('d.__dict__'); print(d.__dict__)

def example_14():
	"""
	Приведение к логическому типу, метод __bool__
	"""
	pfi()
	class A:
		def __bool__(self):
			return False

	class B:
		def __bool__(self):
			return True
	a = A()
	b = B()
	m('a and b'); print(a and b)
	m('a or  b'); print(bool(a) or bool(b))

from decimal import Decimal
from fractions import Fraction

def example_15():
	"""
	Приведение типа должно быть явным. Числа - исключение.
	Тип int автоматически преобразуется в Decimal.
	"""
	pfi()
	class A:
		def __int__(self):
			return 1
	a = A()
	#print(a + 1) # => TypeError: unsupported operand type(s) for +
	m('int(a) + 1'); print(int(a) + 1) # => 2
	m('1 + 2.2 + 3+5j + Fraction(6, 2)'); print(1 + 2.2 + 3+5j + Fraction(6, 2)) # => (9.2+5j)
	m('1 + Decimal(3)'); print(1 + Decimal(3)) # => 4
	#print(1.0 + Decimal(3)) # => TypeError: unsupported operand type(s) for +

def example_16():
	"""
	Придание объекту логического значения
	"""
	pfi()
	class EvenNumber:
		def __init__(self, n):
			self.n = n
		def __bool__(self):
			return bool(self.n % 2 == 0)

	i = EvenNumber(10)
	phdr('10 is even number')
	m("bool(i)"); print(bool(i))
	m("'abc' and i"); print('abc' and i)
	m("not i"); print(not i)

	j = EvenNumber(11)
	phdr('11 is odd number')
	m("bool(j)"); print(bool(j))
	m("[] or j"); print([] or j)
	m("not j"); print(not j)

if len(sys.argv) > 1 and sys.argv[1].isdigit() and int(sys.argv[1]) > 0:
	exec('example_%02d()' % int(sys.argv[1]))
else:
	tuple(map(lambda c: exec(c + '()'),
		(f for f in sys._getframe().f_code.co_names
			if f.startswith('example_'))))
