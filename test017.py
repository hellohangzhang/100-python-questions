'''
实例017：字符串构成
题目 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
codes are not original
'''

string = input('Input a string:')
string_num = 0
digit_num = 0
space_num = 0
other_num = 0

for i in range(0,len(string)):
    if string[i].isalpha():
	    string_num += 1
    elif string[i].isdigit():
	    digit_num += 1
    elif string[i].isspace():
	    space_num += 1
    else:
	    other_num += 1

print('There are {} string.'.format(str(string_num)))
print('There are {} digit.'.format(str(digit_num)))
print('There are {} space.'.format(str(space_num)))
print('There are {} other character'.format(str(other_num)))
        
