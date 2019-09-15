#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
python3 -c "print(`id -u` % 5 + 1)"
->1
"""


def step1(string):
	"""Вывести на экран строку, содержащую шестнадцатеричные коды 
	первых трех символов строки s. 
	Например, для строки 'abcd' результат должен быть '616263'."""
	s1 = string.encode()
	s2 = bytearray(s1[0:3])
	s3 = s2.hex()
	return s3


def step2(intNum):
	"""Вычислить сумму трех литералов, каждый из которых является 
	представлением числа x в шестнадцатеричной (первый литерал), 
	восьмеричной (второй литерал), и двоичной (третий литерал) форме. 
	Каким образом Вы нашли эти литералы ? Вывести результат на экран."""
	return hex(intNum) + oct(intNum) + bin(intNum)


def step3(string):
	"""Строка s содержит два числа. Вывести на экран 
	измененную строку s, в которой на месте второго числа 
	находится его сумма с результатом первой операции"""
	num1 = string[6:8]
	num2 = string[17:20]
	num3 = num2 + step1(s)
	numm = bytearray(num3.encode())
	s2 = bytearray(string.encode())
	s2[17:20] = numm
	s3 = s2.decode()
	print("modified string:", s3)


def step4(number):
	"""Результат первой операции разделить на число y. 
	Если результат деления больше единицы вывести на экран строку s, 
	в противном случае вывести на экран строку t"""
	print("string:", s) if (int(step1(s))/number)>1 else print("string:", t)


def step5(string, method, encoding):
	"""Создать байтовый массив, содержащий испорченный 
	русский текст в кодировке utf-8, для которого метод 
	decode будет давать ошибку. Обработать ошибку 
	методом m и вывести декодированную строку на экран."""
	a1 = bytearray(string.encode(encoding))
	print("decoded string:", a1.decode(errors=method))


if __name__ == '__main__':
	x = 197 
	y = 713 
	s = "First 23, second 19" 
	# s ='abcd'
	t = "Too less"
	m = "replace"
	# m = "ignore"

	a1 = step1(s)
	# print(step1.__doc__)
	print("16_code:", a1)
	a2 = step2(x)
	print("sum of 3 literals:", a2)
	step3(s)
	step4(y)

	# str1 = 'Р СѓСЃСЃРєРР‘РµР· СѓРєР°Р·Р°РЅРёСЏ РєРѕРґРёСЂРѕРІРєРё РїРѕР»СѓС‡РёРј СЃС‚СЂРѕРєСѓ СЃ Р±СѓёР№ С‚РµРєСЃС‚'
	# test = некоторый текст
	# str1 = 'íćêîòîđûé òćêńò' # ISO-8859-16 <- CP1251
	# str1 = 'ÎĹËĎÔĎŇŮĘ ÔĹËÓÔ' # CP1250 <- KOI8-R
	# str1 = '╬┼╦╧╘╧╥┘╩ ╘┼╦╙╘' # CP866 <- KOI8-R
	str1 = 'некоторый текст'
	step5(str1, m, 'cp1251')
	step5(str1, m, 'KOI8-R')
	step5(str1, m, 'utf-8')
