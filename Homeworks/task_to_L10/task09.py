#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

from datasource import Datasource

def work():
	data = Datasource()
	dirname = sys.argv[1] if len(sys.argv) > 1 else None
	min_current = int(sys.argv[2]) if len(sys.argv) > 2 else 30
	max_temperature = int(sys.argv[3]) if len(sys.argv) > 3 else 40
	for filename in sorted(os.listdir(dirname or '.')):
		if filename.startswith('data') and filename.endswith('.txt'):
			# try:
				# data += Datasource(filename, min_current=min_current, max_temperature=max_temperature)
			# except:
				# print("Skip broken file", filename, file=sys.stderr)
				# continue
			data += Datasource(filename, min_current=min_current, max_temperature=max_temperature)
	for timemark, temperature, current, probe_1, probe_2 in data:
		print('Time = {:3d}, Temperature = {:2d}, Current = {:2d}, Probe_1 = {:2d}, Probe_2 = {:2d}'.format(
		timemark, temperature, current, probe_1, probe_2))


if __name__ == '__main__':
	work()