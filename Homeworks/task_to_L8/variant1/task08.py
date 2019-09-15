#!/usr/bin/env python3
# -*- coding: utf-8 -*-


'''
The programm prints a report about equipment operation in the form:
Time = 11, Temperature = 12, Current = 13, Probe_1 = 14, Probe_2 = 15

:args: current directroy if no argumet, else 'directory'
:param: files named "data*.txt". Each file consists of lines with data \
from equipment operation.
'''


import os
import sys

from dataset import Dataset
from task6_module import run


data = Dataset()
dirname = sys.argv[1] if len(sys.argv) > 1 else None
for filename in sorted(os.listdir(dirname or '.')):
	if filename.startswith('data') and filename.endswith('.txt'):
		data += Dataset(filename)
run(*data.get())

# help('task08')
# help('dataset')
