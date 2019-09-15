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


def cond(d_control, key, condition): 
	cur_cd = condition.get("current")
	temp_cd = condition.get("temperature")
	if cur_cd and temp_cd:
		if cur_cd[0] == '>' and temp_cd[0] == '>':
			return ((d_control[key][1] > int(cur_cd[1:])) and (d_control[key][0] > int(temp_cd[1:])))
		elif cur_cd[0] == '<' and temp_cd[0] == '>':
			return ((d_control[key][1] < int(cur_cd[1:])) and (d_control[key][0] > int(temp_cd[1:])))
		elif cur_cd[0] == '<' and temp_cd[0] == '<':
			return ((d_control[key][1] < int(cur_cd[1:])) and (d_control[key][0] < int(temp_cd[1:])))
		elif cur_cd[0] == '>' and temp_cd[0] == '<':
			return ((d_control[key][1] > int(cur_cd[1:])) and (d_control[key][0] < int(temp_cd[1:])))
	elif cur_cd: 
		if cur_cd[0] == '>':
			return ((d_control[key][1] > int(cur_cd[1:])))
		elif cur_cd[0] == '<':
			return ((d_control[key][1] < int(cur_cd[1:])))
		elif cur_cd[0] == '<':
			return ((d_control[key][1] < int(cur_cd[1:])))
		elif cur_cd[0] == '>':
			return ((d_control[key][1] > int(cur_cd[1:])))
	elif temp_cd: 
		if temp_cd[0] == '>':
			return ((d_control[key][0] > int(temp_cd[1:])))
		elif temp_cd[0] == '>':
			return ((d_control[key][0] > int(temp_cd[1:])))
		elif temp_cd[0] == '<':
			return ((d_control[key][0] < int(temp_cd[1:])))
		elif temp_cd[0] == '<':
			return ((d_control[key][0] < int(temp_cd[1:])))


def make_result(control, probe_1, probe_2, condition = None):
	d_control, d_probe_1, d_probe_2 = make_dict(control, probe_1, probe_2)
	d = dict((key, (d_control[key], d_probe_1[key], d_probe_2[key])) for key in d_control.keys() 
		if (key in d_probe_1.keys() and key in d_probe_2.keys())
		# if (d_control[key][0]<40 and d_control[key][1]>30)
		if cond(d_control, key, condition)
		)
	return d

		
def print_report(inputt):
	if isinstance(inputt, dict): 
		inputt = sorted(inputt.items())
		for i in range(0, len(inputt)):
			print("Time = %3d," % inputt[i][0], 
				"Temperature = %2d," % inputt[i][1][0][0], 
				"Current = %2d," % inputt[i][1][0][1], 
				"Probe_1 = %2d," % inputt[i][1][1], 
				"Probe_2 = %2d" % inputt[i][1][2])		


# 2nd algoritm
def make_dict(control, probe_1, probe_2):
	d_control = dict(zip(control[2::3], zip(control[0::3], control[1::3])))
	d_probe_1 = dict(zip(probe_1[1::2], probe_1[0::2]))
	d_probe_2 = dict(zip(probe_2[1::2], probe_2[0::2]))
	return d_control, d_probe_1, d_probe_2


def run(control, probe_1, probe_2, condition = None):
	# print(__doc__)
	""" condition of the task to change in numbers and comparison symbols
	 '=' is not allowed """
	if condition is None:
		cond = {"current": ">30", "temperature": "<40"}
	else:
		cond = condition

	d = make_result(control, probe_1, probe_2, condition = cond)
	# print(d1)
	print_report(d)
	return d # !added


def prob():
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
	return control, probe_1, probe_2


if __name__ == '__main__':
	print(__doc__)
	control, probe_1, probe_2 = prob()
	# condition = {"temperature": "<30"}
	# run(control, probe_1, probe_2)
	import cProfile
	# cProfile.run('run(control, probe_1, probe_2)')
	cProfile.run('run(control, probe_1, probe_2)')
	# make_dict(control, probe_1, probe_2)
	# print("var1___________________________________________________________")
	# cProfile.run('print(make_result(control, probe_1, probe_2, var = 3.1))')
	# print("var2___________________________________________________________")
	# cProfile.run('print(make_result(control, probe_1, probe_2, var = 3.2))')