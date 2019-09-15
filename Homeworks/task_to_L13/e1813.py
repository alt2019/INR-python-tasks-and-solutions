#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Для исполнения одного примера задайте его номер
в качестве параметра при запуске программы.
Изображение сохраняется в файле. Добавьте любой
второй параметр что бы показать изображение на экране.
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

# Необходимо импортировать модуль numpy
import numpy as np

# Необходимо импортировать модуль matplotlib
import matplotlib.pyplot as plt

# Показывать графики на экране (False) или сохранять в файлах (True)
to_file = True
#to_file = False

import sys
if len(sys.argv) > 1 and sys.argv[1] == 'slides':
	# Если задан аргумент slides, генерировать файлы для слайдов
	to_file = True
	# Изменение цвета фона внутри и вокруг графика
	plt.rcParams['axes.facecolor'] = '#F0EFC0'
	plt.rcParams['savefig.facecolor'] = '#F0EFC0'
	# Файлы будут сохранены в поддиректории 'img'
	import os
	imdir = 'img'
	if not os.path.exists(imdir):
		os.mkdir(imdir)
	os.chdir(imdir)

def finish(n=0, s=''):
	# Вывод изображения на экран или в файл
	if to_file:
		plt.savefig('ex%02d%s.png' % (n, s))
	else:
		plt.show()
	plt.close() # Close figure - очистка "холста"

def lsm(n=101, v_min=1, v_max=10):
	"Linear sample"
	return np.linspace(v_min, v_max, n, endpoint=True)

def rsm(n=101, v_min=1, v_max=10):
	"Random sample"
	scale = 10000
	return np.random.randint(v_min * scale, v_max * scale, n) / scale

def sca(offset=0):
	"Scale A"
	return(np.arange(0, 11) / 10 + offset)

def scale(a):
	try:
		size = a.size
	except:
		size = int(a)
	return(range(size))

def pla():
	"Plot A"
	xa = np.linspace(-np.pi, np.pi, 101, endpoint=True)
	ya = np.cos(xa)
	plt.plot(xa, ya, color='#ef7050') # Цвет в формате #rrggbb

def example_01(call_from_other_example=False):
	"""
	Простой график, два аргумента
	"""
	if not call_from_other_example:
		pfi()

	# Накопление данных для отображения
	xa = np.linspace(-np.pi, np.pi, 101, endpoint=True)
	if not call_from_other_example:
		print(xa)
	ya1 = np.sin(xa)
	ya2 = np.cos(xa)
	# Подготовка изображения
	#plt.axes(axisbg='r')
	#import matplotlib
	#matplotlib.set_axis_bgcolor('r')
	plt.title('Simple plot, two lines')
	plt.plot(xa, ya1)
	plt.plot(xa, ya2)
	# Вывод изображения на экран или в файл
	if to_file or call_from_other_example:
		plt.savefig('ex01.png')
	else:
		plt.show() 
	plt.close() # Close figure - очистка "холста"

def example_02():
	"""
	Единственный аргумент-массив
	"""
	pfi()

	a = np.array((1, 2, 3, 4, 5, 6) * 2)
	print(a)
	plt.plot(a)
	finish(2, 'a')
	b = a.reshape(3, 4)
	print(b)
	plt.plot(b)
	finish(2, 'b')

def example_03():
	"""
	Последовательность аргументы-массивы. аргументы-форматы
	"""
	pfi()

	a1 = rsm()
	a2 = rsm()
	# Два массива + формат x 2
	plt.plot(range(a1.size), a1, 'o', range(a2.size), a2, '+')
	finish(3, 'a')
	# Один массив + формат x 3
	plt.plot(rsm(21), 'o', rsm(21), '+', rsm(21), '*')
	finish(3, 'b')

def example_04():
	"""
	Формат и цвет линии или маркера
	"""
	pfi()

	formats = ('Dr-', 'g--', 'b-.', 'k:', 'c.', 'm|', 'o', 'v', '1')
	i = 0
	for fmt in formats:
		plt.plot(sca(offset=i), np.arange(0, 11), fmt, linewidth=8, markersize=16, alpha=0.5)
		i += 1
	finish(4, 'a')
	formats = ('s', 'p', '*', '1', 'h', '+', 'x', 'D', 'd')
	i = 0
	for fmt in formats:
		plt.plot(sca(offset=i), np.arange(0, 11), fmt, markersize=16)
		i += 1
	finish(4, 'b')

def example_05():
	"""
	Функция figure()
	"""
	pfi()

	pla()
	finish(5, 'a')
	plt.figure(num='Modified figure', figsize=(6, 9), dpi=75, facecolor='#ffcc66')
	plt.xlim(-6, 6)
	plt.ylim(-1.5, 1.5)
	plt.xticks(np.linspace(-6, 6, 13, endpoint=True))
	plt.yticks(np.linspace(-1.5, 1.5, 13, endpoint=True))
	pla()
	finish(5, 'b')
	# Третий график повторяет первый, после отображения графика
	# настройки сбрасываются
	pla()
	finish(5, 'c')

def example_06():
	"""
	Пояснение к графику, функция legend()
	"""
	pfi()

	xa = np.linspace(-np.pi, np.pi, 101, endpoint=True)
	plt.plot(xa, np.sin(xa))
	plt.plot(xa, np.cos(xa))
	plt.legend(('sin(x)', 'cos(x)'), loc='upper left')
	finish(6, 'a')
	plt.plot(xa, np.sin(xa), label='sin(x)')
	plt.plot(xa, np.cos(xa), label='cos(x)')
	plt.legend()
	finish(6, 'b')

def example_07():
	"""
	Координатная сетка
	"""
	pfi()

	pla()
	plt.grid(True, color='b', linewidth=2)
	finish(7, 'a')

def example_08():
	"""
	Заливка графика
	"""
	pfi()

	xa = np.linspace(-np.pi, np.pi, 101, endpoint=True)
	plt.fill(xa, np.cos(xa), 'y')
	finish(8)

def example_09():
	"""
	Заливка между двумя графиками
	"""
	pfi()

	xa = np.linspace(-np.pi, np.pi, 101, endpoint=True)
	plt.fill_between(xa, np.cos(xa), np.cos(xa) * 0.7, color='y')
	finish(9)

def example_10():
	"""
	Точечный график
	"""
	pfi()

	plt.scatter(rsm(), rsm(), c=rsm(), s=rsm() ** 2 * 16, alpha=0.7)
	finish(10)

def example_11():
	"""
	Столбчатая диаграмма, текст
	"""
	pfi()

	ax = lsm(n=11)
	ay = rsm(n=11)
	plt.bar(ax, ay, color='g')
	for x, y in zip(ax, ay):
		plt.text(x + 0.4, y + 0.1, '%.2f' % y, ha='center', va='bottom')
	finish(11)

def example_12():
	"""
	Трехмерный график
	"""
	pfi()

	from mpl_toolkits.mplot3d import Axes3D
	axes = Axes3D(plt.figure())
	r = np.arange(-4, 4, 0.25)
	ax, ay = np.meshgrid(r, r)
	print('ax =\n', ax, '\nay =\n', ay)
	az = np.sin(np.sqrt(ax**2 + ay**2))
	print('az shape =', az.shape) # => (32, 32)
	print('az dtype =', az.dtype) # => float64
	axes.plot_surface(ax, ay, az, rstride=1, cstride=1, cmap='cool')
	finish(12)

def example_13():
	"""
	Массив как цветовая карта
	"""
	pfi()

	r = np.arange(-4, 4, 0.25)
	ax, ay = np.meshgrid(r, r)
	az = np.sin(np.sqrt(ax**2 + ay**2))
	plt.imshow(az)
	plt.colorbar()
	finish(13)

def example_14():
	"""
	Массив как цветовая карта, интерполяция выключена
	"""
	pfi()

	r = np.arange(-4, 4, 0.25)
	ax, ay = np.meshgrid(r, r)
	az = np.sin(np.sqrt(ax**2 + ay**2))
	plt.imshow(az, interpolation='none')
	plt.colorbar()
	finish(14)

def example_15():
	"""
	Двумерный массив - несколько графиков
	"""
	pfi()

	a1d = np.linspace(0, 10, 11, endpoint=True)
	a2dx = np.array([a1d * 5, a1d * 5, a1d * 5, a1d * 5]).transpose()
	a2dy = np.array([a1d + 1, a1d + 2, a1d + 3, a1d + 4]).transpose()
	print(a2dx)
	print(a2dy)
	# Координаты X и Y
	plt.plot(a2dx, a2dy)
	finish(15, 'a')
	# Только координата Y
	plt.plot(a2dy)
	finish(15, 'b')

# Импорт субмодуля image
import matplotlib.image as mpimg

def example_16():
	"""
	Работа с растровыми изображениями
	"""
	pfi()

	example_01(call_from_other_example=True)
	image = mpimg.imread('ex01.png')
	print('image shape =', image.shape) # => (600, 800, 3)
	print('image dtype =', image.dtype) # => uint8
	# Младшая координата: [0] => R, [1] => G, [2] => B
	# 0 - минимум, 255 - максимум
	plt.imshow(image)
	finish(16)

	do_copy = True
	#do_copy = False

	if do_copy:
		img2 = np.copy(image)
	else:
		img2 = image
	img2[:,:,1:3] = 0 # G = 0, B = 0 => Red
	plt.imshow(img2)
	finish(16, 'r')

	if do_copy:
		img2 = np.copy(image)
	else:
		img2 = image
	img2[:,:,[0,2]] = 0 # R = 0, B = 0 => Green
	plt.imsave('ex01-green.png', img2)
	plt.imshow(img2)
	finish(16, 'g')

	if do_copy:
		img2 = np.copy(image)
	else:
		img2 = image
	img2[:,:,0:2] = 0 # R = 0, G = 0 => Blue
	for i in range(1, 200):
		# Белая линия шириной 4 пикселя
		img2[i + 20 : i + 24, i + 100, :] = 255
	plt.imshow(img2)
	finish(16, 'b')

def example_17():
	"""
	Массив как монохромное изображение
	"""
	pfi()

	r = np.arange(-4, 4, 0.25)
	ax, ay = np.meshgrid(r, r)
	az = np.sin(np.sqrt(ax**2 + ay**2))
	plt.imshow(az, cmap='gray')
	plt.colorbar()
	finish(17)

def example_18():
	"""
	Двумерный массив как аргумент
	"""
	pfi()

	xa = np.linspace(-np.pi, np.pi, 101, endpoint=True)
	ya1 = np.sin(xa)
	ya2 = np.cos(xa)
	plt.plot(xa, ya1)
	plt.plot(xa, ya2)
	finish(18, 'a')

	x2d = np.matrix((xa, xa)).T
	y2d = np.matrix((ya1, ya2)).T
	print(y2d)
	plt.plot(x2d, y2d)
	finish(18, 'b')

def example_19():
	"""
	Несколько графиков на одном изображении
	"""
	pfi()

	fig, axes = plt.subplots(2, 3) # 2 rows, 3 columns
	print(axes.__class__, axes.shape) # => <class 'numpy.ndarray'> (2, 3)
	plt.subplots_adjust(wspace=0.4, hspace=0.4) # wspace => width, hspace => height

	fig.suptitle('Several plots on single picture')

	xa = np.linspace(-np.pi, np.pi, 101, endpoint=True)
	ya = np.sin(xa)
	axes[0, 0].plot(ya, color='red',     label='r') ; axes[0, 0].set_title('Red')
	axes[0, 1].plot(ya, color='green',   label='g') ; axes[0, 1].set_title('Green')
	axes[0, 2].plot(ya, color='blue',    label='b') ; axes[0, 2].set_title('Blue')
	axes[1, 0].plot(ya, color='cyan',    label='c') ; axes[1, 0].set_title('Cyan')
	axes[1, 1].plot(ya, color='magenta', label='m') ; axes[1, 1].set_title('Magenta')
	axes[1, 2].plot(ya, color='black',   label='k') ; axes[1, 2].set_title('Black')
	fig.legend(prop={'size': 8})
	finish(19)

def example_20():
	"""
	Стили отображения
	"""
	pfi()

	xa = np.linspace(-np.pi, np.pi, 101, endpoint=True)
	ya1 = np.sin(xa)
	ya2 = np.cos(xa)

	#print(plt.style.available)
	print('Total', len(plt.style.available), 'stypes available\n')
	for style in plt.style.available:
		phdr('Style ' + style)
		plt.style.use(style)
		plt.title('Simple plot, style ' + style)
		plt.plot(xa, ya1)
		plt.plot(xa, ya2)
		if to_file:
			plt.savefig('ex20-' + style + '.png')
		else:
			plt.show() 
		plt.close()

if len(sys.argv) > 1 and not sys.argv[1] == 'slides':
	if sys.argv[1].isdigit() and int(sys.argv[1]) > 0:
		if len(sys.argv) > 2:
			to_file = False
		exec('example_%02d()' % int(sys.argv[1]))
	elif sys.argv[1][0].lower() == 'h':
		help(__name__)
	else:
		print(__doc__)
else:
	tuple(map(lambda c: exec(c + '()'),
		(f for f in sys._getframe().f_code.co_names
			if f.startswith('example_'))))
