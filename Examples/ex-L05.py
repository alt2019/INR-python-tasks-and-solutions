#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def example_01():
	"""
	Определение и вызов функции
	"""
	print('\n*** Example 01 ***')
	def distance(a, b=0):
		value = a - b
		return value if value > 0 else -value

	# def distance3(a, b=0, c): # => SyntaxError: non-default argument
	#	pass                    # => follows default argument

	result = distance(2, 4)
	print('A: distance =', result) # => 2
	result = distance(3)
	print('B: distance =', result) # => 3

a = 10

def example_02():
	"""
	Глобальная переменная
	"""
	print('\n*** Example 02 ***')
	print('A:', a) # => 10, переменная a определенная на уровне модуля

def example_03():
	"""
	Создание локальной переменной с тем же именем,
	что и имя глобальной переменной
	"""
	print('\n*** Example 03 ***')
	# print(a) # UnboundLocalError: local variable 'a' referenced before assignment
	# print(b) # NameError: name 'b' is not defined
	a = 6 / 2
	print('A:', a) # => 3.0, a это локальная переменная

def example_04():
	"""
	Изменение глобальной переменной внутри функции
	"""
	print('\n*** Example 04 ***')
	global a
	print('A:', a) # => 10, переменная a определенная на уровне модуля
	a = 6 * 2
	print('B:', a) # => 12, переменная a определенная на уровне модуля

def example_05():
	"""
	Удаление переменной инструкцией del
	"""
	print('\n*** Example 05 ***')
	print('A:', a) # => 10 или 12, глобальная, изменена в функции example_04()
	b = 8
	print('B:', b) # => 8
	del b
	# print(b) # NameError: name 'b' is not defined

def example_06():
	"""
	Область видимости локальной переменной - вся функция
	"""
	print('\n*** Example 06 ***')
	a = 1
	if a > 0:
		b = 5
	# Локальная переменная b видна не только в своем блоке, но и во всей функции
	print(b) # => 5
	if a < 0:
		c = 5
	# Строка кода c = 5 не была исполнена, переменная c не существует
	# print(c) # UnboundLocalError: local variable 'c' referenced before assignment

def example_07():
	"""
	Объявление переменной как nonlocal
	"""
	print('\n*** Example 07 ***')
	a = 22
	def internal_fun():
		# здесь nonlocal a это переменная из объемлющей функции
		nonlocal a
		a = 33
	print('A:', a) # => 22
	internal_fun()
	print('B:', a) # => 33

def example_08():
	"""
	Вызов функции
	"""
	print('\n*** Example 08 ***')
	def fun(a, b=2, c=3):
		return (a + b) / c

	print('A:',fun(4, 5, 3)) # => 3.0
	fun(3, 5, 2) # Возвращаемое значение 4.0 отброшено

	m = [1, 2]
	print('Original m =', m)
	def swap_list(a):
		t = a[0]
		a[0] = a[1]
		a[1] = t
	print('Function without return returns', swap_list(m))
	print('Modified m =', m)
	def divide_with_check(a, b):
		if b == 0:
			return None, 'Error: divide by zero'
		return a / b, 'OK'
	value, status = divide_with_check(5, 0)
	print('divide_with_check(5, 0) => value =', value, ', status =', status)

def example_09():
	"""
	Использование значений по умолчанию
	"""
	print('\n*** Example 09 ***')
	def polynom(x=0, c0=0, c1=0, c2=0, c3=0, c4=0):
		return c0 + c1 * x**1 + c2 * x**2 + c3 * x**3 + c4 * x**4
	print('A:', polynom()) # => 0
	print('B:', polynom(c1=3, x=5)) # => 15
	print('C:', polynom(c2=2, c0=1, x=4)) # => 33
	print('D:', polynom(3, 2, 1)) # => 5
	# print('E:', polynom(3, c4=2, 1)) # Ошибка, после именованного параметра
	                                   # нельзя использовать позиционный

def example_10():
	"""
	Произвольное количество аргументов
	"""
	print('\n*** Example 10 ***')
	def fun(p1, p2, *pos_args, nam1, nam2, **nam_args):
		print('pos_args', pos_args.__class__, ', nam_args', nam_args.__class__)
		print(p1, p2, pos_args, nam1, nam2, nam_args)
	fun(1, 2, 3, 4, 5, nam1='one', nam2='two', nam3='three', last='End')
	# => 1 2 (3, 4, 5) one two {'nam3': 'three', 'last': 'End'}
	# Ошибка, попытка один и тот же аргумент передать дважды
	# fun(1, 2, 3, 4, 5, nam1='one', nam2='two', p1='three', last='End')

	def process_positional_argument(p):
		print('Positional:', p)

	def process_named_argument(n, v):
		print('Named:', n, '=', v)
	
	def fun2(*pos_args, **nam_args):
		print('=== fun2() === ')
		for p in pos_args: process_positional_argument(p)
		for n in nam_args: process_named_argument(n, nam_args[n])

	fun2()
	fun2(1, 2)
	fun2(1, color='white')
	# fun2(color='white', 1) # Ошибка: позиционный аргумент после именованного

def example_11():
	"""
	Моделирование функции dict()
	"""
	print('\n*** Example 11 ***')
	def adict(**nam_args):
		return nam_args
	print('adict =>', adict(color='white', brand='new', count=8))
	
	from copy import deepcopy
	def bdict(*pos_args, **nam_args):
		if len(pos_args) == 1 and isinstance(pos_args[0], dict):
			return deepcopy(pos_args[0])
		return nam_args
	print('bdict =>', bdict(color='white', brand='new', count=8))
	print('bdict =>', bdict({'a':1, 'b':2, 'last':'End'}))

def example_12():
	"""
	"""
	print('\n*** Example 12 ***')
	print('deep', 'copy', sep='') # => deepcopy  
	print('a', 1, end=' ')
	print('b', 2, end=' ')
	print('c', 3) # => a 1 b 2 c 3 
	print('Sample\nSecond line\nEnd', file=open("test.txt", "w"))

def example_13():
	"""
	Разложение последовательностей и словарей
	в параметры при вызове функции
	"""
	print('\n*** Example 13 ***')
	def polynom(x=0, c0=0, c1=0, c2=0, c3=0, c4=0, debug=False):
		if debug:
			print('x =', x, 'c0 =', c0, 'c1 =', c1,
		          'c2 =', c2, 'c3 =', c3, 'c4 =', c4)
		return c0 + c1 * x**1 + c2 * x**2 + c3 * x**3 + c4 * x**4

	pos_args = [ 3, 5 ]
	nam_args = { 'c4': 2, 'c3': 1 }
	polynom(11, *pos_args, debug=True, **nam_args)
	# => x = 11 c0 = 3 c1 = 5 c2 = 0 c3 = 1 c4 = 2
	# polynom(*pos_args, 11, **nam_args, debug=True) # В ранних версиях не работает
	# => x = 3 c0 = 5 c1 = 11 c2 = 0 c3 = 1 c4 = 2

def example_14():
	"""
	Аннотации
	"""
	print('\n*** Example 14 ***')
	import math
	def power(voltage: 'Напряжение в вольтах', current: 'Ток в амперах',
		phi: 'Сдвиг по фазе' = 0) -> 'Мощность в ваттах':
		return voltage * current * math.cos(phi)  
	print(power(voltage=220, current=0.01))
	print(power(voltage=220, current=0.01, phi=0.5))
	print(power.__annotations__)
	# => {'voltage': 'Напряжение в вольтах', 'current': 'Ток в амперах',
	# =>  'phi': 'Сдвиг по фазе', 'return': 'Мощность в ваттах'}
	power.new_attribute = 12
	print('New attribute of power() is', power.new_attribute)

def example_15():
	"""
	Совпадение имен переменных с именами аргументов функции
	"""
	print('\n*** Example 15 ***')
	def current(voltage, resistance):
		i = voltage / resistance
		return i

	def calculate_current_mA():
		voltage = 220
		resistance = 10000
		i = current(voltage=voltage, resistance=resistance)
		return int(i * 1000)

	print(calculate_current_mA()) # => 22

def example_16():
	"""
	Замыкания
	"""
	print('\n*** Example 16 ***')
	def create_fun(r):
		resistance = r
		test_no = 1
		def current_by_voltage(voltage):
			nonlocal test_no
			this_test_no = test_no
			test_no = test_no + 1
			return this_test_no, voltage / resistance
		return current_by_voltage

	f = create_fun(4)
	g = create_fun(2)
	print('f(12) =>', f(12)) # => (1, 3.0)  # (resistance == 4)
	print('g(12) =>', g(12)) # => (1, 6.0)  # (resistance == 2)
	print('f(20) =>', f(20)) # => (2, 5.0)  # (resistance == 4)
	print('g(20) =>', g(20)) # => (2, 10.0) # (resistance == 2)

def example_17():
	"""
	Лямбда-выражение
	"""
	print('\n*** Example 17 ***')
	import math
	f = lambda voltage, current, phi=0: voltage * current * math.cos(phi)
	print(f(220, 0.01))
	print(f(voltage=220, current=0.01, phi=0.5))

def example_18():
	"""
	Пример использования лямбда-выражения
	"""
	print('\n*** Example 18 ***')
	d = [ "Иван Петров", "Георгий Иванов", "Валерий Сидоров" ]
	print(d)
	print(sorted(d))
	print(sorted(d, key=lambda s: s.split()[1]))

def example_19():
	"""
	Лямбда-выражение в цикле
	"""
	print('\n*** Example 19 ***')
	print('Лямбда-выражение в цикле')
	def create_functions():
		a = []
		for i in range(1, 4):
			a.append(lambda x: x * i)
		return a
	for e in create_functions():
		print(e(10), end=' ') # => 30 30 30

	print('\nЛямбда-выражение с аргументом по умолчанию в цикле')
	def create_functions2():
		a = []
		for i in range(1, 4):
			a.append(lambda x, y=i: x * y)
		return a
	for e in create_functions2():
		print(e(10), end=' ') # => 10 20 30

def example_20():
	"""
	Определение функции в цикле
	"""
	print('\n*** Example 20 ***')
	
	print('Определение функции в цикле')
	a = []
	for i in range(1, 4):
		def f(x):
			return x * i
		a.append(f)
	for e in a:
		print(e(10), end=' ') # => 30 30 30

	print('\nОпределение функции с аргументом по пумолчанию в цикле')
	a = []
	for i in range(1, 4):
		def f(x, y=i):
			return x * y
		a.append(f)
	for e in a:
		print(e(10), end=' ') # => 10 20 30

z = 9999
def example_21():
	"""
	Инструкция nonlocal
	"""
	print('\n*** Example 21 ***')
	print('\nИнструкция nonlocal')
	def fun1():
		a = 1
		b = 11
		c = 111
		def fun2():
			a = 2
			b = 22
			def fun3():
				a = 3
				def fun4():
					#nonlocal a, b, c, z # => SyntaxError: no binding for nonlocal 'z' found
					nonlocal a, b, c
					print(a, b, c)
				return fun4
			return fun3
		return fun2
	fun1()()()() # => 3 22 111
	
def example_22():
	"""
	Рекурсия
	"""
	print('\n*** Example 22 ***')
	print('\nРекурсия')
	def plr(a):
		if a:
			e = a.pop()
			print('before', e)
			plr(a)
			print('after ', e)
	plr([ 1, 2, 3, 4 ])

aa = 10

def example_23():
	"""
	Инструкция global
	"""
	print('\n*** Example 23 ***')
	print('\nИнструкция global')

	def fun1():
		print(aa)

	def fun2():
		aa = 11
		print(aa)

	def fun3():
		global aa
		aa = 22
		print(aa)

	fun1()    # => 10
	fun2()    # => 11
	print(aa) # => 10
	fun3()    # => 22
	print(aa) # => 22

# Comment-out tests you like to skip with '#' character

example_01()
example_02()
example_03()
example_04()
example_05()
example_06()
example_07()
print('C:', a) # => 12
example_08()
example_09()
example_10()
example_11()
example_12()
example_13()
example_14()
example_15()
example_16()
example_17()
example_18()
example_19()
example_20()
example_21()
example_22()
example_23()
