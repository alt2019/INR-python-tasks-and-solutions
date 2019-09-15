#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def example_01():
	print('\n*** Example 01 ***')
	# Функция range СОЗДАЕТ список в Питоне 2
	# Функция range ИМИТИРУЕТ список в Питоне 3
	print('A:', range(0, 100))
	print('B:', list(range(0, 100)))

def example_02():
	print('\n*** Example 02 ***')
	# Использование тройных кавычек для превращения
	# части текста программы в комментарий
	a = 1
	a = a * 2 # здесь a увеличивается вдвое
	a = a * 2 # здесь a увеличивается вдвое еще раз
	a = a * 2 # и еще раз
	"""
	a = a * 2 # и еще раз
	a = a * 2 # и еще раз
	"""
	print('a = ', a) # => a = 8

def example_03():
	print('\n*** Example 03 ***')
	# Синтаксически корректная программа
	a = 3 + 2  # инструкция присваивания
	3 + 2      # одиночное выражение записанное в строке
	3          # элементарное выражение
	"A string" # элементарное выражение
	a          # элементарное выражение
	a == 12    # одиночное выражение записанное в строке, если программист
	           # хотел написать a = 12, ошибка не будет замечена !

def example_04():
	print('\n*** Example 04 ***')
	# Особенности синтаксиса и терминологии
	def eat_apples(n):
		print('We ate %d apples' % n)
	def get_more_fruits():
		print('We got more fruits')
	apples = 5
	pears = 3

	if apples > pears:
		eat_apples(apples - pears)
		print('We ate extra apples')
	get_more_fruits()

def example_05():
	print('\n*** Example 05 ***')
	# Переменные и операция присваивания
	a = 4 + 6 * 2
	print('a =', a)
	b = 'Long' + 'Name'
	print('b =', a)

def example_06():
	# Строки и функция print
	print('\n*** Example 06 ***')
	s = '%2d часов\t%02d минут' % (16, 30)
	print(s)
	s2 = '{} часов\t{} минут'.format(16, 30)
	print(s2)
	s2 = str(16) + ' часов\t' + str(30) + ' минут'
	print(s2)
	print(1, 2, 3) # => 1 2 3
	print(1, 2, 3, sep='->') # => 1->2->3

def example_07():
	print('\n*** Example 07 ***')
	# Определение функции
	def add(a, b):
		n = a + b
		return n

	result = add(2, 4)
	print('sum =', result) # => 6

def example_08():
	print('\n*** Example 08 ***')
	# Пробелы и разделители
	a=2+3*4 # Без пробелов
	print('A: a =', a)
	a = 2 + 3 * 4 # То же, но с пробелами
	print('B: a =', a)
	a=a+1 if a==14 else a+4 # Правильно
	#a=a+1 ifa==14 else a+4 # Синтаксическая ошибка
	print('C: a =', a)

def example_09():
	print('\n*** Example 09 ***')
	# Переносы строк
	import math
	alpha = 0.735
	a = 0.5 - math.sin(alpha + math.pi/2)
	a = 0.5 - \
	math.sin(alpha + math.pi/2)
	a = 0.5 - math.sin(alpha +
math.pi/2)

	b = alpha ** 2 # Правильно
	# Перенос строки кода символом '\' интерпретируется как пробел
	"""
	b = alpha *\
* 2 # Синтаксическая ошибка, оператор ** разорван пробелом
	"""
	# Перенос символьного литерала символом '\' НЕ интерпретируется как пробел
	s = 'ab\
cd'
	print('s =', s) # => s = abcd

def example_10():
	print('\n*** Example 10 ***')
	# Несколько инструкций в строке

	import math
	alpha = 0.735
	a = math.sin(alpha + math.pi/2) ; a = 0.5 - a ; print(a)
	if a < 0: a = -a ; print(a) ; a = a + 1 ; print(a)

def example_11():
	print('\n*** Example 11 ***')
	# Инструкция import

	import math
	alpha = 0.735
	a = math.sin(alpha)
	print('1: a =', a)

	from math import sin, cos, tan
	a = sin(alpha)
	print('2: a =', a)

	from math import sin as sinus, cos as cosinus
	a = sinus(alpha)
	print('3: a =', a)

def example_12():
	print('\n*** Example 12 ***')
	# Определение функции и ее вызов
	def add(a, b):
		n = a + b
		return n

	result = add(1, 2) * add(3, 4)
	print('result =', result)

def example_13():
	print('\n*** Example 13 ***')
	# The Zen of Python
	import this

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
