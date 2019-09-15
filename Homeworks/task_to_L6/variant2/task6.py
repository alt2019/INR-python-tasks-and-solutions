#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
 Изучите примеры к лекции, запустите программу с примерами.
 Преобразуйте программу, написанную как домашнее задание к лекции 4, в модуль.
 При запуске в качестве самостоятельной программы модуль должен выполнять\
  те же действия, что и ранее, возможно с исправлениями.
 При импорте модуль должен предоставлять функцию run с тремя аргументами:
- run(control, probe_1, probe_2)
- При необходимости могут быть введены дополнительные аргументы, имеющие\
 значения по умолчанию
- При исполнении функции run из импортированного модуля функция должна\
 вывести на экран отчет точно соблюдая\
формат строк, описанный в домашнем задании к лекции 4:
- Все числовые поля отформатированы в два символа\
 с выравниванием по правому краю
- Все пробельные разделители содержат один пробел
- Присутствуют запятые после чисел, но не в конце строки, так как это\
 показано в примере в тексте домашнего задания к лекции 4
- Отсутствуют пробелы в начале и конце строк
- Отсутствуют пустые строки и отладочная печать
 Напишите программу которая обработает данные, находящиеся\
  в файлах выполняя следующие действия:
- Перебрать все файлы в директории с именами data*.txt в алфавитном порядке
 Для каждого файла:
- Вывести на экран заголовок в виде: символ '#', пробел, имя файла, пример:
-- # data001.txt
- Извлечь из файла данные для списков control, probe_1, probe_2
- Вывести на экран отчет вызовом функции run из модуля описанного выше
 Файлы данных для обработки находятся в zip архиве
'''

# import os
from os import listdir as ld
from task6main import run
import zipfile


# def sys_work1():
	# stories_zip = zipfile.ZipFile('data06dz.zip')
	# for file in stories_zip.namelist():
		# stories_zip.extract(file)
	# stories_zip.close()
# 

def sys_work():
	files_to_analise = [ item for item in ld() 
		if 'data' in item and '.txt' in item ]
	return files_to_analise


def file_work():
	control_list = []
	probe_1_list = []
	probe_2_list = []
	stories_zip = zipfile.ZipFile('data06dz.zip')
	# sss = sys_work().sort()
	for file in sys_work():
	# for file in sss:
	# for file in stories_zip.namelist():
		# print("# {}".format(file))
		# print("# %s" % file, "")
		print(file)

		with open(file) as f:
			line_list = [ line.split(',') for line in f ]
			line_list1 = [ item[i] for item in line_list 
				for i in range(len(item)) if item[i] != '\n' ]
			i = 0
			for i in range(len(line_list1)):
				if '# control' in line_list1[i]: i1 = i
				if '# probe_1' in line_list1[i]: i2 = i
				if '# probe_2' in line_list1[i]: i3 = i
			c_control_list = [ int(item) for item in line_list1[i1+1:i2] ]
			control_list.append(c_control_list)
			c_probe_1_list = [ int(item) for item in line_list1[i2+1:i3] ]
			probe_1_list.append(c_probe_1_list)
			c_probe_2_list = [ int(item) for item in line_list1[i3+1:] ]
			probe_2_list.append(c_probe_2_list)
			# print(c_control_list)
			# print(c_probe_1_list)
			# print(c_probe_2_list)
	
			condition = {"temperature": "<30"}
			run(c_control_list, c_probe_1_list, c_probe_2_list, 
				condition = None)


if __name__ == '__main__':
	print(__doc__)
	file_work()