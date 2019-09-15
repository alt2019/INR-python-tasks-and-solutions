#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
:module:
========
Prints a report of incidents, happened through connection to service, by\
 ip and username. 

:arguments: module get optional argument - minimal number of incidents per\
 one user. If not, all icdinets will be printed.

:task:
======
Изучите примеры к лекции, запустите программу с примерами
Напишите программу, анализа инцидентов несанкционированного доступа,\
 отраженных в log файле, находящемся в zip архиве data11dz.zip
Для анализа строк log файла и извлечения данных используйте регулярные выражения
Каждый инцидент соответствует одной строке log файла. В строке инцидента\
 в обязательном порядке присутствует ключевое слово from за которым следует\
  IP адрес  атакующего компьютера. В строке инцидента также присутствует\
   имя пользователя, используемое для атаки
Напечатайте отчет инцидентов по IP адресам в виде:
- Заголовок отчета: # Report by IP
- Строки отчета в виде: <IP адрес> <пробел> <количество инцидентов>
- IP адрес должен быть помещен в поле шириной 15 символов\
 и быть выравнен по левому краю
- Количество инцидентов должно быть помещено в поле шириной 6 символов\
 и быть выравнено по правому краю
- Строки отчета должны быть отсортированы\
 по количеству инцидентов в порядке убывания
Напечатайте отчет инцидентов по именам пользователя в виде:
- Заголовок отчета: # Report by user
- Строки отчета в виде: <имя пользователя> <пробел> <количество инцидентов>
- Имя пользователя должно быть помещено в поле шириной 15 символов\
 и быть выравнено по левому краю
- Количество инцидентов должно быть помещено в поле шириной 6 символов\
 и быть выравнено по правому краю
- Строки отчета должны быть отсортированы по количеству инцидентов\
 в порядке убывания
Программа должна воспринимать один параметр - число инцидентов.\
 В отчеты включаются только те строки, для которых число инцидентов\
  больше или равно числу,  заданному параметром. Если программа\
   была запущена без параметров, в отчет включаются все строки.

"""


import zipfile
import re
import os
import sys

from collections import Counter, OrderedDict


def generate_report(file):
	""" 
	This function generates lists of incidents by ip and by user
	:args file: - <file> - name of file, where the computation is done
	:returns: <list> of ip incidents, list of user incidents
	:debugging: counters of incidents to compare with
	"""
	pattern = 'from'
	list_of_ip = []
	list_of_users = []
	# debugging
	counter_of_incidents = 0
	counter_of_ip_inc = 0
	real_incidents = 0
	count_root_inc = 0
	count_user_inc1 = 0
	count_user_inc2 = 0
	
	for line in file:
		text = str(line)
		if re.search(pattern, text, flags=0):	
			counter_of_incidents += 1
			root_incidents = re.search("root" , text, flags=0)
			user1 = re.search("user\s[a-zA-Z0-9]+" , text, flags=0)
			user2 = re.search("for\s[a-zA-Z0-9]+" , text, flags=0)

			if root_incidents:
				count_root_inc += 1
				list_of_users.append(root_incidents.group())
			if user1 and not root_incidents:
				count_user_inc1 += 1
				list_of_users.append(user1.group()[5:])
			if user2 and not root_incidents and not user1:
				count_user_inc2 += 1
				list_of_users.append(user2.group()[4:])
			if root_incidents or user1 or user2: 
				real_incidents += 1
				ip = re.search('(([2][5][0-5]\.)|([2][0-4][0-9]\.)|([0-1]?[0-9]?[0-9]\.)){3}(([2][5][0-5])|([2][0-4][0-9])|([0-1]?[0-9]?[0-9]))', text, flags=0)
				if ip: 
					counter_of_ip_inc += 1
					list_of_ip.append(ip.group())

	if not __debug__:
		print("counter of all incidents", counter_of_incidents)
		print("counter of ip incidents", counter_of_ip_inc)
		print("real incidents", real_incidents)
		print("count_root_inc", count_root_inc)
		print("count_user_inc1", count_user_inc1)
		print("count_user_inc1", count_user_inc2)
		print("sum of inc", count_root_inc + count_user_inc1 + count_user_inc2)
	return list_of_ip, list_of_users


def count_elems(list_):
	""" 
	This function makes frequency analylis of list elements
	:params list_: <list>
	:returns: <dict> frequency dictionary of list
	"""
	# from collections import Counter
	d_count = dict(Counter(list_))
	if not __debug__: print("dictionary of counted events", d_count)
	return d_count


def dict_sorted_by_values(dict_, order):
	""" \
	This function sorts dictionary by values
	:param dict_: <dict> - dictionary to sort
	:param order: <str> - if "reversed", sort in descending order,\
	 else - in ascending order
	:returns: sorted <dict> by values
	"""
	reverse = True if order == 'reversed' else False
	# from collections import OrderedDict
	d_sorted = OrderedDict(sorted(
		dict_.items(), 
		key=lambda t: t[1], 
		reverse=reverse))
	return d_sorted


def print_report(dict_, ip__user, order, n_incidents):
	""" 
	This function prints a report
	:param dict_: <dict> - dictionary to print report
	:param order: <str> - optional, if "reversed", sort in descending order,\
	 else - in ascending order
	:param ip__user: <str> - if "user", sort by user,if "ip" - sort by ip
	:param n_incidents: <int> - minimal number of incidents
	:returns: None
	"""
	n_incidents = 0 if n_incidents == None else int(n_incidents)
	if ip__user == 'ip': print('# Report by IP')	
	elif ip__user == 'user': print('# Report by user')	
	d_sorted = dict_sorted_by_values(dict_, order)
	for key, value in zip(d_sorted.keys(), d_sorted.values()):
		if value >= n_incidents:
			print("{ip:<15} {N_incidents:>6}".format(ip=key, N_incidents=value))


def main():
	""" 
	Main function, obtains # of incidents, opens zip, and processes\
	 file "log*.txt"; finally, prints a report
	"""
	n_incidents = sys.argv[1] if len(sys.argv) > 1 else None
	dirname = sys.argv[2] if len(sys.argv) > 2 else None
	for filename in sorted(os.listdir(dirname or '.')):
		if filename.startswith('data') and filename.endswith('.zip'):
			with zipfile.ZipFile(filename, 'r') as z1:
				if not __debug__:
					z1.printdir()
					print(z1.namelist())
				for log_file in z1.namelist():
					if log_file.startswith('log') and log_file.endswith('.txt'):
						with open(log_file) as f:
							list_of_ip, list_of_users = generate_report(f)

	if not __debug__: print(list_of_ip, list_of_users)

	ip_counted = count_elems(list_of_ip)
	user_counted = count_elems(list_of_users)

	if not __debug__: 
		print(ip_counted, user_counted)

		sorted_ip_counted = dict_sorted_by_values(
			ip_counted, order = 'reversed')
		sorted_user_counted = dict_sorted_by_values(
			user_counted, order = 'reversed')

		print(sorted_ip_counted, sorted_user_counted)
		print("# of elements:", sum(sorted_ip_counted.values()))
		print("# of elements:", sum(sorted_user_counted.values()))

	print_report(ip_counted, 'ip', 'reversed', n_incidents)
	print_report(user_counted, 'user', 'reversed', n_incidents)


if __name__ == '__main__':
	import cProfile
	cProfile.run('main()')
	pass