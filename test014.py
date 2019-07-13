'''
实例014：分解质因数
题目 将一个整数分解质因数。例如：输入90,打印出90=2*3*3*5。
'''
prime_number = [2,3]
n = 0 #counting the number of prime number
k = 0 #counting the circulation number


for i in range(5,10001):
	for j in range(2,int(i**0.5)+1):
		k += 1
		if i%j == 0:
			k = 0
			break
		if k == int(i**0.5) - 1:
			prime_number.append(i)
			
				
number = int(input("Input a number:"))
a = number
zhiyinshu = []
for i in range(len(prime_number)):
	flag = True
	while flag:
		if number%prime_number[i] == 0:
			zhiyinshu.append(prime_number[i])
			number /= prime_number[i]
		else:
			flag = False
			
print("The number {} could be combined by :".format(str(a)))
result = ''

for i in zhiyinshu:
	result += str(i)+'*'
	
result = result[:-1]
print(result)
