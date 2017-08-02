#!/usr/bin/env
# -*- coding: utf-8 -*-
#
# 2017-08-01 20:02:28
# 
# Py_It_Back
# -a kit for the game "Paint it back" in python
# -author: dark-flame-maseter
# -mail: nerver0stop@163.com
#
# * the comments are Chinese
# 
# pib cornel

from itertools import combinations
from pixel_img import PixImg

#对单独的一行进行运算，产生所有可能的结果
def pib_row(row, nums):
	#生成总墨点总数
	anum = 0
	for num in nums:
		anum += num
	#生成已经存在的墨点总数
	dnum = 0
	for d in row:
		if d:
			dnum += 1
	#当墨点总数超出额定数量的时候，返回错误
	if anum + len(nums) - 1 > len(row) or dnum > anum:
		return [[],False]
	#正常情况，则枚举可能性
	random_list = []
	usable_pos = []
	for i in range(0,len(row)):
		if not row[i]:
			usable_pos.append(i)
	random_list = combinations(usable_pos, abs(anum-dnum))
	#对于每种可能性构造一个list
	result_list = []
	for chance in random_list:
		new_list = row[:]
		for c in chance:
			new_list[c] = True
		result_list.append(new_list)
	#对生成的列表进行合法性判断
	valid_list = []
	for res in result_list:
		#对于每一个数字进行判断（连续性）
		now = 0
		width = len(row)
		nums_t = nums[:]
		has_num = False
		while now < width:
			#如果这一位是空位
			if not res[now]:
				if has_num:
					if nums_t[0] != 0:
						break
					else:
						nums_t.pop(0)
						has_num = False
						if len(nums_t)==0:
							valid_list.append(res)
							break
			#如果不是空位
			else:
				if not has_num:
					has_num = True
					nums_t[0] -= 1
					if nums_t[0] == 0 and now == width-1 and len(nums_t) == 1:
						valid_list.append(res)
						break
				else:
					nums_t[0] -= 1
					if nums_t[0] == 0 and now == width-1 and len(nums_t) == 1:
						valid_list.append(res)
						break
			now += 1

	if len(valid_list) == 0:
		return [[],False]
	else:
		return [valid_list,True]
	pass


def main():
	npm = PixImg(5, 10)
	print(npm.getRow(0))
	print(npm.getColumn(1))
	print(npm.data)


	pass
	

if __name__ == "__main__":
	main()