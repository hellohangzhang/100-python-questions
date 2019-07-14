'''
1.输出如下格式的当天日期：2019-07-14
2.输入指定格式的日期：2333-02-03
3.输出指定格式的当天日期；14/07/2019
4.在指定日期基础上增加指定的年数(22)并得到指定格式的日期：1133-02-03

'''


import datetime
print(datetime.date.today())
print(datetime.date(2333,2,3))
print(datetime.date.today().strftime('%d/%m/%Y'))
print(datetime.date(1111,2,3).replace(year=1133))
day = datetime.date.today()
new_day = day.replace(year=day.year+22)
print(new_day)

