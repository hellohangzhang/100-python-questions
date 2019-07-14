'''
实例019：完数
题目 一个数如果恰好等于它的因子之和，这个数就称为"完数"。
例如6=1＋2＋3.编程找出1000以内的所有完数。
'''

'''
def seek_yinshu(number):
	yinshu = []
	for i in range(1,number):
		if number%i == 0:
			yinshu.append(i)
	yinshu_set = set(yinshu)
	yinshu = list(yinshu_set)
	return yinshu
'''

def seek_yinshu(number):
	yinshu = set()
	for i in range(1,number):
		if number%i == 0:
			yinshu.add(i)
	return yinshu


for i in range(2,1001):
	yinshu = seek_yinshu(i)
	sum_yinshu = sum(yinshu)
	if i == sum_yinshu:
		print(i)
		


'''
for i in range(2,1001):
	yinshu = seek_yinshu(i)
	sum = 0
	for j in range(len(yinshu)):
		sum += yinshu[j]
	
	if sum == i:
		print(i)
		
'''
