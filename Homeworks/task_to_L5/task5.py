#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Напишите программу содержащую следующие четыре функции:
- Функция fmin: 
-- имеет один аргумент - словарь; 
-- возвращаемое значение - минимальное значение значений элементов\
 словаря - целое число.
- Функция fmax: 
-- имеет произвольное количество именованных аргументов,
-- возвращаемое значение - максимальное значение значений элементов словаря,\
 - целое число
- Функция fawg:
-- имеет один аргумент: словарь, 
-- возвращаемое значение: None;
-- функция вычисляет среднее арифметическое значений элементов словаря\
 и помещает результат в глобальную переменную arithmetic_mean
Общие требования к функциям fmin, fmax и fawg:
- при расчете функция не должна учитывать значения элементов, в ключах\
 которых присутствует строка broken
- если значения элемента является строкой, оно должно быть преобразовано\
 в целое число и быть использовано в расчете
Функция print_result выводит на экран значения переданные ей в качестве\
 параметров функция имеет три аргумента: pmin и pmax и mean:
- аргумент pmin имеет значение по умолчанию 0;
- аргумент pmax имеет значение по умолчанию 99;
- аргумент mean не имеет значения по умолчанию 
- возвращаемое значение None.
Исходные данные представляют собой словарь data:
- ключи элементов словаря - строки;
- значения элементов словаря - целые числа или строки,\
 являющиеся представлением целых чисел.
Далее программа должна произвести следующие действия:
- Вычислить минимальное значение элементов словаря data используя функцию fmin;
- Вычислить максимальное значение элементов словаря data используя функцию fmax;
- Вычислить среднее арифметическое значений элементов словаря data,\
 используя функцию fawg;
- Вызвать функцию print_result с единственным параметром arithmetic_mean;
- Вызвать функцию print_result тремя параметрами: arithmetic_mean,\
 значением возвращенным из функции fmin и значением,\
 возвращенным из функции fmax.
'''


def condition(dictionary, not_to_be):
	"""
	Check containing of the substring not_to_be in keys of dictionary
	Return: list of values corresponding to keys of dictionary.
	"""
	list_to_compute = [ int(list(dictionary.values())[item])
		for item in range(len(list(dictionary.keys()))) 
		if not_to_be not in list(dictionary.keys())[item] ]
	return list_to_compute


def fmin(dictionary):
	"""
	Return minimal from values in dictionary
	"""	
	list_to_compute = condition(dictionary, "broken")
	min_value = min(list_to_compute)
	return min_value


def fmax(dictionary, **kwargs):
	"""
	Return maximal from values in dictionary
	"""	
	list_to_compute = condition(dictionary, "broken")
	max_value = max(list_to_compute)
	return max_value


def fawg(dictionary):
	"""
	Return mean from values in dictionary
	"""	
	list_to_compute = condition(dictionary, "broken")
	summ = 0 
	for i in range(len(list_to_compute)):
		summ += list_to_compute[i]
	arithmetic_mean = summ/len(list_to_compute)
	return arithmetic_mean


def print_result(mean, pmin = 0, pmax = 99):
	print('**** %7s ****' % 'RESULT')
	print('Minimal value: %2d' % pmin)
	print('Maximal value: %2d' % pmax)
	if (pmin == 0 and pmax == 99):
		mean = (pmin + pmax)/2
	print('Mean value: %5d' % mean)


if __name__ == '__main__':
	data = {
	'ab': 18,
	'cd': '7',
	'ef-broken': 11,
	'ef': 38,
	'gh': '17',
	'broken_result': '52'
	}
	print(__doc__)
	print_result(fawg(data))
	print_result(fawg(data), fmin(data), fmax(data, a=1, b=2))
