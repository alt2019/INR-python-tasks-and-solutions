#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def example_01():
	print('\n*** Example 01 ***')
	print('Литералы')
	print('  45 =>',   45)
	print('0x45 =>', 0x45, '  (4 * 16 + 5)')
	print('0o45 =>', 0o45, '  (4 * 8 + 5)')
	print('0b1101 =>', 0b1101, '  (1 * 8 + 1 * 4 + 0 * 2 + 1)')

def example_02():
	print('\n*** Example 02 ***')
	print('Числа и приведение типов')
	a = 25 + int("28") ; print(a) # => 53
	b = str(25) + "28" ; print(b) # => "2528"
	c = 3 + int(2.8)   ; print(c, type(c)) # => 5 <class 'int'>
	print(123, 0x123, 0o123, 0b1101)
	print(1.23, 12., .12, 1.2e3, 1.2+3.4j, 3.4J)

def example_03():
	print('\n*** Example 03 ***')
	print('Деление и округление')
	a = 5 // 2; print(a, type(a))
	a = 5.8 / 2; print(a, type(a))
	a = 5.8 // 2; print(a, type(a))
	a = round(5.8 / 2); print(a, type(a))
	a = 5.2 / -2; print(a, type(a))
	a = 5.2 // -2; print(a, type(a))
	a = 5.2 // -2; print(a, type(a))
	a = round(5.8 / -2); print(a, type(a))
	# Число это объект и как объект имееет методы.
	# Однако применить метод к числовому литералу нельзя:
	# print(31.bit_length()) # => Ошибка: SyntaxError: invalid syntax
	print(int(31).bit_length()) # => 5
	# Трехместный оператор if - else
	message = 'less than five' if int(31).bit_length() < 5 else 'five or greater'
	print(message)

def example_04():
	print('\n*** Example 04 ***')
	print('Строки и символы')
	print("ord('я')  =>", ord('я'))   # => 1103
	#print("ord('яя') =>", ord('яя')) # => Ошибка
	print('chr(1103) =>', chr(1103))  # => я

def example_05():
	print('\n*** Example 05 ***')
	print('Создание объекта')
	print('   === Строки ===')
	s1 = 'abcdef'
	s2 = str(s1)
	s3 = s2[:]
	print(s1)
	print(s2)
	print(s3)

	print('   === Байты ===')
	a1 = b'abcdef'
	a2 = bytearray(a1)
	a3 = a2.copy()
	a4 = a3[:]
	a5 = bytearray.fromhex('B9 01EF') # Пробелы игнорируются
	s6 = a5.hex() # => 'b901ef'
	print(a1)
	print(a2)
	print(a3)
	print(a4)
	print(a5)
	print(s6)

def example_06():
	print('\n*** Example 06 ***')
	print('Операции со строками')
	s = 'abcdef'; print('s =>', s)
	print('s[2:] =>', s[2:]) # => 'cdef'
	print('s[:-2] =>', s[:-2]) # => 'abcd'
	print('s[:] =>', s[:]) # => 'abcdef'
	print('s[::2] =>', s[::2]) # => 'ace'
	s2 = 'Abc' * 6; print("('Abc' * 6) =>", s2)
	s3 = s2.replace('cA', '-'); print("('Abc' * 6).replace('cA', '-') =>", s3) # => Ab-b-b-b-b-bc
	s4 = 72 * '='; print("(s = 72 * '=') =>", s4)
	# Применить метод к литералу-строке можно:
	print('Found at position', 'Sample lamp'.find('am')) # => Found at position 1
	print('Found at position', 'Sample lamp'.rfind('am')) # => Found at position 8

def example_07():
	print('\n*** Example 07 ***')
	print('Поиск и замена')
	print('   === Строки ===')
	s1 = '123 456 654 321'
	print('s1', s1)
	print("s1.count('4')       ", s1.count('4'))
	print("s1.find('4')        ", s1.find('4'))
	print("s1.rfind('4')       ", s1.rfind('4'))
	print("s1.index('4')       ", s1.index('4'))
	print("s1.rindex('4')      ", s1.rindex('4'))
	print("s1.replace('4')     ", s1.replace('4', '?'))
	print("s1.replace('4', 1)  ", s1.replace('4', '?', 1))
	print("s1.startswith('123')", s1.startswith('123'))
	print("s1.endswith('321')  ", s1.endswith('321'))
	print("'456' in s1         ", '456' in s1)
	print("'457' in s1         ", '457' in s1)

	print('   === Байты ===')
	# Допустимы как bytes так и bytearray
	a1 = b'123 456 654 321'
	#a1 = bytearray(b'123 456 654 321')
	print('a1', a1)
	print("a1.count(b'4')       ", a1.count(b'4'))
	print("a1.find(b'4')        ", a1.find(b'4'))
	print("a1.rfind(b'4')       ", a1.rfind(b'4'))
	print("a1.index(b'4')       ", a1.index(b'4'))
	print("a1.rindex(b'4')      ", a1.rindex(b'4'))
	print("a1.replace(b'4')     ", a1.replace(b'4', b'?'))
	print("a1.replace(b'4', 1)  ", a1.replace(b'4', b'?', 1))
	print("a1.startswith(b'123')", a1.startswith(b'123'))
	print("a1.endswith(b'321')  ", a1.endswith(b'321'))
	print("b'456' in s1         ", b'456' in a1)
	print("b'457' in s1         ", b'457' in a1)

def example_08():
	print('\n*** Example 08 ***')
	print('Разделение и соединение')
	print('   === Строки ===')
	s1 = '123 456 654 321'
	print('s1', s1)
	print('s1.split()           ', s1.split())
	print('s1.split(maxsplit=2) ', s1.split(maxsplit=2))
	print('s1.rsplit(maxsplit=2)', s1.rsplit(maxsplit=2))
	print("s1.split('4')       ", s1.split('4'))
	print("s1.partition('4')   ", s1.partition('4'))
	print("s1.rpartition('4')  ", s1.rpartition('4'))
	print("s1.rpartition('4')  ", '--'.join(s1.split()))
	s2 = 'Line 1\nLine 2\nLast line'
	print('s2', s2)
	print('s2.splitlines()      ', s2.splitlines())

	print('   === Байты ===')
	# Допустимы как bytes так и bytearray
	a1 = b'123 456 654 321'
	#a1 = bytearray(b'123 456 654 321')
	print('a1', a1)
	print('a1.split()           ', a1.split())
	print('a1.split(maxsplit=2) ', a1.split(maxsplit=2))
	print('a1.rsplit(maxsplit=2)', a1.rsplit(maxsplit=2))
	print("a1.split(b'4')       ", a1.split(b'4'))
	print("a1.partition(b'4')   ", a1.partition(b'4'))
	print("a1.rpartition(b'4')  ", a1.rpartition(b'4'))
	print("a1.rpartition(b'4')  ", b'--'.join(a1.split()))
	a2 = bytearray(b'Line 1\nLine 2\nLast line')
	print('a2', a2)
	print('a2.splitlines()      ', a2.splitlines())

def example_09():
	print('\n*** Example 09 ***')
	print('Методы модифицирующие объект')
	print('   === Модифицирующие методы к типам str и bytes неприменимы ===')

	print('   === Байтовые массивы ===')
	a1 = bytearray(b'123 456 654 321')
	print('a1', a1)
	a1.append(0x61)         ; print("a1.append(0x61)        ", a1)
	a1.extend([0x41, 0x43]) ; print("a1.extend([0x41, 0x43])", a1)
	a1.insert(2, 0x62)      ; print("a1.insert(2, 0x62)     ", a1)
	a1.remove(0x41)         ; print("a1.remove(0x41)        ", a1)
	a1.reverse()            ; print("a1.reverse()           ", a1)
	print("a1.pop()               ", chr(a1.pop()))  ; print('a1', a1)
	print("a1.pop(3)              ", chr(a1.pop(3))) ; print('a1', a1)
	print("a1.pop(-3)             ", chr(a1.pop(-3))); print('a1', a1)
	a1.clear()              ; print("a1.clear()             ", a1)

def example_10():
	print('\n*** Example 10 ***')
	print('Методы форматирования текста')
	print('   === Строки ===')
	s1 = 'text example\taNd Other words'
	print('s1', s1)
	print("s1.capitalize()   ", s1.capitalize())
	print("s1.title()        ", s1.title())
	print("s1.expandtabs()   ", s1.expandtabs())
	print("s1.ljust(36)      ", s1.ljust(36))
	print("s1.center(36)     ", s1.center(36))
	print("s1.rjust(36)      ", s1.rjust(36))
	print("s1.lower()        ", s1.lower())
	print("s1.upper()        ", s1.upper())
	print("s1.swapcase()     ", s1.swapcase())
	s2 = '   123   '
	print('s2', s2)
	print("s2.strip()        ", s2.strip())
	print("s2.lstrip()       ", s2.lstrip())
	print("s2.rstrip()       ", s2.rstrip())
	print("'123'.zfill(3)   ", '123'.zfill(3))
	print("'123'.zfill(6)   ", '123'.zfill(6))

	print('   === Байты ===')
	# Допустимы как bytes так и bytearray
	a1 = b'text example\taNd Other words'
	#a1 = bytearray(b'text example\taNd Other words')
	print('a1', a1)
	print("a1.capitalize()   ", a1.capitalize())
	print("a1.title()        ", a1.title())
	print("a1.expandtabs()   ", a1.expandtabs())
	print("a1.ljust(36)      ", a1.ljust(36))
	print("a1.center(36)     ", a1.center(36))
	print("a1.rjust(36)      ", a1.rjust(36))
	print("a1.lower()        ", a1.lower())
	print("a1.upper()        ", a1.upper())
	print("a1.swapcase()     ", a1.swapcase())
	a2 = b'   123   '
	print('a2', a2)
	print("a2.strip()        ", a2.strip())
	print("a2.lstrip()       ", a2.lstrip())
	print("a2.rstrip()       ", a2.rstrip())
	print("b'123'.zfill(3)   ", b'123'.zfill(3))
	print("b'123'.zfill(6)   ", b'123'.zfill(6))

def example_11():
	print('\n*** Example 11 ***')
	print('Информация о тексте')
	print('   === Строки ===')
	print("' \\t\\r\\n\\f '.isspace()", ' \t\r\n\f '.isspace())
	print("'1234'.isdigit()", '1234'.isdigit())
	#print("'text'.isascii()", 'text'.isascii())
	print("'text'.isalpha()", 'text'.isalpha())
	print("'txt2'.isalnum()", 'txt2'.isalnum())
	print("'text'.islower()", 'text'.islower())
	print("'TEXT'.isupper()", 'TEXT'.isupper())
	print("'Text'.istitle()", 'Text'.istitle())

	print('   === Байты ===')
	print("b' \\t\\r\\n\\f '.isspace()", b' \t\r\n\f '.isspace())
	print("b'1234'.isdigit()", b'1234'.isdigit())
	#print("b'text'.isascii()", b'text'.isascii())
	print("b'text'.isalpha()", b'text'.isalpha())
	print("b'txt2'.isalnum()", b'txt2'.isalnum())
	print("b'text'.islower()", b'text'.islower())
	print("b'TEXT'.isupper()", b'TEXT'.isupper())
	print("b'Text'.istitle()", b'Text'.istitle())

def example_12():
	print('\n*** Example 12 ***')
	print('Трансляция')
	print('   === Строки ===')
	s1 = 'Last lump'
	print('s1', s1)
	ts = str.maketrans('aLup', 'eBib')
	print("s1.translate()", s1.translate(ts)) # => 'Best limb'

	print('   === Байты ===')
	a1 = bytes(b'Last lump')
	print('a1', a1)
	ta = bytes.maketrans(b'aLup', b'eBib')
	print("a1.translate()", a1.translate(ta)) # => b'Best limb'

def example_13():
	print('\n*** Example 13 ***')
	print('Преобразования между байтами и строками')
	s = 'Home Дом'
	b = s.encode('utf-8')
	c = s.encode() # Кодирование с использованием текущей кодировки ОС
	print('s:', s, ', length =', len(s)) # => Home Дом , length = 8
	print('b:', b, ', length =', len(b)) # => b'Home \xd0\x94\xd0\xbe\xd0\xbc' , length = 11
	print('c:', c, ', length =', len(c)) # => b'Home \xd0\x94\xd0\xbe\xd0\xbc' , length = 11
	b2 = b'Home \xd0\x94\xd0\xbe\xd0\xbc'
	s2 = b2.decode('utf-8')
	t2 = b2.decode() # Декодирование с использованием текущей кодировки ОС
	print('b2:', b2, ', length =', len(b2)) # => b'Home \xd0\x94\xd0\xbe\xd0\xbc' , length = 11
	print('s2:', s2, ', length =', len(s2)) # => s: Home Дом , length = 8
	print('t2:', t2, ', length =', len(t2)) # => s: Home Дом , length = 8
	# b3 = bytes('Home Дом') # => Вызывает ошибку, указание кодировки обязательно
	b3 = bytes('Home Дом', 'utf-8')
	s3 = str(b'Home \xd0\x94\xd0\xbe\xd0\xbc', 'utf-8')
	print('b3:', b3, ', length =', len(b3)) # => b'Home \xd0\x94\xd0\xbe\xd0\xbc' , length = 11
	print('s3:', s3, ', length =', len(s3)) # => s: Home Дом , length = 8
	# Без указания кодировки получим строку с буквальным текстом двоичного литерала
	s4 = str(b'Home \xd0\x94\xd0\xbe\xd0\xbc')
	print('s4:', s4, ', length =', len(s4)) # => "b'Home \xd0\x94\xd0\xbe\xd0\xbc'" , length = 32
	a1 = bytearray('Русский текст'.encode('utf-8'))
	a1.pop(3) # Удален один байт из двухбайтового символа
	#print("a1.decode()   ", a1.decode()) # => ошибка, utf-8 испорчен
	print("a2.decode()   ", a1.decode(errors='replace'))
	print("a2.decode()   ", a1.decode(errors='ignore'))

def example_14():
	print('\n*** Example 14 ***')
	print('Низкий приоритет трехместного оператора if else')
	a = 0
	b =      2 if a > 0 else 10      # => 10
	c = 3 +  2 if a > 0 else 10  / 5 # => 2.0
	d = 3 + (2 if a > 0 else 10) / 5 # => 5.0
	print('1: a =', a, 'b =', b, 'c =', c, 'd =', d)
	a = 1
	b =      2 if a > 0 else 10      # => 2
	c = 3 +  2 if a > 0 else 10  / 5 # => 5
	d = 3 + (2 if a > 0 else 10) / 5 # => 3.4
	print('2: a =', a, 'b =', b, 'c =', c, 'd =', d)

def example_15():
	print('\n*** Example 15 ***')
	print('Влияние оптимизации на оператор is')
	a = '1' + '5'
	b = '1' + '5'
	print('a =', a, 'b =', b)
	print('a == b', a == b)
	print('a is b', a is b)
	c = '1' + '5'
	d = '1' + str(5)
	print('c =', c, 'd =', d)
	print('c == d', c == d)
	print('c is d', c is d)

def example_16():
	print('\n*** Example 16 ***')
	print('Изменение порядка выполнения операторов')
	a = 7 + 3 * 10 # => 37
	print('a =', a)
	b = (7 + 3) * 10 # => 100
	print('b =', b)

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
example_14()
example_15()
example_16()
