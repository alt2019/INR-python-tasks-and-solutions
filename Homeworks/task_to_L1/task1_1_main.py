#!/usr/bin/env python3

"""
~~~Answers:~~~
-Сколько интерпретаторов Питона Вы видите на сервере, какие у них версии ?
Как Вы это определили ?:
	> find /usr/bin/ -name python*
	/usr/bin/python3.6
	/usr/bin/python2.7

->2 interpretators

-Определите версию Питона 3 с которой Вы будете работать:
	> python3 --version
	Python 3.6.6

-Каким редактором Вы пользовались для написания программы ?
->Sublime Text 3
"""

import task1_2 as t2

if __name__ == '__main__':
	print(__doc__)
	t2.show()
