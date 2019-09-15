#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def example_01():
	"""
	Создание объекта типов list и tuple
	"""
	print('\n*** Example 01 ***')
	m = [ 'abcdef', 14, 27.12, [ 1, 2 ] ] # Список, скобки [ ]
	c = ( 'abcdef', 14, 27.12, [ 1, 2 ] ) # Кортеж, скобки ( )
	print(m) # => ['abcdef', 14, 27.12, [1, 2]]
	print(c) # => ('abcdef', 14, 27.12, [1, 2])

	m1 = list(('abcdef', 14, 27.12, [ 1, 2 ]))  ; print(m1)
	c1 = tuple(['abcdef', 14, 27.12, [ 1, 2 ]]) ; print(c1)
	print(range(1, 5)) # => range(1, 5) - специальный объект-последовательность
	m2 = list(range(1, 5))  ; print(m2) # => [1, 2, 3, 4]
	c2 = tuple(range(1, 5)) ; print(c2) # => (1, 2, 3, 4)

def example_02():
	"""
	Создание объекта, строки и байты
	"""
	print('\n*** Example 02 ***')
	ms = list('abcdef')   ; print(ms) # => ['a', 'b', 'c', 'd', 'e', 'f']
	cs = tuple('abcdef')  ; print(cs) # => ('a', 'b', 'c', 'd', 'e', 'f')
	mb = list(b'abcdef')  ; print(mb) # => [97, 98, 99, 100, 101, 102]
	cb = tuple(b'abcdef') ; print(cb) # => (97, 98, 99, 100, 101, 102)
	bm = bytes(mb)        ; print(bm) # => b'abcdef'
	am = bytearray(mb)    ; print(am) # => bytearray(b'abcdef')
	bc = bytes(cb)        ; print(bc) # => b'abcdef'
	ac = bytearray(cb)    ; print(ac) # => bytearray(b'abcdef')
	sm = str(ms)          ; print(sm) # => ['a', 'b', 'c', 'd', 'e', 'f']
	sc = str(cs)          ; print(sc) # => ('a', 'b', 'c', 'd', 'e', 'f')
	print(sm[:3], 'of', sm.__class__) # => ['a of <class 'str'>
	print(sc[:3], 'of', sc.__class__) # => ('a of <class 'str'>

def example_03():
	"""
	Операторы [ ], + и *
	"""
	print('\n*** Example 03 ***')
	m = [ 'abcdef', 14, 27.12, [ 1, 2 ] ]
	c = ( 'abcdef', 14, 27.12, [ 1, 2 ] )
	m2 = m + m        ; print(m2) # => ['abcdef', 14, 27.12, [1, 2], 'abcdef', 14, 27.12, [1, 2]]
	#m3 = m + c       ; print(m3) # Ошибка
	m4 = m + list(c)  ; print(m4) # => ['abcdef', 14, 27.12, [1, 2], 'abcdef', 14, 27.12, [1, 2]]
	c2 = c + tuple(m) ; print(c2) # => ('abcdef', 14, 27.12, [1, 2], 'abcdef', 14, 27.12, [1, 2])
	c3 = c[:2] * 3    ; print(c3) # => ('abcdef', 14, 'abcdef', 14, 'abcdef', 14)

def example_04():
	"""
	Создание объекта используя фрагмент
	"""
	print('\n*** Example 04 ***')
	m = ['abcdef', 14, 27.12, [ 1, 2 ]]
	c = ('abcdef', 14, 27.12, [ 1, 2 ])  
	m2 = m[:]   ; print(m2) # => ['abcdef', 14, 27.12, [1, 2]]
	c2 = c[:]   ; print(c2) # => ('abcdef', 14, 27.12, [1, 2])
	m3 = m[1:3] ; print(m3) # => [14, 27.12]
	c3 = c[1:3] ; print(c3) # => (14, 27.12)

def example_05():
	"""
	Переменная как элемент списка
	"""
	print('\n*** Example 05 ***')
	a = 18
	b = 'b_string'
	c = [ 1, 2 ]
	y = [ 'abcdef', a, b, c ]
	print('Original y content', y) # => [ 'abcdef', 18, 'b_string', [1, 2] ]
	a = 33
	b = 'b_modified'
	c[1] = 433
	c = [ 8, 9 ]
	print('Modified y content', y) # => [ 'abcdef', 18, 'b_string', [1, 433] ]

def example_06():
	print('\n*** Example 06 ***')
	"""
	Переменная как элемент кортежа
	"""
	a = 18
	b = 'b_string'
	c = [ 1, 2 ]
	y = ( 'abcdef', a, b, c )
	print('Original y content', y) # => [ 'abcdef', 18, 'b_string', [1, 2] ]
	a = 33
	b = 'b_modified'
	c[1] = 433
	c = [ 8, 9 ]
	print('Modified y content', y) # => [ 'abcdef', 18, 'b_string', [1, 433] ]

def example_07():
	"""
	Операции изменяющие список
	"""
	print('\n*** Example 07 ***')
	m = [ 'abcdef', 14, 27.12, [ 1, 2 ] ]
	m[2] = 433  ; print(m) # => ['abcdef', 14, 433, [1, 2]]
	m[1:3] = [ 1.1, 3.3 ] ; print(m) # => ['abcdef', 1.1, 3.3, [1, 2]]
	del m[1:3]  ; print(m) # => ['abcdef', [1, 2]]
	m[1:3] = [] ; print(m) # => ['abcdef']
	m = m + list((1, 2, 3)) ; print(m) # => ['abcdef', 1, 2, 3]
	m[2] = []   ; print(m) # => ['abcdef', 1, [], 3]
	del m[2]    ; print(m) # => ['abcdef', 1, 3]
	m[2:3] = [] ; print(m) # => ['abcdef', 1]

def example_08():
	"""
	Удаление всех элементов списка
	"""
	print('\n*** Example 08 ***')
	m = [ 'abcdef', 14, 27.12, [ 1, 2 ] ]
	m.clear()
	print(m) # => []
	m = [ 'abcdef', 14, 27.12, [ 1, 2 ] ]
	del m[:]
	print(m) # => []

def example_09():
	"""
	Извлечение элемента из списка
	"""
	print('\n*** Example 09 ***')
	m = [ 0, 1, 2, 3, 4, 5, 6, 7 ]
	e = m.pop()   ; print(e, m) # => 7 [0, 1, 2, 3, 4, 5, 6]
	e = m.pop(3)  ; print(e, m) # => 3 [0, 1, 2, 4, 5, 6]
	e = m.pop(-3) ; print(e, m) # => 4 [0, 1, 2, 5, 6]

def example_10():
	"""
	Добавление элементов в список
	"""
	print('\n*** Example 10 ***')
	i = 3
	m = [ 0, 1, 2, 3 ]
	m.append('New')     ; print(m) # => [0, 1, 2, 3, 'New']
	m.extend('New')     ; print(m) # => [0, 1, 2, 3, 'New', 'N', 'e', 'w']
	m.insert(i, 'at_i') ; print(m) # => [0, 1, 2, 'at_i', 3, 'New', 'N', 'e', 'w']
	#m[99] = 433        ; print(m) # Ошибка
	m.insert(99, 433)   ; print(m) # => [0, 1, 2, 'at_i', 3, 'New', 'N', 'e', 'w', 433]

def example_11():
	"""
	Класс deque, расширение класса list
	"""
	print('\n*** Example 11 ***')
	from collections import deque
	m = deque([ 0, 1, 2, 3 ])
	m.appendleft(101) ; print(m) # => deque([101, 0, 1, 2, 3])
	m.extendleft([102, 103]) ; print(m) # => deque([103, 102, 101, 0, 1, 2, 3])
	e = m.popleft() ; print(e, m) # => 103 deque([102, 101, 0, 1, 2, 3])
	e = m.pop() ; print(e, m)     # => 3 deque([102, 101, 0, 1, 2])
	m.append(201) ; print(m)        # => deque([102, 101, 0, 1, 2, 201])
	m.extend([202, 203]) ; print(m) # => deque([102, 101, 0, 1, 2, 201, 202, 203])

def example_12():
	"""
	Поиск и удаление найденного
	"""
	print('\n*** Example 12 ***')
	m = [ 0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0 ]
	nx = m.index(3)    ; print(nx) # => 3
	nx = m.index(3, 4) ; print(nx) # => 7
	m.remove(3) ; print(m) # => [0, 1, 2, 4, 5, 4, 3, 2, 1, 0]

def example_13():
	"""
	Оператор in
	"""
	print('\n*** Example 13 ***')
	m = [ 'abcdef', 14, 27.12, [ 1, 2 ] ]
	c = ( 'abcdef', 14, 27.12, [ 1, 2 ] )  
	print('[ 1, 2 ] in m', [ 1, 2 ] in m) # => True
	print('27.13 in m', 27.13 in m)       # => False
	print("'abcdef' in c", 'abcdef' in c) # => True
	print("'abcde'  in c", 'abcde'  in c) # => False

def example_14():
	"""
	Равенство и идентичность, один список
	"""
	print('\n*** Example 14 ***')
	m = [ 1, 'two', 3.3 ]
	n = m
	n[1] = 122
	print('m =', m)
	print('n =', n)
	print('n == m', n == m, 'n is m', n is m) # => True, True

def example_15():
	"""
	Равенство и идентичность, два списка
	"""
	print('\n*** Example 15 ***')
	m = [ 1, 'two', 3.3 ]
	n = [ 1, 'two', 3.3 ]
	print('m =', m)
	print('n =', n)
	print('n == m', n == m, 'n is m', n is m) # => True, False

def example_16():
	"""
	Равенство и идентичность, два кортежа
	"""
	print('\n*** Example 16 ***')
	m = ( 1, 'two', 3.3 )
	n = ( 1, 'two', 3.3 )
	print('m =', m)
	print('n =', n)
	print('n == m', n == m, 'n is m', n is m) # => True, True

def example_17():
	"""
	Сортировка и инверсия
	"""
	print('\n*** Example 17 ***')
	m = [ 3, 1, 7, 3.5, 11, 2.7, 0 ]
	n = sorted(m)
	print('m =', m)
	print('n =', n)
	n = reversed(m)
	print('m =', m)
	print('n =', n)
	print('n =', list(n), '-- converted to list')
	m.sort()    ; print('m =', m, '-- after m.sort()')
	m.reverse() ; print('m =', m, '-- after m.reverse()')

def example_18():
	"""
	Создание объекта типов dict и set
	"""
	print('\n*** Example 18 ***')
	d = { 'name': 'abcd', 'f1': 14, 5: 27.12, 'pair': [ 1, 2 ] }
	#d = { 'name': 'abcd', 'f1': 14, 5: 27.12, [ 1, 2 ]: 'pair' } # Ошибка
	s = { 'abcd', 14, 27.12, ( 1, 2 ) }
	#s = { 'abcd', 14, 27.12, [ 1, 2 ] } # Ошибка
	print('d =', d)
	print('s =', s)
	d_empty = {}    ; print('d_empty =', d_empty)
	s_empty = set() ; print('s_empty =', s_empty)
	d2 = dict(d) ; print('d2 =', d2)
	d3 = dict(name='abcd', f1=14, digit_5=27.12, pair=[ 1, 2 ]) ; print('d3 =', d3)
	s2 = set(s) ; print('s2 =', s2)
	s3 = set(['abcd', 14, 27.12, ( 1, 2 )]) ; print('s3 =', s3)

def example_19():
	"""
	Доступ к элементу
	"""
	print('\n*** Example 19 ***')
	new_value = 'zzz'
	new_val2 = 'zz2'
	d = { 'name': 'abcd', 'f1': 14, 5: 27.12, 'pair': [ 1, 2 ] }
	print("d =", d)
	value = d['f1']     ; print("d['f1'] =", value)
	d['f1'] = new_value ; print("d['f1'] =", d['f1'], '-- new_value assigned')
	d['f2'] = new_val2  ; print("d['f2'] =", d['f2'], '-- new_val2 assigned')
	#value =  d['ab'] # Ошибка: KeyError: 'ab'
	print("d.get('ab')", d.get('ab'))           # => None
	print("d.get('ab', '?')", d.get('ab', '?')) # => '?'
	del d['f1']  ; print("d =", d, "-- after del d['f1']")

def example_20():
	"""
	Элемент множества и ключ словаря
	"""
	print('\n*** Example 20 ***')
	s = { 'abcd', 14, 27.12, ( 1, 2 ) }  
	print("s =", s)
	print("14 in s =", 14 in s) # => True
	#s.remove(15) # Ошибка
	s.remove(14)
	print("s =", s, '-- after s.remove(14)')
	s.discard(27.13) # Ошибки нет
	s.discard(27.12)
	print("s =", s, '-- after s.discard(27.12)')
	d = { 'name': 'abcd', 'f1': 14, 5: 27.12, 'pair': [ 1, 2 ] }  
	print("d =", d)
	print("'f1' in d =", 'f1' in d) # => True

def example_21():
	"""
	Методы словарей
	"""
	print('\n*** Example 21 ***')
	d = { 'name': 'abcd', 'f1': 14, 5: 27.12, 'pair': [ 1, 2 ] }
	print("d =", d)
	print("d.keys()   =", d.keys())
	print("d.values() =", d.values())
	print("d.items()  =", d.items())
	d.update(color='Green', count=27)
	print("d =", d, '-- after d.update()')
	e = d.pop('name')    ; print("e =", e, "-- after d.pop('name')")
	#d.pop('ab') # Ошибка
	e = d.pop('ab', '?') ; print("e =", e, "-- after d.d.pop('ab', '?')")
	print("d =", d, '-- after all')

def example_22():
	"""
	Метод clear
	"""
	print('\n*** Example 22 ***')
	d = { 'name': 'abcd', 'f1': 14, 5: 27.12, 'pair': [ 1, 2 ] }
	s = { 'abcd', 14, 27.12, ( 1, 2 ) }
	d.clear() ; print("d =", d)
	s.clear() ; print("s =", s)

def example_23():
	"""
	Теоретико-множественные операции
	"""
	print('\n*** Example 23 ***')
	s1 = { 1, 2, 3, 10, 20, 30 }
	print("s1 =", s1)
	s2 = { 1, 2, 3, 100, 200, 300 }
	print("s2 =", s2)
	s3 = { 100, 200 }
	print("s3 =", s3)
	print('s1 & s2', s1 & s2) # => {1, 2, 3}
	print('s1 | s2', s1 | s2) # => {1, 2, 3, 100, 200, 10, 300, 20, 30}
	print('s1 - s2', s1 - s2) # => {10, 20, 30}
	print('s1 ^ s2', s1 ^ s2) # => {100, 200, 10, 300, 20, 30}
	print('s1 > s2', s1 > s2) # => False
	print('s3 < s2', s3 < s2) # => True

	d = { 'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5 }
	print("d =", d)
	blacklist = { 'b', 'c', 'd' }
	print("blacklist =", blacklist)
	allowed_keys = d.keys() - blacklist
	print('allowed_keys =', allowed_keys) # => {'e', 'a'}

def example_24():
	"""
	Теоретико-множественные методы
	"""
	print('\n*** Example 24 ***')
	s = { 'abcd', 14, 27.12, ( 1, 2 ) }
	print(s.intersection([27.12, 'abcd', 816])) # => {'abcd', 27.12}
	print(s.union('abc')) # => {(1, 2), 'c', 14, 'a', 'b', 'abcd', 27.12}
	print(s.difference((14, 'abcd')))           # => {(1, 2), 27.12}
	print(s.symmetric_difference((14, 'New')))  # => {(1, 2), 'New', 'abcd', 27.12}
	print(s.issuperset([27.12, 'abcd']))        # => True
	print(s.issubset((101, 'New')))             # => False

def example_25():
	"""
	Тип frozenset
	"""
	print('\n*** Example 25 ***')
	f = frozenset(('abcd', 18, 27.12, ( 3, 4 )))
	print('f = ', f) 
	#f.add('New')        # Ошибка, нельзя добавлять элементы
	g = set('abc')
	g.add('New')
	s = { 1, 'two', f } ; print('s = ', s)
	#t = { 1, 'two', g } # Ошибка: unhashable type: 'set'
	e = { f: 18 }        # frozenset может быть ключом в словаре
	#x = { g: 18 }       # Ошибка: unhashable type: 'set'

# Comment-out tests you like to skip with '#' character

# example_15() ; exit() # Uncomment this line to run single test
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
example_17()
example_18()
example_19()
example_20()
example_21()
example_22()
example_23()
example_24()
example_25()
