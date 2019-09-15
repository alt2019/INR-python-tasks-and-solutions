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

def example_01():
	"""
	Простой пример перехвата исключения
	"""
	pfi()
	
	def get_by_index(i):
		a = [0, 1, 2]
		# x = a[7] # => IndexError: list index out of range
		try:
			x = a[i]
			print('After assignment: x =', x)
		except IndexError:
			print('ERROR:', 'Invalid index')
		print('Code after try block')

	phdr('get_by_index(1)')
	get_by_index(1)
	phdr('get_by_index(7)')
	get_by_index(7)

def example_02():
	"""
	Возбуждение исключения, инструкция raise
	"""
	pfi()

	def divide_2_by(n):
		y = 2.0
		# x = y / 0.0 # => ZeroDivisionError: float division by zero
		print('Divider =', n)
		# Числа меньше 0.1 полагаем нулями
		if abs(n < 0.1):
			raise ZeroDivisionError
		else:
			return y / n

	def divide_test(n):
		try:
			phdr('divide_2_by(' +  str(n) + ')')
			x = divide_2_by(n)
			print('After division: x =', x)
		except ZeroDivisionError:
			print('ERROR:', 'ZeroDivisionError')
		print('Code after try block')

	divide_test(2.0)
	divide_test(0.05)

def example_03():
	"""
	Класс исключения, определенный пользователем
	"""
	pfi()

	class DeviceConnectionFailed(Exception):
		pass

	# Параметр инструкции raise может быть как классом исключения,
	# так и объектом этого класса. В первом случае объект класса
	# исключения создается автоматически
	def connect():
		"Использует класс исключения, \
		объект исключения будет создан автоматически"
		raise DeviceConnectionFailed
	def connect2():
		"Использует объект исключения"
		raise DeviceConnectionFailed()

	try:
		phdr('connect')
		connect()
		print('After connect')
	except DeviceConnectionFailed as e:
		print('ERROR:', 'DeviceConnectionFailed', e.__class__)
	print('Code after try block')

	try:
		phdr('connect2')
		connect()
		print('After connect2')
	except DeviceConnectionFailed as e:
		print('ERROR:', 'DeviceConnectionFailed()', e.__class__)
	print('Code after try block')

def example_04():
	"""
	Блоки finally и else
	"""
	pfi()

	def divide_by(n):
		try:
			2.0 / n
		finally:
			print('Finally division by', n)
		print('After division by', n)
	try:
		divide_by(2.0)
	except ZeroDivisionError:
			print('Division by zero occured')
	else:
		print('No errors')
	try:
		divide_by(0.0)
	except ZeroDivisionError:
			print('Division by zero occured')
	else:
		print('No errors')

def example_05():
	"""
	Порядок следования блоков в инструкции try
	"""
	pfi()

	try:
		2.0 / 0.0
	except IndexError:
		print('except IndexError')
	except (ZeroDivisionError, OverflowError):
		print('except (ZeroDivisionError, OverflowError)')
	except Exception:
		print('except Exception')
	except:
		print('except')
	else:
		print('else')
	finally:
		print('finally')

	'После блока try должен следовать как минимум один дополнительный блок'
	#try:
	#	2.0 / 0.0 # => SyntaxError: invalid syntax

	'Блоки except записываются сразу после try'
	try:
		2.0 / 0.0
	#finally: pass
	except: pass # => SyntaxError: invalid syntax

	'Блок except без параметров должен быть последним'
	try:
		2.0 / 0.0
	#except: pass # => SyntaxError: default 'except:' must be last
	except Exception: pass

	'Блок else нельзя использовать без except'
	#try:
	#	2.0 / 0.0
	#else:    # => SyntaxError: invalid syntax
	#	pass

	'Блок else записывается после всех блоков except'
	try:
		2.0 / 0.0
	except IndexError: pass
	#else: pass              # => SyntaxError: invalid syntax
	except Exception: pass

def example_06():
	"""
	Исключение и возврат статуса
	"""
	pfi()

	s = 'abcd'  
	token = 'cz'
	try:
		n = s.index(token)
		print('Token', token, 'found at index', n)
	except ValueError:
		print('Token', token, 'not found, ValueError exception')

	n = s.find(token)
	if n < 0:
		print('Token', token, 'not found: find() return', n)

def example_07():
	"""
	Модель цикла for
	"""
	pfi()

	a = [0, 1, 2]  

	for e in a:
		print(e)
		#break # пример неисполнения else
	else:
		print('All elements printed')

	i = iter(a)  

	while True:
		try:
			e = next(i)
			print(e)
			#break # пример неисполнения else
		except StopIteration:
			print('All elements printed')
			break

def example_08():
	"""
	Завершение функции-генератора вызывает
	исключение StopIteration
	"""
	pfi()

	def gen():
		a = [0, 1, 2]
		for e in a:
			yield e  
		print('Function gen() return')

	i = iter(gen())
	print(next(i)) # => 0
	print(next(i)) # => 1
	print(next(i)) # => 2
	try:
		print(next(i)) # => исключение StopIteration
	except Exception as e:
		print(e.__class__)
		print(e) # Исключение StopIteration не содержит пояснительного текста

def example_09():
	"""
	Исключение внутри обработчика исключения
	"""
	pfi()

	class DeviceConnectionFailed(Exception):
		pass
	try:
		try:
			'Connection reset by peer'.index('connected')
			print('Connection established')
		except ValueError as ve:
			print('Internal except', ve.__class__)
			raise DeviceConnectionFailed from ve
	except Exception as be:
		print('External except', be.__class__)
		print('      caused by', be.__cause__.__class__)

def example_10():
	"""
	Инструкция assert
	"""
	pfi()

	# При обычном запуске интерпретатора __debug__ == True
	# При запуске интерпретаторас ключом -О __debug__ == False
	print('__debug__ =', __debug__)
	n = -1
	try:
		assert n > 0, 'one'
	except AssertionError as ex:
		print(ex.__class__, ex)
	# __debug__ = False # => Изменить значение __debug__ нельзя
	try:
		assert n > 0, 'two'
	except AssertionError as ex:
		print(ex.__class__, ex)

	def divide_2_by(n):
		assert n != 0, 'assert non-zero'
		return 2.0 / n
	try:
		divide_2_by(2)
		divide_2_by(0)
	except AssertionError as ex:
		print('divide_2_by(', ex, ') ecxepted with AssertionError')
	except ZeroDivisionError as ex:
		print('divide_2_by(', ex, ') ecxepted with ZeroDivisionError')

	
def example_11():
	"""
	Менеджер контекста with
	"""
	pfi()
	filename = 'sample.txt'

	def write_unwritable_file():
		with open(filename) as f:
			total_lines = 0
			f.write('abc')

	def read_file():
		with open(filename) as f:
			total_lines = 0
			# with срабатывает на все ошибки, не только на ошибки
			# контекстного объекта
			2.0 / 0.0
			a = f.read()

	try:
		write_unwritable_file()
	except Exception as e:
		print('ERROR in write_unwritable_file():', repr(e))

	try:
		read_file()
	except Exception as e:
		print('ERROR in read_file():', e)
	
def example_12():
	"""
	Несколько контекстов в одной инструкции with
	"""
	pfi()

	with open('test_a.txt', 'w') as fa, open('test_b.txt', 'w') as fb:
		 fa.write('This is file a\n')
		 fb.write('This is file b\n')
	try:
		fa.write('The second line\n')
	except Exception as ex:
		print('fa.write()', ex)
	try:
		fb.write('The second line\n')
	except Exception as ex:
		print('fb.write()', ex)

def example_13():
	"""
	Реализация протокола менеджера контекста (PEP-343)
	"""
	pfi()

	class A:
		def __enter__(self):
			print('Initial context object code')
			return 'a string as context object'
			#return self

		def __exit__(self, type_, value, traceback):
			# type_, value и traceback это величины,
			# возвращаемые sys.exc_info()
			print('Final context object code:')
			print('  type  =', type_)
			print('  value =', value, value.__class__)
			print('  traceback =', traceback)
			return True # stop exception propogation 
			#return False # propogate exception

	phdr('No error in with block')
	with A() as a:
		print('Context object =', a, 'of', a.__class__)
		x = 2 / 1
		print('End of valid with block')
	print('Print line after valid with block\n')

	phdr('Error in with block')
	with A() as a:
		print('Context object =', a, 'of', a.__class__)
		x = 2 / 0  # with перехватывает все ошибки исполнения программы
		sys.exit() # with перехватывает исключение завершения программы SystemExit
		# x = 2  0 # Синтаксические ошибки (исключение SyntaxError) НЕ ПЕРЕХВАТЫВАЮТСЯ
		print('End of error with block')
	print('Print line after error with block\n')

	print('Context object is available after with block:', a, 'of', a.__class__)

def example_14():
	"""
	Пример класса с реализацией протокола менеджера контекста
	"""
	pfi()

	def finalize_data_processing(): print('finalize')
	def disconnect_remote_device(dev): print('disconnect')
	def process_data_block(data): print('process'); x = 2 / 0

	class RemoteDevice:
		def __enter__(self):
			self.device_handler = self.connect_remote_device()
			return self.device_handler

		def __exit__(self, type_, value, traceback):
			finalize_data_processing()
			disconnect_remote_device(self.device_handler)
			return True # comment this line to propogate exception

		def connect_remote_device(self):
			print('connect')
			return self

		def read(self):
			return 'data values'

	with RemoteDevice() as dev:
		while True:
			data = dev.read()
			if not data:
				break
			process_data_block(data)
	print('continue program execution')

def example_15():
	"""
	Декоратор @contextmanager
	"""
	pfi()

	def connect_remote_device(): print('connect'); return 'sometning'
	def finalize_data_processing(): print('finalize')
	def disconnect_remote_device(dev): print('disconnect')
	def process_data_block(data): print('process'); x = 2 / 0
	def read(dev): return 'data values'

	from contextlib import contextmanager

	@contextmanager
	def remote_device():
		device_handler = connect_remote_device()
		try:
			yield device_handler
		finally:
			finalize_data_processing()
			disconnect_remote_device(device_handler)
			return True # comment this line to propogate exception

	with remote_device() as dev:
		while True:
			data = read(dev)
			if not data:
				break
			process_data_block(data)
	print('continue program execution')

def example_16():
	"""
	Функция sys.exc_info() как альтернатива as var
	"""
	pfi()

	phdr('as var')
	try:
		2.0 / 0.0
	except ArithmeticError as ex:
		print('ArithmeticError', ex)
	phdr('sys.exc_info()')
	try:
		2.0 / 0.0
	except:
		print('except:', sys.exc_info()[0], '/', sys.exc_info()[1])
		print('Traceback:', sys.exc_info()[2])

def example_17():
	"""
	Аргументы при создании объекта исключения
	"""
	pfi()

	class DeviceConnectionFailed(Exception):
		pass

	def connect():
		raise DeviceConnectionFailed
	def connect2():
		raise DeviceConnectionFailed('Link brorken')
	def connect3():
		raise DeviceConnectionFailed('Link brorken,', 'distance', 12, 'miles')

	try: connect()
	except DeviceConnectionFailed as e: print('ERROR 1:', e)
	try: connect2()
	except DeviceConnectionFailed as e: print('ERROR 2:', e)
	try: connect3()
	except DeviceConnectionFailed as e: print('ERROR 3:', e)
	try: connect3()
	except DeviceConnectionFailed as e: print('ERROR 4:', ' '.join(map(str, e.args)))

def example_18():
	"""
	Метод __str__() в классе исключения
	"""
	pfi()

	class DeviceConnectionFailed(Exception):
		def __str__(self):
			return 'ERROR 3: Caused by ' + ' '.join(map(str, self.args))

	def connect3():
		raise DeviceConnectionFailed('Link brorken,', 'distance', 12, 'miles')

	try:
		connect3()
	except DeviceConnectionFailed as e:
		print(e)

def example_19():
	"""
	Блок finally
	"""
	pfi()

	def divide_2_by(n):
		try:
			x = 2.0 / n
			print('A: x =', x)
		finally:
			print('B: Finally division by', n)
		print('C: After division by', n)  

	phdr('divide_2_by(2.0)')
	try:
		divide_2_by(2.0)
	except ZeroDivisionError:
		print('D: Division by zero occured')
	# => A: x = 1.0
	# => B: Finally division by 2.0
	# => C: After division by 2.0

	phdr('divide_2_by(0.0)')
	try:
		divide_2_by(0.0)
	except ZeroDivisionError:
		print('D: Division by zero occured')
	# => B: Finally division by 0.0
	# => D: Division by zero occured

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
