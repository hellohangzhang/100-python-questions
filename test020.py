'''
实例020：高空抛物
题目 一球从100米高度自由落下，每次落地后反跳回原高度的一半；
再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
'''


total_range = 100
original_height = 100
current_height = original_height/2

for i in range(2,11):
	
	total_range += 2 * current_height
	current_height /= 2
	
	
print("At the 10th falling, the total range is {}.".format(total_range))
print("The 10th rebonce height is {}.".format(current_height))
