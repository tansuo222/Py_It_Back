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
		return []
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
		return []
	else:
		return valid_list
	pass

def pib_pi(pi):
	return _pin_pi_iteration(pi, 0, 0, pi.row_n, pi.col_n)
	#return _pin_pi_frsc_iteration(pi,0,0)
	pass

#先行后列遍历可能性（迭代）
def _pin_pi_frsc_iteration(pi,row_now,column_now):
	#当两边都不剩的时候，证明判断到了结尾
	if row_now == pi.row_n and column_now == pi.col_n:
		res = []
		res.append(pi)
		pi.print()
		print('------------------------------------')
		return res
	#当测试行的时候
	if row_now < pi.row_n:
		#获取当前行以及行头
		row = pi.getRow(row_now)
		header = pi.row_h[row_now]
		#得到所有可能的结果
		result = pib_row(row, header)
		#print(result)
		#如果没有合适的结果，返回空值
		if len(result) == 0:
			return []
		#否则对所有可能的选项进行迭代
		else:
			end_result = []
			#对于每一种情况
			for r in result:
				npi = pi.copy()
				npi.apply_row_with(r,row_now)
				t_result = _pin_pi_frsc_iteration(npi, row_now+1, column_now)
				end_result.extend(t_result)
			return end_result
	else:
		#获取当前列以及行头
		column = pi.getColumn(column_now)
		header = pi.col_h[column_now]
		#得到所有可能的结果
		result = pib_row(column, header)
		#print(result)
		#如果没有合适的结果，返回空值
		if len(result) == 0:
			return []
		#否则对所有可能的选项进行迭代
		else:
			end_result = []
			#对于每一种情况
			for r in result:
				npi = pi.copy()
				npi.apply_column_with(r,column_now)
				t_result = _pin_pi_frsc_iteration(npi, row_now, column_now+1)
				end_result.extend(t_result)
			return end_result
	pass


def _pin_pi_iteration(pi,row_now,column_now,row_all,column_all):
	#通过进行比例，判断下一个验证的是行还是列
	rate1 = row_now/row_all
	rate2 = column_now/column_all
	#当两边都不剩的时候，证明判断到了结尾
	if rate1 == 1 and rate2 == 1:
		if not pi.finish():
			return []
		res = []
		res.append(pi)
		pi.print()
		print('------------------------------------')
		return res
	#当测试行的时候
	if rate1 <= rate2:
		#获取当前行以及行头
		row = pi.getRow(row_now)
		header = pi.row_h[row_now]
		#得到所有可能的结果
		result = pib_row(row, header)
		#print(result)
		#如果没有合适的结果，返回空值
		if len(result) == 0:
			return []
		#否则对所有可能的选项进行迭代
		else:
			end_result = []
			#对于每一种情况
			for r in result:
				npi = pi.copy()
				npi.apply_row_with(r,row_now)
				t_result = _pin_pi_iteration(npi, row_now+1, column_now, row_all, column_all)
				end_result.extend(t_result)
			return end_result
	else:
		#获取当前列以及行头
		column = pi.getColumn(column_now)
		header = pi.col_h[column_now]
		#得到所有可能的结果
		result = pib_row(column, header)
		#print(result)
		#如果没有合适的结果，返回空值
		if len(result) == 0:
			return []
		#否则对所有可能的选项进行迭代
		else:
			end_result = []
			#对于每一种情况
			for r in result:
				npi = pi.copy()
				npi.apply_column_with(r,column_now)
				t_result = _pin_pi_iteration(npi, row_now, column_now+1, row_all, column_all)
				end_result.extend(t_result)
			return end_result
	pass


#对一整张图像进行运算，得到所有可能的结果
def main():
	row_headers = [[3],[5],[5],[3],[1]]
	column_headers = [[2],[4],[5],[4],[2]]
	npm = PixImg(5, 5,row_headers,column_headers)

	result = pib_pi(npm)

	#print(result)


	pass
	

if __name__ == "__main__":
	main()