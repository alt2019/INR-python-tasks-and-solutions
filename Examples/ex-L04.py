#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def example_01():
	"""
	Составная конструкция языка
	"""
	print('\n*** Example 01 ***')
	def eat_apples(n):
		print('We ate %d apples' % n)
	def eat_pears(n):
		print('We ate %d apples' % n)
	def get_more_fruits():
		print('We got more fruits')

	apples = 4
	pears = 2
	if apples > pears:
		eat_apples(apples - pears)
		print('We ate extra apples')
	else:
		eat_pears(pears - apples)
		print('We ate extra pears')
	get_more_fruits()

def example_02():
	"""
	Компактная запись
	"""
	print('\n*** Example 02 ***')
	a = 1; b = 2; c = a + b; print('A: c =', c) # Несколько инструкций в строке
	if c < 5: a = 5 ; print('B: a =', a) # Блок из двух инструкций, оба исполняются
	if c > 5: a = 9 ; print('C: a =', a) # Блок из двух инструкций, оба НЕ исполняются
	# if c < 5: if b == 2: print('C: Two ifs') # Ошибка: инструкция внутри однострочного блока
	if c < 5:
		if b == 2: print('D: Two ifs in proper notation')
	# if c < 5: print('less') else: print('greater') # Ошибка, второе двоеточие в строке недопустимо
	if c < 5: print('Е: less') # В две строки -
	else: print('Е: greater')  # правильно

def example_03():
	"""
	Инструкция if
	"""
	print('\n*** Example 03 ***')
	t = 105
	if t < 0:
		t = 0
	elif t > 100:
		t = 100
	else:
		# Функция fix_drift() не определена, но при данном
		# значении t она не будет вызвана, ошибки не будет
		t = fix_drift(t)
	print('t =', t)

def example_04():
	"""
	Несколько блоков elif
	"""
	print('\n*** Example 04 ***')
	s = 'three'
	if s == 'zero' or s == 'null' or s == 'nil':
		print(0)
	elif s == 'one':
		print(1)
	elif s == 'two':
		print(2)
	elif s == 'three':
		print(3)
	elif s == 'four':
		print(4)
	elif s == 'five':
		print(5)
	else:
		print(-1)

def example_05():
	"""
	Альтернатива нескольким блокам elif
	"""
	print('\n*** Example 05 ***')
	d = {
		'zero':  0,
		'null':  0,
		'nil':   0,
		'one':   1,
		'two':   2,
		'three': 3,
		'four':  4,
		'five':  5
	}
	print('A:', d.get('three', -1))  # Второй параметр get() это значение
	print('B:', d.get('twenty', -1)) # возвращаемое для ненайденного ключа,
	print('C:', d.get('fifty'))      # по умолчанию None

def example_06():
	"""
	Трактовка объектов как логических величин
	"""
	print('\n*** Example 06 ***')
	def print_true(s):
		print(s, 'is True')
	def print_false(s):
		print(s, 'is False')
	print('=== Print falses first ===')
	if False: print_true('Literal False')
	else: print_false('Literal False')
	if None: print_true('Literal None')
	else: print_false('Literal None')
	if '': print_true('Empty string')
	else: print_false('Empty string')
	if b'': print_true('Empty bytes object')
	else: print_false('Empty bytes object')
	if bytearray(b''): print_true('Empty bytearray')
	else: print_false('Empty bytearray')
	if []: print_true('Empty list')
	else: print_false('Empty list')
	if tuple(): print_true('Empty tuple')
	else: print_false('Empty tuple')
	if {}: print_true('Empty dict')
	else: print_false('Empty dict')
	if set(): print_true('Empty set')
	else: print_false('Empty set')
	if 0: print_true('Integer zero')
	else: print_false('Integer zero')
	if 0.0: print_true('Real zero')
	else: print_false('Real zero')
	print('=== Then print trues ===')
	if True: print_true('Literal True')
	else: print_false('Literal True')
	if 'a': print_true('Non-empty string')
	else: print_false('Non-empty string')
	if b'a': print_true('Non-empty bytes object')
	else: print_false('Non-empty bytes object')
	if bytearray(b'a'): print_true('Non-empty bytearray')
	else: print_false('Non-empty bytearray')
	if [1]: print_true('Non-empty list')
	else: print_false('Non-empty list')
	if (1, 2): print_true('Non-empty tuple')
	else: print_false('Non-empty tuple')
	if {1: 2}: print_true('Non-empty dict')
	else: print_false('Non-empty dict')
	if {1}: print_true('Non-empty set')
	else: print_false('Non-empty set')
	if 1: print_true('Non-zero integer')
	else: print_false('Non-zero integer')
	if 1.0: print_true('Non-zero real')
	else: print_false('Non-zero real')
	if ...: print_true('Ellipsis ...')
	else: print_false('Ellipsis ...')

def example_07():
	"""
	Операторы and и or
	"""
	print('\n*** Example 07 ***')
	def less2(n):
		print('Call less2(', n, ') =>', n < 2)
		if n < 2: return True
		else: return False

	a = less2(1) and less2(2) and less2(3) and less2(4) 
	print('A:', a) # => False
	b = less2(2) or less2(1) or less2(0) or less2(4) 
	print('B:', b) # => True

def example_08():
	"""
	Особенности операторов and и or
	"""
	print('\n*** Example 08 ***')
	a = [] or { 1, 2, 3 } or 'LastToken'
	print('A:', a) # => { 1, 2, 3 }
	b = { 1, 2, 3 } or [] or 'LastToken'
	print('B:', b) # => { 1, 2, 3 }
	c = [ 1, 2 ] and { 1, 2, 3 } and 'LastToken'
	print('C:', c) # => 'LastToken'
	d = [ 1, 2 ] and [] and 'LastToken'
	print('D:', d) # => []
	e = [ 1, 2 ] and not { 1, 2, 3 }
	print('E:', e) # => False
	# Приоритет оператора and выше чем оператора or
	f =  1 or 2  and  0 or 3
	print('F:', f) # => 1
	g = (1 or 2) and (0 or 3)
	print('G:', g) # => 3

def example_09():
	"""
	Трехместный оператор if/else
	"""
	print('\n*** Example 09 ***')
	x = -3
	sign = 'plus' if x >= 0 else 'minus'
	print('sign is', sign)
	# Трехместный оператор if/else имеет очень низкий приоритет,
	# в выражениях его всегда следует помещать в скобки
	print('The result is ' + ('plus' if x >= 0 else 'minus') +
	' ' + str(x if x >= 0 else -x) + ' => Right')
	# Результат без скобок
	print('The result is ' + 'plus' if x >= 0 else 'minus' +
	' ' + str(x if x >= 0 else -x) + ' => Wrong')

def example_10():
	"""
	Цикл while
	"""
	print('\n*** Example 10 ***')
	print('=== Start loop 1 === ')
	n = 1
	while n < 10:
		print('Loop:', n)
		n = n * 2
		if n == 8:
			print('break')
			break;
	else:
		print('Else:', n)

	print('=== Start loop 2 === ')
	n = 1
	while n < 10:
		print('Loop:', n)
		n = n * 2
	else:
		print('Else:', n)

def example_11():
	"""
	Цикл while с пустым блоком и побочным
	эффектом в условии
	"""
	print('\n*** Example 11 ***')
	def eat_apple(d):
		total_apples = d.get('apples', 0)
		if total_apples <= 0:
			return False
		d['apples'] = total_apples - 1
		print('We ate one apple')
		return True

	fruits = { 'apples': 4, 'pears': 6 }
	while eat_apple(fruits):
		pass

def example_12():
	"""
	Объект Ellipsis
	"""
	print('\n*** Example 12 ***')
	def eat_apple(d):
		total_apples = d.get('apples', 0)
		if total_apples <= 0:
			return False
		d['apples'] = total_apples - 1
		print('We ate one apple')
		return True

	fruits = { 'apples': 4, 'pears': 6 }
	while eat_apple(fruits):
		...
	a = ...
	if a == ...:
		print('a is a ... of', a.__class__)
	if a == Ellipsis:
		print('a is an Ellipsis of', a.__class__)

def example_13():
	"""
	Цикл for
	"""
	print('\n*** Example 13 ***')
	print('=== Start loop 1 === ')
	for n in (1, 2, 'three', 4, 5):
		print('Loop:', n)
		if n == 4:
			break;
	else:
		print('Else:', n)

	print('=== Start loop 2 === ')
	for n in (1, 2, 'three', 4, 5):
		print('Loop:', n)
	else:
		print('Else:', n)

def example_14():
	"""
	Встроенная функция range
	"""
	print('\n*** Example 14 ***')
	print('=== Start loop 1 === ')
	for i in range(10, 15): # => 10, 11, 12, 13, 14
		print('i =', i)
	print('=== Start loop 2 === ')
	for i in range(10, 15, 2): print('i =', i) # => 10, 12, 14
	print('=== Start loop 3 === ')
	for i in range(3): print('i =', i) # => 0, 1, 2

def example_15():
	"""
	Словарь в цикле for
	"""
	print('\n*** Example 15 ***')
	fruits = { 'apples': 4, 'pears': 6, 'plums': 8 }
	print('=== Start loop 1 === ')
	for key in fruits:
		print(key, '=', fruits[key])
	print('=== Start loop 2 === ')
	for value in fruits.values():
		print(value)

def example_16():
	"""
	Словарь в цикле for, выборка элементов
	"""
	print('\n*** Example 16 ***')
	fruits = { 'apples': 4, 'pears': 6, 'plums': 8 }
	print('=== Start loop 1 === ')
	for element in fruits.items():
		print(element, element.__class__)
	print('=== Start loop 2 === ')
	for element in fruits.items():
		print('key =', element[0], 'value =', element[1])
	print('=== Start loop 3 === ')
	for (key, value) in fruits.items():
		print('key =', key, 'value =', value)

def example_17():
	"""
	Расширенная инструкция присваивания
	или присваивание последовательностей
	"""
	print('\n*** Example 17 ***')
	m = (1, 2, 3, 4, 5) ; print('A:', 'm =', m)
	(a, b, c, d, e) = (1, 2, 3, 4, 5) ; print('B:', 'a =', a, 'b =', b, 'c =', c, 'd =', d, 'e =', e)
	a, b, c, d, e = 1, 2, 3, 4, 5 ; print('C:', 'a =', a, 'b =', b, 'c =', c, 'd =', d, 'e =', e)
	a, b, c, d, e = [ 1, 2, 3, 4, 5 ] ; print('D:', 'a =', a, 'b =', b, 'c =', c, 'd =', d, 'e =', e)
	a, b, c, d, e = "abcde" ; print('E:', 'a =', a, 'b =', b, 'c =', c, 'd =', d, 'e =', e)
	a, b, c, d, e = { 1, 2, 3, 4, 5 } ; print('F:', 'a =', a, 'b =', b, 'c =', c, 'd =', d, 'e =', e)
	a, b, c, d, e = { 'a':1, 'b':2, 'c':3, 'd':4, 'e':5 } ; print('G:', 'a =', a, 'b =', b, 'c =', c, 'd =', d, 'e =', e)
	(*keys,) = { 'a':1, 'b':2, 'c':3, 'd':4, 'e':5 } ; print('H:', 'keys =', keys)
	a, *x, d, e = 1, 2, 3, 4, 5 ; print('I:', 'a =', a, 'x =', x, 'd =', d, 'e =', e)
	a, *x, c, d, e = 1, 2, 3, 4, 5 ; print('J:', 'a =', a, 'x =', x, 'c =', c, 'd =', d, 'e =', e)
	# a, *x, *y, e = 1, 2, 3, 4, 5 # => Ошибка - две конструкции *переменная
	# a, b, c, d, e = "abc" # => Ошибка - недостаточно величин для заполнения кортежа
	# a, b, c, d, e = "abcdef" # => Ошибка - слишком много величин

def example_18():
	"""
	Соединение последовательностей
	Встроенная функция zip
	"""
	print('\n*** Example 18 ***')
	names = 'apples', 'pears', 'plums'
	values = 4, 6, 8
	d = dict(zip(names, values))
	print('A:', 'd =', d)
	# zip соединяет любое количество последовательностей
	z = zip(names, values, 'abc', reversed(values))
	print('B:', 'z =', z)
	print('C:', 'z =', list(z))
	# Длинна результата это длинна самой короткой исходной последовательности
	x = zip(
		(1, 2, 3),
		(1, 2, 3, 4),
		(1, 2),
		(1, 2, 3, 4, 5)
	)
	print('x =', list(x)) # => x = [(1, 1, 1, 1), (2, 2, 2, 2)]
	

def example_19():
	"""
	Генераторы коллекций
	"""
	print('\n*** Example 19 ***')
	a = [-n if n < 0 else n + 10 for n in (-2, -1, 0, 1, 2)]
	print('A:', 'a =', a) # => [ 2, 1, 10, 11, 12 ]
	d = { 'name': 'abcd', 'f1': 14, 5: 27.12, 'pair': [ 1, 2 ] }
	b = [ print('key =', key, 'value =', value) for key, value in d.items() ]
	print('B:', 'b =', b)
	c = ( print('key =', key, 'value =', value) or 
	    str(key) + '/' +  str(value) 
	    for key, value in d.items() )
	# В качестве кортежа создается объект-генератор эмулирующий кортеж:
	print('C:', 'c =', tuple(c), c.__class__)
	e = { 'char ' + chr(65 + i): i + 10 for i in range(4) }
	print('E:', 'e =', e, e.__class__) # => {'char C': 12, 'char B': 11, 'char A': 10, 'char D': 13}
	x = 20
	s = { i + x for i in range(4) }
	print('S:', 's =', s, s.__class__) # => { 20, 21, 22, 23 }

def example_20():
	"""
	Итераторы 1
	"""
	print('\n*** Example 20 ***')
	a = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
	i1 = iter(a)
	i2 = iter(a)
	while True:
		e1 = next(i1, None)
		if e1 == None:
			break
		if e1 % 2:
			e2 = next(i2)
		print(e1, e2)

def example_21():
	"""
	Итераторы 2
	"""
	print('\n*** Example 21 ***')
	a = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
	i1 = iter(a)
	i2 = iter(a)
	for e1 in i1:
		if e1 % 2:
			e2 = next(i2)
		print(e1, e2)

def example_22():
	"""
	Итераторы 3
	"""
	print('\n*** Example 22 ***')
	a = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
	i2 = iter(a)
	for e1 in a:
		if e1 % 2:
			e2 = next(i2)
		print(e1, e2)

# Comment-out tests you like to skip with '#' character

example_01()
example_02()
example_03()
example_04()
example_05()
example_06()
example_07()
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
