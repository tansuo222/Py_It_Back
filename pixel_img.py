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
	def __init__(self,row,column):
		self.row_n = row
		self.col_n = column
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