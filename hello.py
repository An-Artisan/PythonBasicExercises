# 引用随机函数包
#import random
#rand = random.randint(1,10)
#print(rand)
# isinstance(rand,str) 判断数据类型
# assert 3>4  assert断言。当后面的条为假的时候，程序会自动崩溃并抛出AssertionError的异常
'''
i = 0
s = 0
while i < 10 :
    s += i
    i += 1
print("1-10的和是：",s)
for语句的语法
for 目标 in 表达式 ：
    循环体
for each in range(10):
    print(each)
数据类型  列表
list = ['刘强',123,3.14,[1,2]]
添加数据 append
list.append("葫芦娃")
添加多个数据 extend
list.extend([1,2])
插入数据 insert
list.insert(0,[8,9])
删除数据 remove  del pop
list.remove(0)
del list[0]
list.pop() 删除最后一个元素
list.pop(0) 删除第一个元素
列表分片 slice
list[1:3] 不包含3
成员操作符
in  not in
123 in list
dir(list) 打印列表的内置函数
reverse 翻转list列表
sort  用指定的方式对列表的成员排序
list = [1,2]
list.append([3,4])
list.extend([5,6])
list.insert(0,[8,9])
# print(list[0])
list_one = list[:]
print(list_one)
数据类型 元组
元组对数据修改，添加，删除
访问元组和列表是一样的
tuple1[0]
也可以是用切片来对元组操作
创建一个空元组
tuple = ()
创建一个元素的元组
tuple2 = (1,)
添加一个数据，只能这样来添加
tuple =  tpule[:] + ('你好',)
del tuple删除整个元组
tuple1 = (1,2,3,4,5,6,7,8)
字符串访问
string = "liuqiang"
string1 = string
string = "liuqiang++"
print(string1)
string[:6] 切片
string[0] 这样访问单个字符
# string = "liuqiang"
# print('liuf' in string)
# print(len(string))
list("I love fish")
tuple("i love fish") 转成元组
'''

def MyFisrtFunction():
    print("这是我的第一个函数")
MyFisrtFunction()





