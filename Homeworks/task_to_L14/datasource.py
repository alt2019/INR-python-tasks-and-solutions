#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from dataset import Dataset, file2lists
from task6_module import run, make_result, print_report


class Datasource(Dataset):
	"""docstring for Datasource"""
	def __init__(self, filename = None, min_current = None, max_temperature = None):
		super().__init__(filename)
		if filename is None:
			self.control_list, self.probe_1_list, self.probe_2_list = [], [], []
		self.min_current = min_current
		self.max_temperature = max_temperature

	@staticmethod
	def _get(get, cond):
		return make_result(*get(), condition = cond)

	def __add__(self, other):
		super().__add__(other)
		if self.min_current == None:
			self.min_current = other.min_current
		if self.max_temperature == None:
			self.max_temperature = other.max_temperature
		self.condition = {"current": ">" + str(self.min_current), 
			"temperature": "<" + str(self.max_temperature)}	
		return self	

	def __iter__(self):
		return zip(self._get(self.get, self.condition).keys(),
			list(values[0][0] 
				for values in self._get(self.get, self.condition).values()),
			list(values[0][1] 
				for values in self._get(self.get, self.condition).values()),
			list(values[1] 
				for values in self._get(self.get, self.condition).values()),
			list(values[2] 
				for values in self._get(self.get, self.condition).values()))


if __name__ == '__main__':
	import os
	import sys
	from task6_module import run
	data = Datasource()
	dirname = sys.argv[1] if len(sys.argv) > 1 else None
	for filename in sorted(os.listdir(dirname or '.')):	
		if filename.startswith('data') and filename.endswith('.txt'):	
			data += Datasource(filename, min_current=20, max_temperature=40)
	for timemark, temperature, current, probe_1, probe_2 in data:
		print('Time = {:3d}, Temperature = {:2d}, Current = {:2d}, Probe_1 = {:2d}, Probe_2 = {:2d}'.format(
			timemark, temperature, current, probe_1, probe_2))

	pass