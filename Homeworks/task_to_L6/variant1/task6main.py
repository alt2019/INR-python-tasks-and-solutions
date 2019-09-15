#!/usr/bin/env python3
# -*- coding: utf-8 -*-


'''
Экспериментальная установка состоит из трех компонент:
Управляющая система, ее параметры:
ток управления, мА
температура установки, градусы Цельсия
Датчик 1, его параметры:
напряжение на выходе, мкВ
Датчик 2
напряжение на выходе, мкВ
Экспериментальная установка работает 20 секунд, каждую секунду происходит \
считывание данных с указанием момента времени от 1 до 20. Для некоторых \
моментов времени данные датчика могут отсутствовать.

Данные управляющей системы оформлены как список, в котором последовательно \
идут группы по 3 значения: температура, ток, время.

Данные датчиков оформлены как список, в котором последовательно идут \
группы по 2 значения: напряжение, время.

Напишите программу, которая выведет на экран отчет о работе установки \
в виде строк вида:
Time = 11, Temperature = 12, Current = 13, Probe_1 = 14, Probe_2 = 15

В отчет должны войти строки только тех измерений, для которых есть данные \
обоих датчиков, ток управления превышает 30 мА, а температура \
установки была ниже 40 градусов.

Столбцы отчета должны быть выравнены
Столбцы отчета должны быть отсортированы по времени
'''


control = [
	22, 34,  1,
	32, 37,  2,
	31, 27,  3,
	12, 46,  4,
	22, 38,  5,
	44, 26,  6,
	11, 35,  7,
	41, 52,  8,
	36, 50,  9,
	27, 58, 10,
	40, 54, 20,
	30, 33, 19,
	28, 21, 18,
	30, 30, 17,
	28, 27, 16,
	33, 36, 15,
	21, 26, 14,
	20, 53, 13,
	27, 40, 12,
	18, 35, 11
	]

probe_1 = [
	78,  1,
	95,  2,
	20,  3,
	43,  4,
	71,  6,
	21,  7,
	52,  8,
	44,  9,
	34, 12,
	97, 13,
	93, 14,
	53, 15,
	42, 17,
	79, 18,
	37, 20,
	]

probe_2 = [
	38,  1,
	48,  3,
	50,  4,
	86,  5,
	72,  6,
	62,  8,
	70,  9,
	24, 10,
	71, 12,
	54, 13,
	75, 16,
	72, 18,
	68, 19,
	73, 20,
	]


def cond(i, listt, condition): 
	"""
	Checks condition and transforms it to if-else constructions
	type(condition) # dict
	"""
	cur_cd = condition.get("current")
	temp_cd = condition.get("temperature")
	if cur_cd and temp_cd:
		if cur_cd[0] == '>' and temp_cd[0] == '>':
			return ((listt[i+2] > int(cur_cd[1:])) and (listt[i+1] > int(temp_cd[1:])))
		elif cur_cd[0] == '<' and temp_cd[0] == '>':
			return ((listt[i+2] < int(cur_cd[1:])) and (listt[i+1] > int(temp_cd[1:])))
		elif cur_cd[0] == '<' and temp_cd[0] == '<':
			return ((listt[i+2] < int(cur_cd[1:])) and (listt[i+1] < int(temp_cd[1:])))
		elif cur_cd[0] == '>' and temp_cd[0] == '<':
			return ((listt[i+2] > int(cur_cd[1:])) and (listt[i+1] < int(temp_cd[1:])))
	elif cur_cd: 
		if cur_cd[0] == '>':
			return ((listt[i+2] > int(cur_cd[1:])))
		elif cur_cd[0] == '<':
			return ((listt[i+2] < int(cur_cd[1:])))
		elif cur_cd[0] == '<':
			return ((listt[i+2] < int(cur_cd[1:])))
		elif cur_cd[0] == '>':
			return ((listt[i+2] > int(cur_cd[1:])))
	elif temp_cd: 
		if temp_cd[0] == '>':
			return ((listt[i+1] > int(temp_cd[1:])))
		elif temp_cd[0] == '>':
			return ((listt[i+1] > int(temp_cd[1:])))
		elif temp_cd[0] == '<':
			return ((listt[i+1] < int(temp_cd[1:])))
		elif temp_cd[0] == '<':
			return ((listt[i+1] < int(temp_cd[1:])))


def generate_report(lst, cnd, var=1):
	"""
	Auxillary function, applied to generating report in the first method 
	"""
	if cnd is not None:
		list1t = [ [ lst[i], lst[i+1], lst[i+2], lst[i+3], lst[i+4] ] 
			for i in range(0, len(lst), 5) if cond(i, lst, cnd) ]
	elif cnd is None:
		list1t = [ [ lst[i], lst[i+1], lst[i+2], lst[i+3], lst[i+4] ] 
			for i in range(0, len(lst), 5) if ((lst[i+2] > 30) and (lst[i+1] < 40)) ]
	return list1t


def make_result(time, ic, tc, up1, tp1, up2, tp2, var, condition = None, c = control, p1 = probe_1, p2 = probe_2):
	"""
	Generation of unsorted report due two methods:
	- with nested loops
	- with generator
	In the first method function that check condition is defined
	"""
	if var == 1:
		list1 = []
		for item in time:
			if (item in tc) and (item in tp1) and (item in tp2):
				for i in range(0, len(c)):
					for j in range(0, len(p1)):
						for k in range(0, len(p2)):
							if ((i % 3 == 2) and (c[i] == item) 
								and (j % 2 == 1) and (p1[j] == item) 
								and (k % 2 == 1) and (p2[k] == item)):
								list1.extend([c[i], c[i-2], c[i-1], p1[j-1], p2[k-1]])
		return generate_report(list1, condition, 1)
	elif var == 2:
		list2 = [ [ c[i], c[i-2], c[i-1], p1[j-1], p2[k-1] ] 
			for item in time 
			if ((item in tc) and (item in tp1) and (item in tp2)) 
			for k in range(0, len(p2)) for j in range(0, len(p1)) for i in range(0, len(c)) 
			if ((i % 3 == 2) and (c[i] == item) 
				and (j % 2 == 1) and (p1[j] == item) 
				and (k % 2 == 1) and (p2[k] == item)) ]
		list2t = [ [ list2[i][0], list2[i][1], list2[i][2], list2[i][3], list2[i][4] ] 
			for i in range(0, len(list2)) if ((list2[i][2] > 30) and (list2[i][1] < 40)) ]
		return list2t


def sort_list(listt):
	for j in range(0, len(listt)-1):
		for i in range(0, len(listt)-1):
			if (listt[i][0] > listt[i+1][0]):
				listt[i], listt[i+1] = listt[i+1], listt[i]


def print_report(listt, var = None):
	sort_list(listt)
	if var is None:
		print('\n*** Report: ***')
	elif var == 1:
		print('\n*** Report variant 1: nested loops ***')
	elif var == 2:
		print('\n*** Report variant 2: complex generator ***')
	for i in range(0, len(listt)):
		print("Time = %2d" % listt[i][0], 
			"Temperature = %2d" % listt[i][1], 
			"Current = %2d" % listt[i][2], 
			"Probe_1 = %2d" % listt[i][3], 
			"Probe_2 = %2d" % listt[i][4]) 


def run(control, probe_1, probe_2, condition = None):
	# print(__doc__)
	c, p1, p2 = control, probe_1, probe_2

	tempc, ic, tc = c[0::3], c[1::3], c[2::3]
	up1, tp1 = p1[0::2], p1[1::2]
	up2, tp2 = p2[0::2], p2[1::2]

	""" condition of the task to change in numbers and comparison symbols """
	""" '=' is not allowed """
	if condition is None:
		cond = {"current": ">30", "temperature": "<40"}
	else:
		cond = condition

	time = [ item for item in tc if ((item in tp1) and (item in tp2)) ]
	list1t = make_result(time, ic, tc, up1, tp1, up2, tp2, 1, cond)
	list2t = make_result(time, ic, tc, up1, tp1, up2, tp2, 2)

	print_report(list1t, 1)
	print_report(list2t, 2)

if __name__ == '__main__':
	print(__doc__)
	# condition = {"temperature": "<30"}
	run(control, probe_1, probe_2)
