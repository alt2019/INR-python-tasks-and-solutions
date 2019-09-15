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

def phdr(s):
	"Paragraph header"
	h = '=' * 3
	print('   ', h, s, h)

def m(s):
	"Print mark at line begin"
	print(s + ' => ', end='')

def example_01():
	"""
	Наследование от встроенного класса list
	"""
	pfi()

	class Results(list):
		def __getitem__(self, i):
			'Перепрограммирование оператора []'
			return str(list.__getitem__(self, i)) + ' V'

	r = Results([187, 193, 202, 215, 226, 239])
	r.append(241)
	del r[4]
	print('r[2]:', r[2]) # => r[2]: 202 V
	# Итератор не перепрограммирован !
	print('ra:', r) # => ra: [187, 193, 202, 215, 239, 241]
	print('rb:', [r[i] for i in range(len(r))]) # => rb: ['187 V', '193 V', '202 V', '215 V', '239 V', '241 V']
	
def example_02():
	"""
	Делегирование
	"""
	pfi()

	class ResultsReader:
		"""
		Класс ResultsReader является массивом результатов
		измерений доступных только по чтению
		"""
		def __init__(self, obj):
			self.obj = obj
		def __getitem__(self, i):
			'Перепрограммирование оператора []'
			return str(self.obj[i]) + ' V'
		def __len__(self):
			'Метод __len__ вызывается функцией len()'
			return len(self.obj)

	r = ResultsReader([187, 193, 202, 215, 226, 239])
	# r.append(241) # append не существует
	# r[2] = 241    # элемент не модифицируется
	# del r[4]      # del не поддерживается
	print('r[2]:', r[2]) # => r[2]: 202 V
	# Итератор не существует
	print('ra:', r) # => <__main__.example_02.<locals>.ResultsReader object at 0x7f025dc3d198>
	print('rb:', [r[i] for i in range(len(r))]) # => rb: ['187 V', '193 V', '202 V', '215 V', '226 V', '239 V']
	
def example_03():
	"""
	Конфликт имен атрибутов
	"""
	pfi()

	class DevA:
		def __init__(self):
			self.precision = 0.02
		def prec(self):
			print('DevA:', self.precision)
			return self.precision

	class DevB:
		def __init__(self):
			self.precision = 0.05
		def prec(self):
			print('DevB:', self.precision)
			return self.precision

	class Dev(DevA, DevB):
		def __init__(self):
			DevA.__init__(self)
			DevB.__init__(self)
		def prec_a(self): return DevA.prec(self)
		def prec_b(self): return DevB.prec(self)

	d = Dev()
	d.prec()   # => DevA: 0.05
	d.prec_a() # => DevA: 0.05
	d.prec_b() # => DevB: 0.05
	print([a for a in dir(d) if 'prec' in a])
	# => ['prec', 'prec_a', 'prec_b', 'precision']
	print(d.precision) # => 0.05

def example_04():
	"""
	Использование псевдочастных атрибутов
	для разрешения конфликта имен
	"""
	pfi()

	class DevA:
		def __init__(self):
			self.__precision = 0.02
		def prec(self):
			print('DevA:', self.__precision)
			return self.__precision

	class DevB:
		def __init__(self):
			self.__precision = 0.05
		def prec(self):
			print('DevB:', self.__precision)
			return self.__precision
		def __prec2(self):
			pass

	class Dev(DevA, DevB):
		def __init__(self):
			DevA.__init__(self)
			DevB.__init__(self)
		def prec_a(self): return DevA.prec(self)
		def prec_b(self): return DevB.prec(self)

	d = Dev()
	d.prec()   # => DevA: 0.02
	d.prec_a() # => DevA: 0.02
	d.prec_b() # => DevB: 0.05
	print([a for a in dir(d) if 'prec' in a])
	# => ['_DevA__precision', '_DevB__prec2', '_DevB__precision', 'prec', 'prec_a', 'prec_b']
	# print(d.precision) # => AttributeError: 'Dev' object has no attribute 'precision'

	# Зная правила модификации можно получить доступ к псевдочастным атрибутам
	print(d._DevA__precision) # => 0.02
	d._DevB__precision = 0.09
	print(d._DevB__precision) # => 0.09

	# Mодификация имени атрибута осуществляется в реализации класса
	print([a for a in dir(DevA()) if 'prec' in a])
	# => ['_DevA__precision', 'prec']

	# ... и следовательно происходит и при единичном наследовании
	class DevC(DevA):
		def __init__(self):
			DevA.__init__(self)

	print([a for a in dir(DevC()) if 'prec' in a])
	# => ['_DevA__precision', 'prec']

def example_05():
	"""
	Функция super()
	"""
	pfi()

	class DevBP:
		def __init__(self):
			self.__precision = 0.01
		def prec(self):
			print('DevBP:', self.__precision)
			return self.__precision

	class DevA:
		def __init__(self):
			self.__precision = 0.02
		def prec(self):
			print('DevA:', self.__precision)
			return self.__precision

	class DevB(DevBP):
		def __init__(self):
			self.__precision = 0.05
		def prec(self):
			print('DevB:', self.__precision)
			return self.__precision
		def __prec2(self):
			pass

	class Dev(DevA, DevB):
		def __init__(self):
			DevA.__init__(self)
			DevBP.__init__(self)
			DevB.__init__(self)
		def prec_a(self): return DevA.prec(self)
		def prec_b(self): return DevB.prec(self)

		def prec(self):
			return super().prec()
		def prec_dev(self):
			return super(Dev, self).prec()
		def prec_a(self):
			return super(DevA, self).prec()
		def prec_b(self):
			return super(DevB, self).prec()

	d = Dev()
	d.prec()       # => DevA: 0.02
	d.prec_dev()   # => DevA: 0.02
	d.prec_a()     # => DevB: 0.05
	d.prec_b()     # => DevBP: 0.01

def example_06():
	"""
	Использование функции super() для вызова метода __init__()
	"""
	pfi()

	class A:
		def __init__(self, *pargs, **nargs):
			print('Call A.__init__()')
			super().__init__(*pargs, **nargs) # Будет вызван B.__init__()

	class B:
		def __init__(self, *pargs, **nargs):
			print('Call B.__init__()')
			super().__init__() # Будет вызван object.__init__()

	class C(A, B):
		def __init__(self, *pargs, **nargs):
			print('Call C.__init__()')
			super().__init__(*pargs, **nargs) # Будет вызван A.__init__()

	# Поиск метода происходит в последовательности
	# хранящейся в атрибуте __mro__ (Method Resolution Order).
	# Атрибут __mro__ вычисляется по алгоритму C3-линеаризации.
	print('C.__mro__ =', [v.__name__ for v in C.__mro__]) # => [C, A, B, object]

	c = C()
	# => Call C.__init__()
	# => Call A.__init__()
	# => Call B.__init__()
	
	print()
	phdr('Явный вызов метода __init__ класса object')
	# В классе object метод __init__ не делает ничего (?)
	print('object.__init__(None) return', object.__init__(None))

	 
def example_07():
	"""
	Изменение наследования во время исполнения программы
	"""
	pfi()
	class Empty:
		pass

	class A(Empty):
		def f(self):
			print('call A.f()')

	class B:
		def f(self):
			print('call B.f()')
		def m1(self):
			del A.f
		def m2(self):
			A.__bases__ = (C, B)

	class C:
		def f(self):
			print('call C.f()')

	# Классы A и B это интерфейс к библиотеке
	# Они предоставляют методы f, m1 и m2

	class X(A, B):
		'Пользовательский класс X'
		def f(self):
			'Расширение библиотечной функции f'
			print('In class X', end=' ')
			super().f()

	x = X()
	x.f() # => In class X call A.f()
	x.m1()
	x.f() # => In class X call B.f()
	print('X.__mro__ =', [v.__name__ for v in X.__mro__]) # => [X, A, Empty, B, object]
	x.m2()
	print('X.__mro__ =', [v.__name__ for v in X.__mro__]) # => [X, A, C, B, object]
	x.f() # => In class X call C.f()

def example_08():
	"""
	Связанные методы
	"""
	pfi()

	class DevA:
		def __init__(self):
			self.precision = 0.02
		def prec(self):
			print('DevA:', self.precision)
			return self.precision

	class DevB:
		def __init__(self):
			self.precision = 0.05
		def prec(self):
			print('DevB:', self.precision)
			return self.precision

	da = DevA()
	db = DevB()
	m('da.prec()'); da.prec() # => DevA: 0.02
	mu = DevA.prec
	m('mu(da)'); mu(da) # => DevA: 0.02
	m('mu(db)'); mu(db) # => DevA: 0.05 # Метод класса DevA применен к объекту класса DevB
	mba = da.prec
	mbb = db.prec
	m('mba()'); mba() # => DevA: 0.02
	m('mbb()'); mbb() # => DevB: 0.05
	print(mu)  # => function
	print(mba) # => bound method
	
	phdr('Bound method implementation')
	print('dir(mba) =>', dir(mba))
	print(mba.__class__) # => <class 'method'>
	print(mba.__self__ is da) # => True
	print(mba.__func__ is DevA.prec) # => True
	mba.__func__(mba.__self__) # => DevA: 0.02

def example_09():
	"""
	Статические методы и методы класса
	"""
	pfi()

	class Dev:
		_num_instances = 0

		def __init__(self):
			Dev._num_instances += 1

		# Обычный метод (метод объекта), аргумент self это объект
		def instance_method(self):
			print('Instance method, total ', Dev._num_instances, ', argument is', self)

		# Статический метод, нет аргумента self
		def static_method():
			print('Static method,   total ', Dev._num_instances, ', no arguments')
		static_method = staticmethod(static_method)

		# Метод класса, один аргумент, аргумент cls это класс
		def class_method(cls):
			print('Class method,    total ', cls._num_instances, ', argument is', cls)
		class_method = classmethod(class_method)

	# Обычный метод вызывается как атрибут объекта
	xa = Dev()
	xa.instance_method() # => 1
	# или объект нужно передать как аргумент
	Dev.instance_method(xa) # => 1

	# Статический метод вызывается как атрибут объекта, так и атрибут класса
	xb = Dev()
	xb.static_method() # => 2
	Dev.static_method() # => 2

	# Метод класса вызывается как атрибут объекта, так и атрибут класса
	xc = Dev()
	xc.class_method() # => 3
	Dev.class_method() # => 3

def example_10():
	"""
	Статические методы и методы класса
	Идентичен предыдущему примеру,
	но с использованием декораторов
	"""
	pfi()

	class Dev:
		_num_instances = 0

		def __init__(self):
			Dev._num_instances += 1

		# Обычный метод (метод объекта), аргумент self это объект
		def instance_method(self):
			print('Instance method, total ', Dev._num_instances, ', argument is', self)

		# Статический метод, нет аргумента self
		@staticmethod
		def static_method():
			print('Static method,   total ', Dev._num_instances, ', no arguments')

		# Метод класса, один аргумент, аргумент cls это класс
		@classmethod
		def class_method(cls):
			print('Class method,    total ', cls._num_instances, ', argument is', cls)

	# Обычный метод вызывается как атрибут объекта
	xa = Dev()
	xa.instance_method() # => 1
	# или объект нужно передать как аргумент
	Dev.instance_method(xa) # => 1

	# Статический метод вызывается как атрибут объекта, так и атрибут класса
	xb = Dev()
	xb.static_method() # => 2
	Dev.static_method() # => 2

	# Метод класса вызывается как атрибут объекта, так и атрибут класса
	xc = Dev()
	xc.class_method() # => 3
	Dev.class_method() # => 3

def test_thermometer(thermometer, with_default=True):
	m('Channel 0'); print(thermometer(0))
	m('Channel 1'); print(thermometer(1))
	m('Channel 2'); print(thermometer(2))
	m('Channel 3'); print(thermometer(3))
	m('Channel 4'); print(thermometer(4))
	if with_default:
		m('Default  '); print(thermometer())

def example_11():
	"""
	Плохо работающий четырехканальный
	термометр (температура воды)
	"""
	pfi()
	def four_channels_thermometer(channel):
		if channel == 0: return 20
		elif channel == 1: return 35
		elif channel == 2: return 107
		elif channel == 3: return -3
		else:
			print('ERROR: Invalid channel', channel, end=', ')
			return None

	test_thermometer(four_channels_thermometer, with_default=False)

def example_12():
	"""
	Исправленный четырехканальный термометр
	"""
	pfi()
	# Функция-декоратор - корректор
	def corrector(fun):
		def corrected_fun(channel=0):
			if channel < 0 or channel >= 4:
				channel = 0
			t = fun(channel)
			if t < 0: t = 0
			if t > 100: t = 100
			return t
		return corrected_fun

	@corrector
	def four_channels_thermometer(channel):
		if channel == 0: return 20
		elif channel == 1: return 35
		elif channel == 2: return 107
		elif channel == 3: return -3
		else:
			print('ERROR: Invalid channel', channel, end=', ')
			return None

	test_thermometer(four_channels_thermometer)

def example_13():
	"""
	Реализация декоратора в виде класса
	"""
	pfi()
	class corrector:
		'Класс-декоратор - корректор'
		def __init__(self, fun):
			self.fun = fun
		def __call__(self, channel=0):
			if channel < 0 or channel >= 4:
				channel = 0
			t = self.fun(channel)
			if t < 0: t = 0
			if t > 100: t = 100
			return t

	@corrector
	def four_channels_thermometer(channel):
		if channel == 0: return 20
		elif channel == 1: return 35
		elif channel == 2: return 107
		elif channel == 3: return -3
		else:
			print('ERROR: Invalid channel', channel, end=', ')
			return None
	test_thermometer(four_channels_thermometer)

def example_14():
	"""
	Декоратор в виде класса неприменим к методам
	"""
	pfi()
	class decor:
		def __init__(self, f):
			self.f = f
		def __call__(self):
			print('Call decor.__call__(', self.__class__, ')')
			self.f(self)
	class X:
		def fun(self):   # fun это метод класса X
			             # self это объект класса X
			print('Call fun(', self.__class__, ')')
		fun = decor(fun) # теперь fun это объект класса decor
	m = X()
	phdr('m.fun()')
	m.fun() # => decor.__call__(X.fun) # параметр это объект класса decor
	phdr('decor.__call__(X.fun)')
	decor.__call__(X.fun)

def example_15():
	"""
	Декоратор в виде класса неприменим к методам.
	Атрибут декорируемого класса теряется и замещается
	атрибутом класса-декоратора, если такой есть.
	Декоратор в виде функции дает правильный результат.
	"""
	pfi()
	class corrector_class:
		'Класс-декоратор - корректор'
		def __init__(self, fun):
			self.fun = fun
			self.serial = 999999
		def __call__(self, channel=0):
			if channel < 0 or channel >= 4:
				channel = 0
			# self это объект класса corrector_class. Доступ к атрибутам
			# класса, чей метод был декорирован, утерян.
			t, serial = self.fun(self, channel)
			if t < 0: t = 0
			if t > 100: t = 100
			return t, serial

	def corrector_functuion(fun):
		def corrected_fun(self, channel=0):
			if channel < 0 or channel >= 4:
				channel = 0
			t, serial = fun(self, channel)
			if t < 0: t = 0
			if t > 100: t = 100
			return t, serial
		return corrected_fun

	class Lab:
		def __init__(self, serial):
			self.serial = serial
		@corrector_class
		def four_channels_thermometer(self, channel):
			if channel == 0: return (20, self.serial)
			elif channel == 1: return (35, self.serial)
			elif channel == 2: return (107, self.serial)
			elif channel == 3: return (-3, self.serial)
			else:
				print('ERROR: Invalid channel', channel, end=', ')
				return None
		@corrector_functuion
		def four_channels_thermometer2(self, channel):
			if channel == 0: return (20, self.serial)
			elif channel == 1: return (35, self.serial)
			elif channel == 2: return (107, self.serial)
			elif channel == 3: return (-3, self.serial)
			else:
				print('ERROR: Invalid channel', channel, end=', ')
				return None

	lab = Lab(123456)
	# В функцию test_thermometer передаются связанные методы
	phdr('corrector_class')
	test_thermometer(lab.four_channels_thermometer)
	phdr('corrector_functuion')
	test_thermometer(lab.four_channels_thermometer2)

def example_16():
	"""
	Декоратор с параметрами
	"""
	pfi()
	class Button:
		def __init__(self):
			self.color = 'White'
			self.__callback = None
		def set_callback(self, callback):
			self.__callback = callback
		def click(self):
			print(self.color, 'button clicked: ', end='')
			if self.__callback:
				self.__callback()

	button_open = Button()
	button_help = Button()
	button_test = Button()
	
	def callback_decorator(button, color):
		def real_decorator(fun):
			button.color = color
			button.set_callback(fun)
			return fun
		return real_decorator

	@callback_decorator(button_open, 'Green')
	def open_message():
		print('Open file')

	def help_message():
		print('Help on application')
	help_message = callback_decorator(button_help, 'Yellow')(help_message)

	button_open.click() # => Green button clicked: Open file
	button_help.click() # => Yellow button clicked: Help on application
	button_test.click() # => White button clicked:
	print()

def example_17():
	"""
	Декоратор класса в виде функции
	"""
	pfi()

	def wrapper(cls):
		class WrappingClass(cls):
			def new_method(self):
				print('New method')
			def prec(self):
				print('Customized message for ', end='')
				return cls.prec(self)
		return WrappingClass

	@wrapper
	class Dev:
		def __init__(self):
			self.precision = 0.02
		def prec(self):
			print('Dev:', self.precision)
			return self.precision
	# Dev = wrapper(Dev) # Альтернатива синтаксису @wrapper
		
	d = Dev()
	print(d.prec())
	d.new_method()
	print(Dev)
	
def example_18():
	"""
	Декоратор класса в виде класса
	"""
	pfi()

	class wrapper():
		def __init__(self, cls):
			self.cls = cls
		def __call__(self):
			Parent = self.cls
			class WrappingClass(Parent):
				def new_method(self):
					print('New method')
				def prec(self):
					print('Customized message for ', end='')
					return Parent.prec(self)
			return WrappingClass()

	@wrapper
	class Dev:
		def __init__(self):
			self.precision = 0.02
		def prec(self):
			print('Dev:', self.precision)
			return self.precision
	# Dev = wrapper(Dev) # Альтернатива синтаксису @wrapper
		
	d = Dev()
	print(d.prec())
	d.new_method()
	print(Dev)

def example_19():
	"""
	Декораторы для создания виртуальных
	атрибутов или свойств (property)
	"""
	pfi()

	def error():
		print('deleter: ERROR: Device disconnected')

	class VoltageRegulator:
		def __init__(self):
			self.v_exists = True
			self.voltage = 0
		@property
		def v(self):
			"Voltage property"
			return self.voltage if self.v_exists else error()
		@v.setter
		def v(self, v):
			self.voltage = v if self.v_exists else error()
		@v.deleter
		def v(self):
			self.v_exists = False

	r = VoltageRegulator()
	r.v = 215
	print('Remote device voltage is', r.v, 'V')
	del r.v
	print('After del r.v voltage is', r.v)
	# help(r) # См. описание атрибута v в общей документации класса
	
if len(sys.argv) > 1 and sys.argv[1].isdigit() and int(sys.argv[1]) > 0:
	exec('example_%02d()' % int(sys.argv[1]))
else:
	tuple(map(lambda c: exec(c + '()'),
		(f for f in sys._getframe().f_code.co_names
			if f.startswith('example_'))))
