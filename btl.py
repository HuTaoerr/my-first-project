import time
from random import randrange, randint
import string
from datetime import datetime
from itertools import combinations
from random import sample


# try:
#     x = float(input('请输入被除数'))
#     y = float(input('请输入除数'))
#     z = x/y
# except ZeroDivisionError:
#     print('')
# except ValueError:
#     print('')
# except NameError:
#     print('')
# else:
#     print(z)
#
#



# filename = input('请输入一个文件名：')
#
# try:
#     fp = open(filename)
#     try:
#         x = fp.read()
#         print(int(x) + 5)
#     except:
#         print('文件内容格式不正确')
#     finally:
#         fp.close()
# except:
#     print("文件不存在")







# while True:
#     x = input('Please input:')
#     try:
#         x = int(x)
#     except Exception as e:
#         print('Error.')
#     else:
#         print('You are input {0}'.format(x))
#         break






# while True:
#     x = input('Please input:')
#     try:
#         x = int(x)
#         print('You are input {0}'.format(x))
#         break
#     except Exception as e:
#         print('Error.{0}'.format(e))








# from docx import Document
# doc = Document('乱七八糟.docx')
#
# contents = ''.join((p.text for p in doc.paragraphs))
# words = []
# for index, ch in enumerate(contents[:-2]):
#     if ch == contents[index + 1] or ch == contents[index + 2]:
#         word = contents[index:index + 3]
#         if word not in words:
#             words.append(word)
#             print(word)






# from openpyxl import Workbook
#
#
# def main(txtFileName):
#     new_XlsxFileName = txtFileName[:-3] + 'xlsx'
#     wb = Workbook()
#     ws = wb.worksheets[0]
#     with open(txtFileName) as fp:
#         for line in fp:
#             line = line.strip().split(', ')
#             ws.append(line)
#     wb.save(new_XlsxFileName)
#
#
# main('test.txt')





# import openpyxl
# from openpyxl import Workbook
#
# fn = r'f:\test.xlsx'
# wb = Workbook()
# ws = wb.create_sheet(title='hello world')
# ws['A1'] = '这是第一个单元格'
# ws['B1'] = 3.1415926
# wb.save(fn)
#
# wb = openpyxl.load_workbook(fn)
# ws = wb.worksheets[1]
# print(ws['A1'].value)
#
# ws.append([1, 2, 3, 4, 5])
# ws.merge_cells('F2:F3')
# ws['F2'] = "=sum(A2:E2)"
# for r in range(10,15):
#     for c in range(3,8):
#         ws.cell(row=r, column=c, value=r*c)
# wb.save(fn)


# import struct
#
# n = 1300000000
# x = 96.45
# b = True
# s = 'a1@中国'
# # 序列化，i表示整数，f表示实数，？表示逻辑值
#  # 得到的字节串sn长度为9，其中整数和实数各占4个字节，逻辑值占1个字节
#
# sn = struct.pack('if? ', n, x, b)
# with open('sample_struct.dat', 'wb') as f:
#     f.write(sn)
# # 字符串方法encode()默认使用UTF8编码
# # 字符串s需要编码为字节串（长度为9）再写入文件
#     f.write(s.encode())
#
#
# with open('sample_struct.dat', 'rb') as f:
#     sn = f.read(9)
#     n, x, b1 = struct.unpack('if? ', sn)  # 使用指定格式反序列化
#     print('n=', n, 'x=', x, 'b1=', b1)
#     s = f.read(9).decode()
#     print('s=', s)


import pickle
# i = 13000000
# a = 99.056
# s = '中国人民123abc'
# lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# tu = (-5, 10, 8)
# coll = {4, 5, 6}
# dic = {'a':'apple', 'b':'banana', 'g':'grape', 'o':'orange'}
#
# data = (i, a, s, lst, tu, coll, dic)
#
# with open('sample_pickle.dat', 'wb') as f:
#     try:
#         pickle.dump(len(data), f)
#         for item in data:
#             pickle.dump(item, f)
#     except:
#         print('写文件异常')


# with open('sample_pickle.dat', 'rb') as f:
#     n = pickle.load(f)
#     print(n)
#     for i in range(n):
#         x = pickle.load(f)
#         print(x)


# fp = open('Luan.txt', 'x')
# fp.close()

# s = 'Hello world\n文本文件的读取方法\n文本文件的写入方法\n'
# with open('sample.txt', 'w') as fp:
#     fp.write(s)
# with open('sample.txt') as fp:
#     print(fp.read())

# with open('sample.txt') as fp:
#     for line in fp:
#         print(line)
# with open('sample.txt') as fp:
#     print(fp.readlines())

# s = '1\n2\n3\n8\n5\n0\n8\n6'
# with open('data.txt','w') as fp:
#     fp.write(s)
# with open('data.txt','r') as fp:
#     data = fp.readlines()
# data = [int(item) for item in data]
# data.sort(reverse=True)
# data = [str(item)+'\n' for item in data]
# with open('data_desc.txt', 'w') as fp:
#     fp.writelines(data)

# s = '基本思路：虽然不建议使用readlines\n()一次性读取全部内容，但也要具体问题具体分析。以本例问题为例,\n只有把所有数据都读取之后才能进行排序。另外，内置函数int()在把字符串转换为整数时，会自动忽略字符串尾部的换行符\n'
# with open('sample.txt','w') as fp:
#     fp.write(s)
# with open('sample.txt') as fp:
#     result = [0,'']
#     for line in fp:
#         t = len(line)
#         if t > result[0]:
#             result = [t, line]
# print(result)


#
# class Root:
#     __total = 0
#
#     def __init__(self, v):  # 构造方法，特殊方法
#         self.__value = v
#         Root.__total += 1
#
#     def show(self):  # 普通实例方法，以self作为第一个参数
#         print('self.__value:', self.__value)
#         print('Root.__total:', Root.__total)
#
#     @classmethod  # 修饰器，声明类方法
#     def classShowTotal(cls):  # 类方法，一般以cls作为第一个参数
#         print(cls.__total)

#     @staticmethod  # 修饰器，声明静态方法
#     def staticShowTotal():  # 静态方法，可以没有参数
#         print(Root.__total)
#
# r = Root(3)
# r.classShowTotal()  # 通过对象来调用类方法
# r.staticShowTotal()  # 通过对象来调用静态方法
# rr = Root(5)
# Root.classShowTotal()  # 通过类名调用类方法
# Root.staticShowTotal()  # 通过类名调用静态方法
# # Root.show()  # 试图通过类名直接调用实例方法，失败
# #
# Root.show(rr)  # 可以通过这种方法来调用方法并访问实例成员
# # self.__value: 3
# # Root.__total: 2


# class Test:
#     def __init__(self, value):
#         self.__value = value
#     @property
#     def value(self):
#         return self.__value
#
# t = Test(3)
# print(t.value)


# class Test:
#     def __int__(self, value=0):
#         self.__value = value
#
#     def setValue(self, value):
#         self.__value = value
#
#     def show(self):
#         print(self.__value)
# t = Test()


# class Car(object):
#     def showInfo(self):
#         print("This is a car")
#
# car = Car()
# car.showInfo()


# 编写函数，接收圆的半径作为参数，返回圆的面积
# import math
# def circle(r):
#     pi = math.pi
#     s = round((pi * r **2),2)
#     print('circle are is:',s)
# circle(5)


# user_birthday = '2023/10/09'
# # 计算一个人的生日
# def birthday():
#     global user_birthday
#     now_time = datetime.now()
#     today_time = now_time.strftime('%Y/%m/%d')
#     print('Today is:', today_time)
#     if user_birthday == today_time:
#         print('Happy birthday to you!')
#
# birthday()


# def binarySeach(lst, value):
#     start = 0
#     end = len(lst)
#     while start < end :
#         print(start, end)
#         middle = (start + end)//2
#         if (middle + 1) < end:
#             if value == lst[middle]:
#                 return middle
#             elif value > lst[middle]:
#                 start = middle
#             elif value < lst[middle]:
#                 end = middle - 1
#         else:
#             return False
#     return False
#
# lst = [randint(1, 50) for i in range(20)]
# lst.sort()
# print(lst)
# result = binarySeach(lst, 17)
# if result != False:
#     print('Success, its position is:', result)
# else:
#     print('Fail. Not exist.')


# def selectSort(lst, reverse=False):
#      lenght = len(lst)
#      for i in range(0, lenght):
#          m = i
#          for j in range(i+1, lenght):
#              exp = 'lst[m] < lst[j]'
#              if reverse:
#                 exp = 'lst[m] > lst[j]'
#              if eval(exp):
#                  m = j
#          if m != i:
#              lst[m], lst[i] = lst[i], lst[m]
# lst = [randint(1, 100) for i in range(20)]
# print('排序前: \n', lst)
# selectSort(lst, reverse=True)
# print('排序后: \n', lst)


# def bubbleSort(lst, reverse=False):
#     length = len(lst)
#     for i in range(0, length):
#         flag = False
#         for j in range(0, length-i-1):
#             exp = 'lst[j] > lst[j+1]'
#             if reverse:
#                 exp = 'lst[j] < lst[j+1]'
#             if eval(exp):
#                 lst[j], lst[j+1] = lst[j+1], lst[j]
#                 flag = True
#         if not flag:
#             break
# lst = [randint(1, 100) for i in range(20)]
# print('排序前: \n', lst)
# bubbleSort(lst)
# print('排序后: \n', lst)


# def main(n):
#     start = 10**(n-1)
#     end = 10**n
#     for i in range(start, end):
#         big = ''.join(sorted(str(i), reverse=True))
#         little = ''.join(reversed(big))
#         big, little = map(int, (big, little))
#         if big - little == i:
#             print(i)
# main(int(input('输入一个n：')))


# def hannoi(num, src, dst, temp=None,zzy=None):
#     global times
#     assert type(num) == int, 'num must be integer'
#     assert num > 0, 'num must > 0'
#     print(f"zzy={zzy},num={num},起始={src},目标={dst},中间={temp}")
#     if num == 1:
#         print('The {0} Times move:{1} == > {2}'.format(times, src, dst))
#         times += 1
#     else:
#         hannoi(num - 1, src, temp, dst, zzy='one')
#         hannoi(1, src, dst, zzy='two')
#         hannoi(num - 1, temp, dst, src, zzy='three')
# times = 1
# hannoi(4, 'A', 'C', 'B')


# maxTime = 3
# def guess(num, time, maxValue=10):
#     value = randint(1, maxValue)
#     if time == maxTime:
#         print('Game over. FAIL')
#         print('The value is:', value)
#
#     if time < maxTime:
#         print(f"{20 * '-'}Time = {time}{20 * '-'}")
#         print('Start to GUESS:') if time == 0 else print('GUESS again:')
#         print('I guess:', num)
#         try:
#             isinstance(num, int)
#             assert 1 <= num <= 10
#         except:
#             print('Must input an integer between 1 and ', maxValue)
#         else:
#             if  num == value:
#                 print('Congratulations!')
#                 return True
#             elif num > value:
#                 print('Too big')
#                 return False
#             else:
#                 print('Too small')
#                 return False
#
# def AIguess():
#     for i in range(0, 10):
#         x = randint(0, 12)
#         if guess(x, i):
#             break
#         else:
#             continue
#
# AIguess()


# def Rate(origin, userInput):
#     if not (isinstance(origin, str) and isinstance(userInput, str)):
#         print('The two parameters must be strings.')
#         return
#     right = sum((1 for o, u in zip(origin, userInput) if o==u))
#     print(right)
#     return round(right/len(origin), 2)
#
# # s1 = 'Readability conts'
# s1 = str(input('请输入第一次命令'))
# s2 = str(input('请输入第二次命令'))
# print(Rate(s1, s2))


# def demo(n):
#     def IsPrime(p):
#         if p == 2:
#             return True
#         if p%2 == 0:
#             return False
#         for i in range(3, int(p**0.5)+1, 2):
#             if p%i == 0:
#                 return False
#         return True
#     if isinstance(n, int) and n > 0 and n%2 == 0:
#         for i in range(2, n//2+1):
#             if IsPrime(i) and IsPrime(n-i):
#                 print(i, '+', n-i, '=', n)
#
# demo(100)


# 杨辉
# def yanghui(t):
#     print([1])
#     line = [1, 1]
#     print(line)
#     for i in range(2, t):
#         r = []
#         for j in range(0, len(line) - 1):
#             r.append(line[j] + line[j+1])
#         line = [1] + r + [1]
#         print(line)
#
# yanghui(5)


# def demo(s):
#     result = [0, 0]
#     for ch in s:
#         if ch.islower():
#             result[1] += 1
#         elif ch.isupper():
#             result[0] += 1
#     return tuple(result)
# print(demo('ighiufg3i4FRFGFGFEF'))


# def demo(*p):
#     print(p)
# demo(1, 2, 3)
# demo(1, 2, 3, 4, 4, 5)
#
# def demo1(**p):
#     for item in p.items():
#         print(item)
# demo1(x=1, y=2, z=3)


# def demo2(a, b, c):
#     print(a+b+c)
#
# seq = [1,2,3]
# demo2(*seq)
# dic = {1:'a', 2:'b', 3:'c'}
# demo2(*dic.keys())


# def factors(num, fac=[]):
#     for i in range(2, int(num**0.5)+1):
#         if num % 1 == 0:
#             fac.append(i)
#             print(fac)
#             factors(num//i, fac)
#             break
#         else:
#             fac.append(num)
#             print(fac)
#
# art = []
# n = 77190905
# factors(n, art)
# result = '*'.join(map(str, art))
# if n == eval(result):
#     print(n, '='+result)
#
# print(2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2*2)


# n = int(input('请输入一个正整数'))
# while n > 1:
#     print("该你拿了，现在剩余物品数量为：{0}".format(n))
#     while True:
#         try:
#             num = int(input('输入你要拿走的物品数：'))
#             assert 1 <= num <= n//2
#             break
#         except:
#             print('最少拿走一个，最多拿走{0}'.format(n//2))
#     n -= num
#     if n == 1:
#         print('恭喜你你赢了')
#         break
#     n -= randint(1, n//2)
# else:
#         print('哈哈，你输了')


# data = time.localtime()
# year, month, day = data[:3]
# day_month = [31,28,31,30,31,30,31,31,30,31,30,31]
# if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
#     day_month[1] = 29
# if month == 1:
#     print(day)
# else:
#     per = sum(day_month[:month - 1]) + day
#     print(per)
#     print(per/sum(day_month) * 100)


# numbers = []
# while True:
#     x = input('请输入一个成绩')
#     try:
#         numbers.append(float(x))
#     except:
#         print('不是合法成绩')
#     while True:
#         flag = input('继续输入吗？（yes/no）').lower()
#         if flag not in ('yes', 'no'):
#             print('只能输入yes或No')
#         else:
#             break
#     if flag == 'no':
#         break
# print(sum(numbers)/len(numbers))


# x=[1, 2, 3, 2, 3]
# x.pop()
# print(x)


# x, y, z = 1, 2, 3
# v_tuple = (False, 3.5, 'exp')
# x, y = y, x
# keys = ['a', 'b', 'c', 'd']
# values = [1, 2, 3, 4]
# for k, v in zip(keys, values):
#     print(k, v)
# s = {'a':1, 'b':2, 'c':3}
# for k, v in s.items():
#     print(k, v)


# data = {'user' + str(i):{'film' + str(randrange(1, 15)) : randrange(1, 6) for j in range(randrange(3, 10))}
#         for i in range(10)}
#
# user = {'film' + str(randrange(1, 15)):randrange(1, 6) for i in range(5)}
#
#
# f = lambda item:(-len(item[1].keys()&user), sum(((item[1].get(film)-user.get(film))**2 for film in user.keys()&item[1].keys())))
#
# similarUser, films = min(data.items(), key = f)
# print('known data'.center(50, '='))
#
# for item in data.items():
#     print(len(item[1].keys() & user.keys()),
#     sum(((item[1].get(film) - user.get(film)) ** 2
#         for film in user.keys() & item[1].keys())), item, sep = ':')
#     print('current user'.center(50, '='))
#     print(user)
#     print('most similar user and his films'.center(50, '='))
#
#     print(similarUser, films, sep=':')
#
#     print('recommended film'.center(50, '='))
#  # 在当前用户没看过的电影中选择打分最高的进行推荐
#
#     print(max(films.keys() - user.keys(), key=lambda film: films[film]))


# lstColor = ('red', 'green', 'blue')
# colors = [random.choice(lstColor) for i in range(100)]
# print(set(colors) - set(lstColor))
# if set(colors)-set(lstColor):
#     print('error')


# def randomNumbers(number, start, end):
#     data = set()
#     while len(data) < number:
#         element = random.randint(start, end)
#         data.add(element)
#     return data
#
#
# data = randomNumbers(10, 1, 100)
# print(data)


# x = string.ascii_letters + string.digits
# z = ''.join((random.choice(x) for i in range(10)))
# # print(z)
# d = dict()
# for ch in z:
#     # print(ch)
#     d[ch] = d.get(ch, 0) + 1
#     # print(d[ch])
# for k, v in sorted(d.items()):
#         print(k, ':', v)


# a_set = set(range(3,8))
# b_set = set([0,1,2,3,4,1,2,4,9,6])
# print(a_set)
# print(b_set)


# d = dict()
# d = {'a':1, 'b':[2,5], 'c':3}
# # d = dict.fromkeys(['name', 'age', 'sex'])
# g = d.get('a')
# print(d)
# d['address'] = 'beijing'
# for value in d.items():
#     print(value)
