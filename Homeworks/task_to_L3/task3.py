#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
python3 -c "print(`id -u` % 5 + 1)"
->1
"""


from collections import deque


def step1(listt):
	"""1) Преобразовать список а в множество sa. 
	Вывести множество sa на экран."""
	return set(listt.copy())


def step2(listt, number, dictt):
	"""2) Заменить в списке а элемент с индексом n словарем d, 
	вывести результат на экран"""
	listt1 = listt.copy()
	listt1[number:number+1] = [dictt]
	return listt1


def step3(listt, number, dictt):
	"""3) Заменить в списке а элемент с индексом n значениями, 
	извлеченными из словаря d так, чтобы каждое значение 
	из словаря стало отдельным элементом списка Вывести 
	результат на экран"""
	listt1 = listt.copy()
	listt1[number:number+1] = dictt.values()
	return listt1


def step4(set1, set2):
	"""4) Преобразовать список, полученный в предыдущей операции 
	в множество и выполнить над ним и множеством sa операции 
	пересечения и объединения Вывести результаты на экран"""
	print("пересечение:", set1&set2)
	print("объединение:", set1|set2)


def step5(input_list):
	"""5) Продемострировать использование списка (класс list) 
	в качестве очереди: создать пустой список, добавить в него 
	элементы из списка а, извлечь элементы из очереди в том же 
	порядке в котором они были добавлены. Вывести на экран 
	извлекаемые из очереди элементы"""

	def defaulfvar(lst):
		"""FIFO"""
		listt = deque([])
		listt.appendleft(lst)
		print(listt)
		e = listt.popleft()
		print(e, listt)

	def filo(lst):
		"""FILO/LIFO"""
		lst1 = []
		lst1.insert(-1, lst[0])
		lst1.insert(-2, lst[1])
		lst1.insert(-3, lst[2])
		lst1.insert(-4, lst[3])
		lst1.insert(-5, lst[4])
		print(lst1)
		print(lst1.pop(0))
		print(lst1.pop(0))
		print(lst1.pop(0))
		print(lst1.pop(0))
		print(lst1.pop(0))	

	def fifo(lst):
		"""FIFO"""
		lst1 = []
		lst1.append(lst[0])
		lst1.append(lst[1])
		lst1.append(lst[2])
		lst1.append(lst[3])
		lst1.append(lst[4])
		print(lst1)
		print(lst1.pop(0))
		print(lst1.pop(0))
		print(lst1.pop(0))
		print(lst1.pop(0))
		print(lst1.pop(0))

	print("variant0:", defaulfvar.__doc__)
	defaulfvar(input_list)
	print("variant1:", filo.__doc__)
	filo(input_list)
	print("variant2:", fifo.__doc__)
	fifo(input_list)


if __name__ == '__main__':
	a = [4, 9, 3, 28, 17] 
	n = 2 
	d = {'first': 2, 'second': 33}

	print(step1.__doc__)
	sa = step1(a)
	print(sa)

	print(step2.__doc__)
	print(step2(a, n, d))

	print(step3.__doc__)
	print(step3(a, n, d))

	print(step4.__doc__)
	step4(sa, set(step3(a, n, d)))

	print(step5.__doc__)
	step5(a)