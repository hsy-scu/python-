# # 1. 字面量 变量 字符串
# print("Hello World")
# print(100)
# print(3.14)
# print(True)
# print(False)
# print(None)
# # bool 的 True表示1
# print(True+1)
#
# num = 14
# print(num)
# num = 15
# print(num)
# num = True
# print(num)
# num = "OK"
# print(num)  # python里面变量类型随便
#
# num,num1 = 1,2    # 逗号隔开直接定义多个变量
# print("我爱你中国",num+num1) # 输出逗号隔开不同东西 print输出是自带\n的
# print(type("Hello"))  # type来看数据的类型
# print(isinstance(num,int))  # 判断num是不是类型int
#
# flag = "人生苦短"
# flag2 = "我用python"
# print(flag+","+flag2)  # 字符串拼接只能拼接字符串 如果是其他类型的变量 需要类型转换
#
# name = "韩思瑜"
# age = 18
# pro = "软件工程"
# print("大家好，我是"+name+","+"年龄"+str(age)+"岁，"+"专业是"+pro)
# print("大家好，我是%s,年龄%d岁，专业是%s" %(name,age,pro))  # %占位符格式化输出 中间没有逗号
# print(f"大家好，我是{name}，年龄{age}岁，专业室{pro}")      # f{} 格式化输出 更推荐的写法
#
# # 输入 输入的都是字符串类型
# name_ = input()   # input() 它是按行输入的 换行才结束
# age_ = int(input())  # 一定要注意输入的都是字符串类型
# print(f"大家好，我是{name_},年龄是{age_}")
# name1,age1 = input().split()   # split是按空格来截取
# print(f"大家好，我是{name1},年龄是{age1}")
#
# # 运算符需要注意的就是  /是除法算出来是小数  //表示整除算出来是整数  a**b表示a的b次方
# # 逻辑运算符用 and or not
# n = int(input())
# print(f"{n}在10到20之间", n>=10 and n<=20)   # 输出True或者False
#
#
# # 分支语句
# # if elif else
# score = 8
# if score>0:
#     print("正数")
# elif score<0:
#     print("负数")
# else:
#     print("0")
#
# year = int(input())
# if (year%4==0 and year%100!=0) or (year%400==0):
#     print(year+"是闰年")
# else:
#     print(year+"不是闰年")
#
# # match—case 很像c/c++里面的switch 但是不需要加break 它匹配到就直接结束
# day = int(input())
# match day:
#     case 0:
#         print(0)
#     case 1:
#         print(1)
#     case 2|3:
#         print("2和3")
#     case _:
#         print("输入错误")
#
# # while循环 else可有可无 循环结束时走else
# i = 0
# while i<=10:
#     print("人生苦短 我用python")
#     i+=1
# else:
#     print("循环正常结束")
#
# # for循环
# # 字符串遍历 其实很像for_each
# s1 = "hisnsch"
# for s in s1:
#     print(s)

# # 数字遍历
# for i in range(1,10,1):    # 左闭右开(start,end,step)
#     print(i)
# # 循环的嵌套
# m = 10
# n1 = 5
# for i in range(m):  # range(m) 表示循环m次
#     for j in range(n1):
#         print("*",end=" ")
#     print()


# # 2 数据容器

#------列表-------

# # 列表（一个列表是可以存储不同的数据类型的）（正向是从0开始 反向是从下标-1开始）
# s = [56,90,88,"a","hello",True]   # s的数据类型是list
# print(s[0])   # 56
# print(s[-1])  # True
# # 列表切片
# print(s[0:5:1])  # s[开始位置：结束索引，步长] 结束索引不算 就是左闭右开吧
# print(s[0:-2:1]) # [56, 90, 88, 'a'] 就是从0开始到-2为止 如果想直接取完 那么第二个参数不填就行[0::1]
# print(s[-1:-7:-1])  # 如果步长为负数 那么索引必须也是倒序的 这样就可以实现反着取
# 列表基本函数
# s.append("a") # 在列表尾部添加一个元素
# s.insert(2,"你好")  # 插入元素 (索引，插入内容)
# s.remove("a") # 从头到尾删除第一个a
# e = s.pop(2)  # 删除索引2的元素 如果不写的话 默认删除最后一个 它是有返回值的 返回删除的那个值
# s.sort() # 排序 必须都是相同类型才能sort
# s.reverse() # 翻转列表

# # 一个简单的冒泡排序
# s1 = [8,6,4,3,9,1,3,5]
# for i in range(len(s1)-1):
#     for j in range(len(s1)-i-1):
#         if s1[j]>s1[j+1]:
#             a = s1[j]
#             s1[j]=s1[j+1]
#             s1[j+1]=a
# print(s1)

# # 列表循环输入
# num_list = []
# a = 0
# for i in range(10):
#     n = int(input())
#     a+=n
#     num_list.append(n)
# num_list.sort()
# print(num_list)
# print(num_list[0])
# print(num_list[-1])
# print(a/10)
# print(sum(num_list)/10)


# 列表的合并并去重操作
# s1 = [1,53,6,48,95,2,2,2,2,2,36,4]
# s2 = [64,98,53,122,76]
# s4 = [*s1,*s2]   # 解包 *列表名 s4就是s1+s2
# s5 = s1+s2       # 也可以直接加 直接合并列表
# s3 = []
# for i in range(len(s4)):
#     if s4[i] not in s3:   # python太强大了
#         s3.append(s4[i])
# s3.sort()
# print(s3)


# # 列表推导式
# s1 = []
# for i in range(1,21):
#     if i%2==0:
#         s1.append(i**2)
# s2 = [i**2 for i in range(1,21) if i%2==0]
# # 这里面s1和s2是等效的 列表推导式 [要插入的数 for循环 if条件]  没有条件就不写条件


# --------字符串--------
# 常见小操作
# s = "Hello World"
# print(s[0])
# print(s[-1])
# #s[0] = 'A' # 这个是错的 字符串不可改变
# print(s[0:5:1])  # 切片操作 输出 Hello
# print(s[-1:-6:-1])

# # 常见函数（字符串是不可变的 因此所有的操作函数都不能改变原字符串）
# s = "i think it is an apple"
# index = s.find('a')  # 返回第一次出现的下标
# times = s.count('a') # 返回a出现的次数
# S = s.upper()        # 转大写
# s1 = S.lower()       # 转小写
# print(S)
# list = s.split(' ')  # 以‘-’切割字符串 返回一个列表
# print(list)          # ['i', 'think', 'it', 'is', 'an', 'apple']
# s2 = s.replace(' ','-') # 意思是把s里面的空格替换为‘-’ 并返回一个新字符串

# 判断邮箱格式是否正确
# mail = "sfhrh@163.com"
# if mail.count('@')==1 and mail.count('.')>=1:   # 字符串函数
#     print(True)
# else:
#     print(False)
# if '@' in mail and '.' in mail:   # in运算符
#     print(True)
# else:
#     print(False)


# -------元组--------
# 列表元素可重复有序可以修改 元组元素也可重复有序 但是不能修改只能查询
# 其实就是const/Final 修饰的列表 静态元素
# t1 = (5,7,6,4,5,4,7,6,5,4,1)
# t11 = ()
# t12 = tuple()  # 两种方法定义空元组
# print(t1[0:3:1])  # 切片操作
# num = t1.count(5) # 元组里面5的个数
# index = t1.index(6) # 第一个出现6的下标
# t3 = (100,) # 定义一个元素的元组的话 后面必须加逗号

# 元组的组包和解包 组包其实就是直接定义
# tt = (1,2,3,4)
# a,b,c,d = tt    # 基础解包
# a1,*a2 = tt     # *这个符号用来接受所有剩余元素 *最后返回的是列表
# b1,*b2,b3 = tt # b2 = [2,3]
# print(a1,a2,b1,b2,b3)

# 根据元组的解包组包 可以有以下操作
# 1--交换两个数
# a=10
# b=20
# a,b = (b,a)
# print(a,b)

# 小案例
# students = (
#     ("s001","王嘘嘘",85,92,78),
#     ("s002","蔡徐坤",99,99,99),
#     ("s003","韩思瑜",100,100,101)
# )
# # 输出总分和平均分
# for st in students:
#     total = (st[2]+st[3]+st[4])
#     avg = total/3
#     avg = round(avg,1)
#     print(f"{st[0]}\t{st[1]}\t{st[2]}\t{st[3]}\t{st[4]}\t{total}\t{avg}")
#
# ch = [s[2] for s in students]
# ma = [s[3] for s in students]
# en = [s[4] for s in students]
# print(f"语文最高分:{max(ch)}\t数学最高分:{max(ma)}\t英语最高分:{max(en)}")
# print(f"语文最低分:{min(ch)}\t数学最低分:{min(ma)}\t英语最低分:{min(en)}")
# print(f"语文均分:{sum(ch)/len(ch):.1f}\t数学均分:{sum(ma)/len(ma):.1f}\t英语均分:{sum(en)/len(en):.1f}\t")

# ---------集合---------
# # set是无序的(不支持索引) 不可重复的 可修改的
# s1 = {"a","b","c","d","e","f","g","h"}
# s2 = {"b","c","d","e","f","g","h"}
# s = set()  # 空集合定义
#
# # 常用方法
# s1.add("a")
# s1.remove("a") # 如果不存在会报错
# e=s1.pop() # 随机删除并返回
# s1.clear()
# s__ = s1.difference(s2)  # 在s1里面但是不在s2里面的
# s__ = s1 - s2
# s_ = s1.union(s2) # 并集
# s_ = s1 | s2
# s___ = s1.intersection(s2) # 交集
# s___ = s1 & s2


# ---------字典----------
# 字典里面存的是键值对 键必须是不可变类型(string tuple) 值任意都行
# 如果key重复了 后面的值将覆盖前面的值
# d = {"韩思瑜":"大傻逼","蔡徐坤":"小傻逼"}
# d1 = dict()
# d2 = {}  # 两种定义空字典的方法
# nu = d["韩思瑜"]
# print(nu)  # 输出值 大傻逼

# 基本操作函数
# d["大计基"] = "小鸡鸡"
# value = d.pop("韩思瑜")
# del d["韩思瑜"] # 这个是删除 根据key删除值 不返回
# d.keys()  # 获取所有键
# d.values() # 获取所有值
# d.items() # 获取所有键值对
# for k,v in d.items():  print(k,v)

# 一个小案例
# d = dict()
# while 1:
#     n = int(input())
#     if(n==1):
#         name = input()
#         value = int(input())
#         sum = int(input())
#         if name in d:continue
#         d[name]=[value,sum]
#     elif(n==2):
#         name = input()
#         value = int(input())
#         sum = int(input())
#         if name not in d: continue
#         d[name]=[value,sum]
#     elif(n==3):
#         name = input()
#         if name not in d: continue
#         d.pop(name)
#     elif(n==4):
#         for k,v in d.items():
#             print(f"商品名称：{k},商品价格：{v[0]},商品数量：{v[1]}")
#     else:
#         break


# 教务管理系统 用到字典 元组 列表 字符串倒是也有融合吧
# student = {}
# while 1:
#     print("""**********************************************
#     1. 添加学生信息  2.修改学生信息  3.删除学生信息  4.查询学生信息  5.列出所有学生  6.统计班级成绩  7.退出
#     **********************************************
#     """)
#     n = int(input())
#     match n:
#         case 1:
#             name,chinese,math,english = input().split()
#             if name in student:
#                 print("您已添加过该学生")
#                 continue
#             student[name] = (int(chinese),int(math),int(english))
#         case 2:
#             name, chinese, math, english = input().split()
#             if name not in student:
#                 print("该学生不存在")
#                 continue
#             student[name] = (int(chinese),int(math),int(english))
#         case 3:
#             name = input()
#             if name not in student:
#                 print("该学生不存在")
#                 continue
#             student.pop(name)
#         case 4:
#             name = input()
#             if name not in student:
#                 print("该学生不存在")
#                 continue
#             print(f"该生姓名：{name},该生三科成绩：{student[name]}")
#         case 5:
#             for k,v in student.items():
#                 print(f"学生姓名：{k},学生三科成绩：{v}")
#         case 6:
#             ch = [s[0] for s in student.values()]
#             ma = [s[1] for s in student.values()]
#             en = [s[2] for s in student.values()]
#             ch_max = max(ch)
#             ma_max = max(ma)
#             en_max = max(en)
#             ch_min = min(ch)
#             ma_min = min(ma)
#             en_min = min(en)
#             name1,name2,name3,name4,name5,name6 = [],[],[],[],[],[]
#             print(f"语文最高分{ch_max},最低分{ch_min},平均分{sum(ch)/len(ch):.1f}")
#             print(f"数学最高分{ma_max},最低分{ma_min},平均分{sum(ma)/len(ma):.1f}")
#             print(f"英语最高分{en_max},最低分{en_min},平均分{sum(en)/len(en):.1f}")
#             for k,v in student.items():
#                 if v[0]==ch_max:
#                     name1.append(k)
#                 if v[0]==ch_min:
#                     name2.append(k)
#                 if v[1]==ma_max:
#                     name3.append(k)
#                 if v[1]==ma_min:
#                     name4.append(k)
#                 if v[2]==en_max:
#                     name5.append(k)
#                 if v[2]==en_min:
#                     name6.append(k)
#             print(f"语文最高：{name1},语文最低：{name2}，数学最高：{name3},数学最低：{name4},英语最高：{name5},英语最低：{name6}")
#         case 7:
#             break
#         case _:
#             print("输错了 重新输入")




#  3. 函数
# 可以没有返回值和参数列表 直接不写就行
# 参数类型可以是列表元组字典字符串包括基本数据类型 还可以把函数作为参数
# def 函数名(参数列表):
#     函数体
#     return 返回值

# 简单的加法（注意缩进 同等缩进才是一个函数里面的）
# 关于函数传参 其实传的就是形参 对int这些基础类型来说 函数内改变值不会真的改变值 但是对列表 字典等的增删改查 是会影响的
# 函数是可以返回多个值的 封装到元组里面

# 三引号用来写文档注释 可以使用help(函数名)这个方法来查看函数说明
# def add(a,b):
#     """
#     一个简易的两个数运算方法
#     :param a: 第一个参数
#     :param b: 第二个参数
#     :return: 返回ab的和积商差
#     """
#     return a+b,a*b,a/b,a-b
# print(add(1,2))
# # help(add)

# 函数变量的作用域
# num = 50
# def text():
#     num = 100  # 其实是定义了一个新的局部变量 没有改变全局变量num
#     print(num)
# text()
# print(num)   # 先输出100 再输出50 也就是说 函数没有改变全局变量
#
# num1 = 50
# def text1():
#     global num1  # 这个就是把全局变量取过来
#     num1/=2
#     print(num1)
# text1()
# print(num1)    # 输出两个25

# 不定长参数函数传参
# def calc(*arges):   # 其实是一个元组
#     return sum(arges),min(arges),max(arges)
# def calc_(*arges,**kwargs):    # 关键字参数传过来自动组成字典类型 关键字一般是用来调节函数数据的 可能一般还是用的不是很多
#     return sum(arges),min(arges),max(arges),kwargs
# print(calc(1,2,3,4,1,4,3,5))
# print(calc(1,5,9,76))
# print(calc_(1,4,7,2,3,5,a=3,b=5,v=9))

# lambda表达式------匿名函数
# lambda 参数列表：函数体      # 基本写法
# add = lambda x,y: x+y
# print(add(1,2))
# out_line = lambda:print("-------")
# out_line()
# # 由于这个匿名函数只能处理简单的函数 因此一般是很简单的函数才要用lambda函数
# list = ["c++","java","python","c","php","javascript"]
# # sort函数里面只有Key和reverse两个参数 key其实是选择数据的根据 reverse是看是升序还是降序排列 True为降序 False为升序
# list.sort(key=lambda item:len(item),reverse=True)
# print(list)

# def jiecheng(a):
#     if a==1:return 1
#     return a*jiecheng(a-1)
# print(jiecheng(5))
#
# f = {0:1}
# def jc(a):
#     if a in f.keys():return f[a]
#     f[a] = a*jc(a-1)
#     return f[a]
#
# arr = [0]*10
# arr[0]=1
# def jjcc(a):
#     if arr[a]!=0:return arr[a]
#     arr[a] = a*jjcc(a-1)
#     return arr[a]
#
#
# def calc_cost(*args,yhj,score,yf):
#     total_cost = 0
#     for a,b,c in args:
#         total_cost += (b*c)
#     total_cpy = total_cost
#     if total_cost>=5000 and yhj<=total_cost:
#         total_cost-=yhj
#     if total_cpy>=5000 and score//100<=total_cpy:
#         total_cost-=score//100
#     return total_cost+yf



# 4 模块和包
# import 模块名
# import 模块名 as 别名
# import 包名.模块名  调用是 包名.模块名.功能名
# from 包名 import *   调用是 模块名.功能名