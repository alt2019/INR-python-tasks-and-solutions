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

def create_text_sample_file():
	with open('sample.txt', 'w') as f:
		f.write(
"""This is sample text for file reading examples
Second line
Third line
Четвертая строка по-русски
Line 5 - the end
""")

def create_bin_sample_file():
	with open('sample.bin', 'wb') as f:
		f.write(
b"""This is sample text for file reading examples
Second line
Third line
\xd0\xa7\xd0\xb5\xd1\x82\xd0\xb2\xd0\xb5\xd1\x80\xd1\x82\xd0\xb0\
\xd1\x8f\x20\xd1\x81\xd1\x82\xd1\x80\xd0\xbe\xd0\xba\xd0\xb0\x20\
\xd0\xbf\xd0\xbe\x2d\xd1\x80\xd1\x83\xd1\x81\xd1\x81\xd0\xba\xd0\
\xb8
Line 5 - the end
""")

def example_01():
	"""
	Файл как коллекция
	"""
	pfi()
	create_text_sample_file()
	for line in open('sample.txt'):
		print(' for:', line, end='')

	f = open('sample.txt')
	i = iter(f)
	while True:
		line = next(i, None)
		if line == None:
			break
		print('iter:', line, end='')
	f.close()

	a = [ line for line in open('sample.txt') if line[0] != 'T' ]
	print('a =', a)

def example_02():
	"""
	Чтение фиксированного количества символов,
	метод read()
	"""
	pfi()
	create_text_sample_file()
	f = open('sample.txt')
	for i in range(10):
		print(i, ':', f.read(4))
	f.close()

def example_03():
	"""
	Менеджер контекста with автоматически
	закрывает файл
	"""
	pfi()
	create_text_sample_file()
	with open('sample.txt') as f:
		a = 14
		for line in f:
			print(line, end='')
	# f.read() # => ValueError: I/O operation on closed file.
	print('a =',  a) # with не создает область видимости

def example_04():
	"""
	Чтение бинарного файла дает объекты типа bytes
	"""
	pfi()
	create_bin_sample_file()
	with open('sample.bin', "rb") as f:
		a = 14
		for line in f:
			print(line)
	# f.read() # => ValueError: I/O operation on closed file.
	print('a =',  a) # with не создает область видимости

def example_05():
	"""
	Перечисление файлов в директории
	"""
	pfi()
	import os
	directory = sys.argv[2] if len(sys.argv) > 2 else '.'
	for filename in os.listdir(directory):
		print(filename)

def example_06(called_from_other_example=False):
	"""
	Средства функционального программирования
	"""
	if not called_from_other_example:
		pfi()
	import math
	voltage_list = [180, 200, 220, 240]
	current_list = [0.12, 0.14, 0.15, 0.18]
	phi_list = [0.02, 0.03, 0.03, 0.05]
	def power(voltage, current, phi=0):
		return voltage * current * math.cos(phi)

	if called_from_other_example:
		return map(power, voltage_list, current_list, phi_list)

	print('=== map on three lists === ')
	for w in map(power, voltage_list, current_list, phi_list):
		print(w)
	print('\n=== map on two lists === ')
	for w in map(power, voltage_list, current_list):
		print(w)
	
	print(map(power, voltage_list, current_list)) # => map object
	
	print('\n=== filter accepts only one sequence === ')
	print(filter(lambda u: u < 220, voltage_list)) # => filter object
	print(u for u in filter(lambda u: u < 220, voltage_list)) # => generator object
	for e in filter(lambda u: u < 220, voltage_list):
		print('e =', e)

	# Три способа преобразовать фильтр или генератор в реальную последовательность
	print([u for u in filter(lambda u: u < 220, voltage_list)])
	print(list(u for u in filter(lambda u: u < 220, voltage_list)))
	print(list(filter(lambda u: u < 220, voltage_list)))
	# Также работает для map
	print(list(map(power, voltage_list, current_list)))
	# Применение map к неупорядоченным коллекциям возможен, результат неопределен
	e = {1, 2, 3}
	f = {10, 20, 30}
	print('Map on sets', set(map(lambda i, j: i + j, e, f)))

def example_07():
	"""
	Модуль shelve
	"""
	pfi()
	voltage_list = [180, 200, 220, 240]
	current_list = [0.12, 0.14, 0.15, 0.18]
	phi_list = [0.02, 0.03, 0.03, 0.05]
	a = example_06(called_from_other_example=True)
	test_config = {
		'voltage_list': voltage_list,
		'current_list': current_list,
		'phi_list': phi_list,
		'result': list(a)
		}
	import shelve
	import sys
	if sys.platform == 'linux':
		with shelve.open('example_07') as d:
			d['test_config'] = test_config

		with shelve.open('example_07', 'r') as loaded_d:
			print(loaded_d['test_config'])
			print('Third voltage is', loaded_d['test_config']['voltage_list'][2])
	else:
		d = shelve.open('example_07')
		d['test_config'] = test_config
		d.close()

		loaded_d = shelve.open('example_07', 'r')
		print(loaded_d['test_config'])
		print('Third voltage is', loaded_d['test_config']['voltage_list'][2])
		loaded_d.close()

def example_08():
	"""
	Строка документации хранится в атрибуте __doc__
	Функции dir и help
	"""
	pfi()
	import math
	def power(voltage, current, phi=0):
		""" Функция power вычисляет электрическую мощность
по значениям напряжения (параметр voltage),
тока (параметр current) и фазового угла (параметр phi)
Фазовый угол по умолчанию принимает нулевое значение.
"""
		return voltage * current * math.cos(phi)  

	print(dir(power))
	# help(power) # Работает, но вызывает pager, нажмите Esc для выхода из pager
	print('\n__doc__ =', power.__doc__)

def example_09():
	"""
	Функция reduce
	"""
	pfi()
	a = example_06(called_from_other_example=True)
	print('Iterator for processing', a)
	# Величина счетчика это размер массива: len(counter)
	counter = [1] # При первом вызове reduce использует два элемента коллекции
	from functools import reduce
	print('Average with reduce', reduce(lambda i, j: counter.append(1) or i + j, a) / len(counter))
	print('Total values processed:', len(counter))

	# Итератор a уже использован, необходимо получить новый
	a = example_06(called_from_other_example=True)
	w_sum = 0
	counter = 0
	for w in a:
		w_sum += w
		counter += 1
	print('Average with a loop', w_sum / counter)
	print('Total values processed:', counter)
	++counter # Ошибки нет, но это не инкремент а два раза унарный плюс
	print('++counter =', ++counter)

	a = example_06(called_from_other_example=True)
	# Задан третий аргумент для инициализации аккумулятора
	counter = [] # Счетчик начинается с нуля !
	print('Average with reduce', reduce(lambda i, j: counter.append(1) or i + j, a, 0) / len(counter))
	print('Total values processed:', len(counter))

def example_10():
	"""
	Функция reduce с необычным аккумулятором
	"""
	pfi()
	# Аккумулятор может быть любого типа, не обязательно
	# связанного с типом элементов коллекции
	c = { 1, 'a', 2, (3, 4), 5, '6', 7, '8', (9, 10, 11), 12 } # Коллекция
	a = { 'numbers': 0, 'strings': 0, 'tuples': 0 } # Аккумулятор
	def get_info(i, j):
		if isinstance(j, int):
			i['numbers'] += 1
		elif isinstance(j, str):
			i['strings'] += 1
		elif isinstance(j, tuple):
			i['tuples'] += 1
		return i
	from functools import reduce
	print('Info on s:', reduce(get_info, c, a))

def example_11():
	"""
	Оператор yield
	"""
	pfi()
	def seq(n=3):
		if n == 99:
			return
		yield '\nfirst'
		for i in range(1, n + 1):
			yield '*' * i

	print('seq() is', seq)
	for x in seq():
		print(x, end=', ') # => first, *, **, ***, 
	for x in seq(5):
		print(x, end=', ') # => first, *, **, ***, ****,  *****, 
	for x in seq(99):
		print(x, end=', ') # => Ни одной итерации не будет
	print()

def example_12():
	"""
	yield это оператор, он возвращает значение и может
	быть использован в выражении. Тема coroutines здесь
	не рассматривается.
	"""
	pfi()
	def seq(n=3):
		if n == 99:
			return
		yield '\nfirst'
		for i in range(1, n + 1):
			z = (n or (yield '*' * i)) * 10
			print('Yield in expression', z)
			print('Yield as parameter', (yield '*' * i))

	print('seq() is', seq)
	for x in seq():
		print(x, end=', ') # => first, *, **, ***, 
	for x in seq(5):
		print(x, end=', ') # => first, *, **, ***, ****,  *****, 
	for x in seq(99):
		print(x, end=', ') # => Ни одной итерации не будет
	print()


if len(sys.argv) > 1 and sys.argv[1].isdigit() and int(sys.argv[1]) > 0:
	exec('example_%02d()' % int(sys.argv[1]))
else:
	tuple(map(lambda c: exec(c + '()'),
		(f for f in sys._getframe().f_code.co_names
			if f.startswith('example_'))))
