'''
实例018：复读机相加
题目 求s=a+aa+aaa+aaaa+aa…a的值，其中a是一个数字。
例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
'''


num1 = input('Input a number in [1,10):')
num2 = input('How many times do you want to count?(<10)')

list = []
a = ''
for i in range(int(num2)):
	a += str(num1)
	list.append(a)

sum = 0
for i in list:
	sum += int(i)
	

result = ''
for i in list:
	result += i+'+'
result = result[:-1]

print('The sum of {0} is {1}.'.format(result,str(sum)))
