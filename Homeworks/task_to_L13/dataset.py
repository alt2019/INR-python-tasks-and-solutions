#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from task6 import file2lists
from task6_module import run
# from t6_mod_2 import run


def add2lst(filename, t_max):
	"""
	:param filename: name of file in directory
	:type filename: str
	:param t_max: max value of time, computed in other function
	:type t_max: int
	"""
	cl, p1, p2 = file2lists(filename)
	for i in range(len(cl)):
		if (i % 3 == 2):
			cl[i] += (t_max + 1)
	for j in range(len(p1)):
		if (j%2 == 1):
			p1[j] += (t_max + 1)
	for k in range(len(p2)):
		if (k % 2 == 1):
			p2[k] += (t_max + 1)
	return cl, p1, p2


class Dataset(object):
	"""docstring for Dataset
	unifies information from all datafiles into 3 main lists, which \
	will be sent to the function run() of module task6_module
	"""
	def __init__(self, filename = None):
		# super(Dataset, self).__init__()
		super().__init__()
		self.filename = filename
		if self.filename == None:
			self.control_list, self.probe_1_list, self.probe_2_list = [], [], []
		else:
			self.control_list, self.probe_1_list, self.probe_2_list =\
			 file2lists(self.filename)
			# try:
				# self.control_list, self.probe_1_list, self.probe_2_list =\
				 # file2lists(self.filename)
			# except:
				# self.control_list, self.probe_1_list, self.probe_2_list = [], [], []
				# print("en error occured")

	@staticmethod
	def find_t_max(cl, p1, p2):
		""" 
		:return: max label of time in data
		"""
		t_max_c = max(cl[2::3])
		t_max_pr1 = max(p1[1::2])
		t_max_pr2 = max(p2[1::2])
		if t_max_c == t_max_pr1 and t_max_c == t_max_pr2:
			t_max = t_max_c		
		return t_max

	def __add__(self, other):
		if len(self.control_list) == 0:
			t_max = -1
		else:
			t_max = self.find_t_max(self.control_list, 
				self.probe_1_list, self.probe_2_list)
		cl1, p11, p21 = add2lst(other.filename, t_max)
		self.control_list += cl1
		self.probe_1_list += p11
		self.probe_2_list += p21
		return self

	def get(self):
		""" 
		:return: control_list, probe_1_list, probe_2_list
		"""
		return self.control_list, self.probe_1_list, self.probe_2_list


if __name__ == '__main__':
	print("000000000000000000000000000000000000000000000000000000000000000")
	import sys
	import os
	data = Dataset()
	dirname = sys.argv[1] if len(sys.argv) > 1 else None
	for filename in sorted(os.listdir(dirname or '.')):
		if filename.startswith('data') and filename.endswith('.txt'):
			data += Dataset(filename)
	# @run_modifier		
	run(data.get()[0], (data.get())[1], (data.get())[2])
	print("000000000000000000000000000000000000000000000000000000000000000")
