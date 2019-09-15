#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Для исполнения одного примера задайте его номер
в качестве параметра при запуске программы.
Используйте параметр h или help для просмотра
документации к функциям и классам примеров.
"""

import sys

def pfi():
	"Print function information"
	caller_code = sys._getframe(1).f_code
	example_no = caller_code.co_name[-2:]
	h = '*' * 6
	print('\n       ', h, 'Example', example_no, h)
	print(caller_code.co_consts[0])

def phdr(s):
	"Paragraph header"
	h = '=' * 3
	print('   ', h, s, h)

def m(s):
	"Print mark at line begin"
	print(s + ' => ', end='')

def good(pattern):
	print("'" + pattern + "'", '=> Match')

def bad(pattern):
	print("'" + pattern + "'", '=> Failed')

def check(pattern, text):
	if re.match(pattern, text):
		good(pattern)
	else:
		bad(pattern)

# Необходимо импортировать модуль re
import re

def print_groups(m, pattern=''):
	if m:
		print(pattern, '=> ', end='')
		try:
			for i in range(1, 999):
				print(str(i) + ':(' + str(m.group(i)) + ')', end=' ')
		except IndexError:
			pass
		finally:
			print('0:(' + str(m.group(0)) + ')')
	else:
		print(pattern, '=> Failed')

def groups(pattern, text):
	m = re.match(pattern, text)
	print_groups(m, pattern)

def example_01():
	"""
	Традиционная операция поиска
	"""
	pfi()

	text = 'Simple pattern'
	
	pattern = 'at'
	good(pattern) if text.find(pattern) >= 0 else bad(pattern)
	try:
		print('at index =', text.index(pattern))
	except ValueError:
		print('at not found')
	
	pattern = 'et'
	good(pattern) if text.find(pattern) >= 0 else bad(pattern)
	try:
		print('et index =', text.index(pattern))
	except ValueError:
		print('et not found')

def example_02():
	"""
	Регулярные выражения, простые примеры
	"""
	pfi()

	check(r'\s', 'Simple pattern') # => Failed, сопоставление идет с начала текста
	good("search(r'\s')") if re.search(r'\s', 'Simple pattern') else bad("search(r'\s')") # => Match
	check(r'......\s', 'Simple pattern') # => Match - пробел после шести любых символов
	# Конструкция \c, где символ c не имеет специального значения
	# check(r'..\z', r'Buzz') # => Match
	# До версии 3.6 символ \ игнорировался, а символ z c воспринимался "как есть"
	# Начиная с версии 3.6 это ошибка -- re.error: bad escape \z at position 2

def example_03():
	"""
	Функция compile()
	"""
	pfi()

	text = 'Simple pattern'
	pattern = r'......\s'
	code = re.compile(pattern)
	phdr("code.match('" + text + "')")
	result = code.match(text)
	good(pattern) if result else bad(pattern)
	phdr("code.search('" + text + "')")
	pattern = r'\s'
	result = code.search(text)
	good(pattern) if result else bad(pattern)
	print('code is object of', code.__class__)
	print('result is object of', result.__class__)

def example_04():
	"""
	Методы объекта регулярного выражения
	"""
	pfi()

	text = 'Simple pattern'
	r = re.compile('impl')
	print(r.match(text))       # => None
	print(r.match(text, 1))    # => <Match object; span=(1, 5), match='impl'>
	print(r.match(text[1:]))   # => <Match object; span=(0, 4), match='impl'>
	print(r.match(text, 1, 4)) # => None # текст слишком короток

def example_05():
	"""
	Функция search()
	Методы объекта совпадения
	"""
	pfi()

	text = 'Simple pattern'
	pattern = r'\s'
	result = re.search(pattern, text)
	if result:
		print('Found', pattern, 'in', text, '- starts at',
		result.start(), 'ends at', result.end(), 'span is', result.span())

def example_06():
	"""
	Квантификаторы
	"""
	pfi()

	text = 'ab3815z'
	check(r'\d*', text) # => Match - ни одной цифры в начале строки
	check(r'\d+', text) # => Failed - в начале строки не цифра
	check(r'ab\d+', text) # => Match - более одной цифры
	check(r'ab\d{4}', text) # => Match - есть 4 цифры
	check(r'ab\d{3}', text) # => Match - есть 3 цифры
	check(r'ab\d{3,}', text) # => Match - есть 3 цифры или более
	check(r'ab\d{5}', text) # => Failed - нет 5 цифр
	check(r'ab\d{3,5}', text) # => Match - от 3 до 5 цифр

def example_07():
	"""
	Наборы символов и greedy алгоритм
	"""
	pfi()

	text = 'Scattered dotted plot'
	phdr(text)
	groups(r'[AES]c', text) # => [AES]c => 0:(Sc)
	groups(r'[A-Zaz][AZa-z]a', text) # => 0:(Sca)
	groups(r'[A-Za-z]+a', text) # => 0:(Sca)
	groups(r'[A-Za-z]+', text) # => 0:(Scattered)
	groups(r'[A-Za-z]+?', text) # => 0:(S)
	groups(r'\w+', text) # => 0:(Scattered)
	groups(r'.+tt', text) # => 0:(Scattered dott)
	groups(r'(.+)(tt)', text) # => 1:(Scattered do) 2:(tt) 0:(Scattered dott)
	groups(r'(.+?)(tt)', text) # => 1:(Sca) 2:(tt) 0:(Scatt)
	groups(r'(.+)(d)(.+)(tt)', text) # => => 1:(Scattered ) 2:(d) 3:(o) 4:(tt) 0:(Scattered dott)

def example_08():
	"""
	Группы
	"""
	pfi()

	text = '80de-7903-1fd2-fe19'
	phdr(text)
	pattern = r'([\da-f]+)-([\da-f]+)-([\da-f]+)-([\da-f]+)'
	groups(pattern, text)
	phdr('Комментарий')
	pattern = r'([\da-f]+)-(?#Это комментарий)([\da-f]+)-([\da-f]+)-([\da-f]+)'
	groups(pattern, text)
	phdr('Вторая группа незахватывающая')
	pattern = r'([\da-f]+)-(?:[\da-f]+)-([\da-f]+)-([\da-f]+)'
	groups(pattern, text)
	phdr('Именованные группы')
	pattern = r'(?P<first>[\da-f]+)-(?P<second>[\da-f]+)-\
(?P<third>[\da-f]+)-(?P<last>[\da-f]+)'
	m = re.match(pattern, text)
	if m: print(m.groupdict())
	pattern = r'([\da-f]+)-(?P<second>[\da-f]+)-([\da-f]+)-([\da-f]+)'
	phdr('pattern = ' + pattern)
	phdr('groupdict() содержит только именованные группы')
	m = re.match(pattern, text)
	if m:
		print(m.groupdict())
		phdr('Именованные группы подчиняются общей нумерации')
		print_groups(m)

def example_09():
	"""
	Группа с квантификатором запоминает последнее совпадение
	"""
	pfi()

	text = 'a1ca2ca3c'
	pattern = r'(a.c)+'
	m = re.match(pattern, text)
	print_groups(m) # => 1:(a3c) 0:(a1ca2ca3c)

def example_10():
	"""
	Отмена greedy алгоритма
	"""
	pfi()

	text = 'Simple pattern'
	m1 = re.match(r'.*at+', text)
	print(m1) # => <Match object; span=(0, 11), match='Simple patt'>
	m2 = re.match(r'.*at+?', text)
	print(m2) # => <Match object; span=(0, 10), match='Simple pat'>
	m3 = re.match(r'.*at*', text)
	print(m3) # => <Match object; span=(0, 11), match='Simple patt'>
	m4 = re.match(r'.*at*?', text)
	print(m4) # => <Match object; span=(0, 11), match='Simple patt'>
	m5 = re.match(r'.*at*?te', text)
	print(m5) # => <Match object; span=(0, 12), match='Simple patte'>

	phdr('Пример с группами')
	text = 'ieee-specrtum'
	groups(r'i(e*?)', text)      # => 1:() 0:(i)
	groups(r'i(e*?)(ee-)', text) # => 1:(e) 2:(ee-) 0:(ieee-)
	groups(r'i(e*?)(e-)', text)  # => 1:(ee) 2:(e-) 0:(ieee-)
	groups(r'i(e*?)(-)', text)   # => 1:(eee) 2:(-) 0:(ieee-)

def example_11():
	"""
	Номер группы как параметр метода объекта совпадений
	"""
	pfi()

	def print_result(r, g):
		print('{:6} {:2} {:2} {}'.format(
			r.group(g), r.start(g), r.end(g), r.span(g)))
	
	text = 'Simple pattern'
	r = re.compile(r'(.*)(\s+\w+)(t+)(\w+)')
	result = r.match(text)
	if result:
		print_result(result, 1) # => 'Simple' 0  6  (0,  6)
		print_result(result, 2) # => ' pat'   6 10  (6, 10)
		print_result(result, 3) # => 't'     10 11 (10, 11)
		print_result(result, 4) # => 'ern'   11 14 (11, 14)

def example_12():
	"""
	Использование именованных групп
	"""
	pfi()

	url = 'https://www.new-company.org/news/articles/18'
	rc = re.compile(
	'http(?P<secure>s?)://\
(?P<site>[\w\-.]+)/(?P<division>\w+)/\
(?P<section>\w+)/(?P<page_no>\d*)')

	def send_html_page(secure, site, division, section, page_no):
		print('secure =', secure)
		print('site =', site)
		print('division =', division)
		print('section =', section)
		print('page_no =', page_no)

	m = rc.match(url)
	if m:
		send_html_page(**m.groupdict())
		send_html_page(*m.groups())
	else:
		print('Error 404: page not found')

def example_13():
	"""
	Обратная ссылка
	"""
	pfi()

	pattern = r"(\w+)\s+(\w+),\s+(\1's age)\s+(\d+),\s+([\w\.]+\s+(\2))"
	text = "John Doe, John's age 27, Mr. Doe"
	phdr(text)
	groups(pattern, text)
	text = "Jane Roe, Jane's age 24, Mrs. Roe"
	phdr(text)
	groups(pattern, text)

def example_14():
	"""
	Обратная ссылка для именованных групп
	"""
	pfi()

	pattern = r"(?P<first>\w+)\s+(?P<last>\w+),\s+((?P=first)'s age)\s+(\d+),\s+([\w\.]+\s+((?P=last)))"
	text = "John Doe, John's age 27, Mr. Doe"
	phdr(text)
	groups(pattern, text)
	text = "Jane Roe, Jane's age 24, Mrs. Roe"
	phdr(text)
	groups(pattern, text)

def example_15():
	"""
	Просмотр вперед и назад
	"""
	pfi()

	text = "John Doe, John's age 27, Mr. Doe"
	phdr(text)
	pattern = r".*John(?='s\s+age)('s\s+age)\s+(\d+),"
	groups(pattern, text)
	pattern = r".*John(?!\s+Doe)('s\s+age)\s+(\d+),"
	groups(pattern, text)
	pattern = r".*John(?=\s+Doe)\s+(\w+)"
	groups(pattern, text)

	pattern = r".*(?<=,\s)John('s\s+age)\s+(\d+),"
	#pattern = r".*(?<=,\s+)John" # Error: look-behind requires fixed-width pattern
	groups(pattern, text)
	pattern = r".*(?<!^)John('s\s+age)\s+(\d+),"
	groups(pattern, text)
	pattern = r".*(?<!,\s)John\s+(\w+)"
	groups(pattern, text)

def example_16():
	"""
	Группа с вариантами
	"""
	pfi()

	pattern = r"(John)?.*\d+,\s+(?(1)(Mr\.)|(Mrs\.))"
	text = "John Doe, John's age 27, Mr. Doe"
	groups(pattern, text)
	text = "Jane Roe, Jane's age 24, Mrs. Roe"
	groups(pattern, text)

def example_17():
	"""
	Функция split()
	"""
	pfi()

	text = "John Doe, John's age 27, Mr. Doe"
	pattern = r'[\s,.]+'
	print('text:', text)
	print('pattern:', pattern)
	print('Split by space:', text.split())
	print('Split by pattern:', re.split(pattern, text))

def example_18():
	"""
	Функции findall() и finditer(), поиск ненакладывающихся включений
	"""
	pfi()

	text = 'alalala'
	pattern = r'ala'
	print(re.findall(pattern, text)) # => ['ala', 'ala'] - 2 элемента
	for s in re.findall(pattern, text):
		print(s, s.__class__) # => ala <class 'str'> - 2 раза

def example_19():
	"""
	Функции sub() и subn(), поиск с заменой
	"""
	pfi()

	text = 'alalala'
	pattern = r'ala'
	replacement = 'O'
	print(re.sub(pattern, replacement, text)) # => 'OlO'
	print(re.subn(pattern, replacement, text, 1)) # => ('Olala', 1)

def example_20():
	"""
	Функция escape()
	"""
	pfi()

	text = 'Line. and() or[] ${}'
	print('original:', text)
	print('escaped:', re.escape(text))

def example_21():
	"""
	Исключения в регулярных выражениях
	"""
	pfi()

	try:
		re.match(r'\w+)', 'Text to test')
	except Exception as e:
		print('\nException class =', e.__class__, '\nError text =', e)
		print('Exception bases =', e.__class__.__bases__)
		if sys.version_info >= (3,5,0):
			print('msg =', e.msg)
			print('pattern =', e.pattern)
			print('pos =', e.pos)
			print('lineno =', e.lineno)
			print('colno =', e.colno)
	try:
		re.match(r'(\w+)\2', 'Text to test')
	except Exception as e:
		print('\nException class =', e.__class__, '\nError text =', e)
		print('Exception bases =', e.__class__.__bases__)
		if sys.version_info >= (3,5,0):
			print('msg =', e.msg)
			print('pattern =', e.pattern)
			print('pos =', e.pos)
			print('lineno =', e.lineno)
			print('colno =', e.colno)

	re.error('Error message', 'abc', 17)

def example_22():
	"""
	Метод expand()
	"""
	pfi()

	pesonal_card = """
	Фамилия: Иванов
	Имя: Владимир
	Отчество: Петрович
	Должность: инженер
	"""
	rc = re.compile('\n\
\s*Фамилия:\s+(\w+)\n\
\s*Имя:\s+(?P<name>\w+)\n\
\s*Отчество:\s+(\w+)\n\
\s*Должность:\s+(\w+)')

	m = rc.match(pesonal_card)
	if not m:
		print('Match failed')
		return
	print(m.groups())
	html_template = r"""
	<html><body><ul>
	<li>Фамилия: \1</li>
	<li>Имя: \g<name></li>
	<li>Отчество: \3</li>
	<li>Должность: \g<4></li>
	</ul></body></html>
	"""
	print(m.expand(html_template))

def example_23():
	"""
	Функции модуля re работают как со строками,
	так и с байтами
	"""
	pfi()

	bytes_sequence = b'Simple pattern'

	pattern = r'^S\w+\s'

	# re.match(pattern, bytes_sequence) # =>
	# TypeError: cannot use a string pattern on a bytes-like object

	bytes_pattern = b'^S\w+\s'

	m = re.match(bytes_pattern, bytes_sequence)
	print(m) # => <Match object; span=(0, 7), match=b'Simple '>

	m = re.search(b'tt', bytes_sequence)
	print(m) # => <Match object; span=(9, 11), match=b'tt'>
	
	m = re.findall(b'\we', bytearray(bytes_sequence))
	print(m) # => [b'le', b'te']
	
	replacement = b'lo'
	print(re.sub(b'\we', replacement, bytes_sequence)) # => b'Simplo patlorn'

if len(sys.argv) > 1:
	if sys.argv[1].isdigit() and int(sys.argv[1]) > 0:
		exec('example_%02d()' % int(sys.argv[1]))
	elif sys.argv[1][0].lower() == 'h':
		help(__name__)
	else:
		print(__doc__)
else:
	tuple(map(lambda c: exec(c + '()'),
		(f for f in sys._getframe().f_code.co_names
			if f.startswith('example_'))))
