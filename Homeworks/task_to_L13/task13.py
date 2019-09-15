#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Изучите примеры к лекции, запустите программу с примерами
Напишите программу построения графиков по результатам работы программы,\
 написанной как домашнее задание к лекции 10
Программа должна выполнять следующие действия:
- Исполнить программу домашнего задания к лекции 10 путем вызова\
 функции os.popen()
- Произвести разбор вывода программы домашнего задания к лекции 10\
 и сформировать соответствующие последовательности чисел
Используя полученные последовательности чисел построить графики в виде\
 ломаных линий, где:
- время отложено по оси X,
- температура, ток и напряжения датчиков отложены по оси Y
Включить в график легенду, указывающую соответствие цвета линий\
 и отображаемых величин
"""

import time
import os
import matplotlib.pyplot as plt


def interception_of_process() -> bytes:
	"""
	This function intersects the output of task09.py
	returns: bytes
	"""
	b = os.popen('python3 task09.py')
	output = bytes(b.read(), 'utf-8')
	# print(b)
	# from subprocess import Popen, PIPE, STDOUT
	# cmd = 'python3 task09.py'
	# p = Popen(cmd, shell=True, 
		# stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
	# output = p.stdout.read()
	return output


def create_sequences(output: bytes) -> (list, list, list, list, list):
	"""
	This function obtains from bytes-like output 5 lists of values\
	 with the help of regular expressions
	arg output: bytes - bytes-like output of stdout
	returns: (list,list,list,list,list)
	"""
	import re
	out_of_prog = output.split(b'\n')

	time_lst = []
	temp_lst = []
	curr_lst = []
	pr1_lst = []
	pr2_lst = []

	pattern = r'b\'(?P<time>\w+\s\=(\s|\s{2}|\s{3})(\d|\d{2}|\d{3}))\,\ ' +\
	 r'(?P<temp>\w+\s\=\ (\d{2}))\,\ ' +\
	  r'(?P<cur>\w+\s\=\ (\d{2}))\,\ ' +\
	   r'(?P<pr1>\w+\s\=\ (\d{2}))\,\ ' +\
	    r'(?P<pr2>\w+\s\=\ (\d{2}))(\'|\w+)'

	for item in out_of_prog:
		res = re.match(pattern, string = str(item))
		if res:
			if not __debug__: print(str(item))
			time_lst.append(int(res.group(3)))
			temp_lst.append(int(res.group(5)))
			curr_lst.append(int(res.group(7)))
			pr1_lst.append(int(res.group(9)))
			pr2_lst.append(int(res.group(11)))

	return time_lst, temp_lst, curr_lst, pr1_lst, pr2_lst

def draw_data_all_one_picture(**nargs: dict) -> None:
	"""
	This function creates files with graphics of values through time \
	via matplotlib: table of plots
	args input: dict - named argumets to draw
	"""
	tabled_horizontal = 2
	tabled_vertical = int((len(nargs.keys())-1)/2)
	fig, axes = plt.subplots(tabled_vertical, tabled_horizontal)
	plt.subplots_adjust(wspace=0.4, hspace=0.4) 
	fig.suptitle('All data')
	x, y = 0, 0
	for key in nargs.keys():
		if key != 'time':
			axes[x, y].set_title(key)
			axes[x, y].plot(nargs['time'], nargs[key], label=key) 
			axes[x, y].legend(loc='upper left')
			x += 1
			if x >= tabled_vertical: 
				x = 0
				y += 1
	plt.savefig('All_in_one_picture' + time.strftime("%Y_%m_%d_%H.%M.%S") + '.png')
	if not __debug__: plt.show()
	plt.close()


def draw_data_all_one_plot(**nargs: dict) -> None:
	"""
	This function creates files with graphics of values through time \
	via matplotlib: 1 common graph
	args input: dict - named argumets to draw
	"""
	fig = plt.figure()
	plt.grid(True)
	i = 72
	for key in nargs.keys():
		if key != 'time':
			plt.plot(nargs['time'], nargs[key], color='#' + hex(i*14641)[2:], label = key)
			i += 300
	plt.title('All data')
	plt.xlabel('time')
	plt.ylabel('All')
	plt.legend(loc='upper left')
	plt.savefig('All_in_one_plot' + time.strftime("%Y_%m_%d_%H.%M.%S") + '.png')
	if not __debug__: plt.show()
	plt.close()


def draw_data_separated(**nargs: dict) -> None:
	"""
	This function creates files with graphics of values through time \
	via matplotlib: separated graphs
	args input: dict - named argumets to draw
	"""
	plt.grid(True)
	i = 72
	for key in nargs.keys():
		if key != 'time':
			plt.title(key)
			plt.xlabel('time')
			plt.ylabel(key)
			plt.plot(nargs['time'], nargs[key], color='#' + hex(i*14641)[2:], label = key)
			plt.legend(loc='upper left')
			plt.savefig('{}_'.format(key) + time.strftime("%Y_%m_%d_%H.%M.%S") + '.png')
			if not __debug__: plt.show()
			plt.close()
			i += 300


def main() -> None:
	"""
	This function completes the task
	"""
	output = interception_of_process()
	time_lst, temp_lst, curr_lst, pr1_lst, pr2_lst = create_sequences(output)
	draw_data_all_one_picture(time = time_lst, 
		temp = temp_lst, curr = curr_lst, pr1 = pr1_lst, pr2 = pr2_lst)
	draw_data_all_one_plot(time = time_lst, 
		temp = temp_lst, curr = curr_lst, pr1 = pr1_lst, pr2 = pr2_lst)
	draw_data_separated(time = time_lst, 
		temp = temp_lst, curr = curr_lst, pr1 = pr1_lst, pr2 = pr2_lst)


if __name__ == '__main__':
	main()




