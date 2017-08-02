#!/usr/bin/env
# -*- coding: utf-8 -*-
#
# 2017-08-02 13:45:19
# 
# PixImg -- data type

from random import randint

class PixImg:

	def getRow(self,row_num):
		tl = self.data[row_num][:]
		return tl
		pass
	def getColumn(self,column_num):
		tl = []
		for i in range(0,self.row_n):
			tl.append(self.data[i][column_num])
		return tl
		pass

	#初始化
	def __init__(self,row,column,row_headers,column_headers):
		self.row_n = row
		self.col_n = column
		self.row_h = row_headers
		self.col_h = column_headers
		self.data = []
		for i in range(0,self.row_n):
			nl = []
			for j in range(0,self.col_n):
				nl.append(False)
			self.data.append(nl)
		#print(self.data)
		pass

	#把这个pi随机化（用于测试)
	def randomize(self):
		for x in range(0,self.row_n):
			for y in range(0,self.col_n):
				end =randint(0, 1)
				#print(end)
				if end == 0:
					self.data[x][y] = False
				else:
					self.data[x][y] = True
	pass

	def copy(self):
		np = PixImg(self.row_n, self.col_n, self.row_h, self.col_h)
		for i in range(0,self.row_n):
			np.data[i] = self.data[i][:]
		return np
		pass

	def apply_row_with(self,data_i,num):
		for i in range(0,len(data_i)):
			self.data[num][i] = data_i[i]
		pass

	def apply_column_with(self,data_i,num):
		for i in range(0,len(data_i)):
			self.data[i][num] = data_i[i]
		pass

	def print(self):
		for i in range(0,self.row_n):
			print(self.data[i])

	def _get_row_header_count(self,num):
		end = 0
		for i in self.row_h[num]:
			end += i
		return end

	def _get_column_header_count(self,num):
		end = 0
		for i in self.col_h[num]:
			end += i
		return end

	def _get_row_count(self,num):
		end = 0
		for i in range(0,len(self.data[0])):
			if self.data[num][i]:
				end += 1
		return end

	def _get_column_count(self,num):
		end = 0
		for i in range(0,len(self.data)):
			if self.data[i][num]:
				end += 1
		return end

	def test(self):
		print(self._get_row_count(2))
		print(self._get_column_count(2))
		print(self._get_row_header_count(1))
		print(self._get_column_header_count(4))
		pass

	def finish(self):
		for i in range(0,self.row_n):
			if self._get_row_count(i) != self._get_row_header_count(i):
				return False
		for j in range(0,self.col_n):
			if self._get_column_count(j) != self._get_column_header_count(j):
				return False
		return True

def main():
	row_headers = [[3],[5],[5],[3],[1]]
	column_headers = [[2],[4],[5],[4],[2]]
	npm = PixImg(5, 5,row_headers,column_headers)
	cpm = npm.copy()
	cpm.apply_row_with([False,True,True,True,False], 0)
	cpm.apply_row_with([True,True,True,True,True], 1)
	cpm.apply_row_with([True,True,True,True,True], 2)
	cpm.apply_row_with([False,True,True,True,False], 3)
	cpm.apply_row_with([False,False,True,False,False], 4)
	cpm.print()
	print('-------------------------------------')
	npm.print()

	print(cpm.finish())

	pass

if __name__ == "__main__":
	main()