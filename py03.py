# # 1.数值讲解
# # 1.1 int整型（常用）：任意大小的整数
# num1 = 1
# #检查数据的类型的方法 type()
# print(type(num1))  # 输出结果为 <class 'int'>
# # 1.2 float浮点数：小数
# num2 = 1.2
# print(type(num2))  #输出结果为 <class 'float'>
# # 1.3 bool布尔型（重点） （通常用于判断）
# # 有固定写法，一个为True,一个为False 区分大小写
# print(type(True))  # 输出结果为 <class 'bool'>
# # True 和 False可以当成整数对待，对应1和0
# print(True + False)  # 输出结果为1
# # 1.4 complex复数型（了解）
# # 固定写法 z = a + bj  （虚数单位只能是j）
# print(type(2 + 3j))  # 输出结果为<class 'complex'>
# fu_shu = 2 + 1j
# fu_shu2 = 3 + 2j
# print(fu_shu +  fu_shu2)  # 输出结果为 (5+3j)
#
# # 2.字符串类型str
# # 特点：需要加上引号，单引号和双引号都ok，包含多行内容时也可以使用三引号
# # name = sixstar  # 会报错，赋值号右侧被识别为变量名，sixstar没有被赋值
# name = 'sixstar'
# print(name)  # 不报错，输出结果为sixstar
# print(type(name))   # 输出结果为 <class 'str'>
# name = """sixstar
# haha"""     # 多行内容三引号不报错
# # 注意多行注释与三引号的字符串类型的区别，多行注释单独存在，前不需要有变量名，不会被执行
#
# # 3. 格式化输出
# # 3.1 占位符
# # 3.1.1 占位符的作用： 生成一定格式的字符串
# # 3.1.2 占位符的三种方式
# # a. %s 字符串（常用）
# name1 = 'bingbing'
# print('我的名字：%s' % name1)  #输出结果为 我的名字：bingbing
# # 注意：第一个%s是插入字符串，第二个%是开启格式
#
# # b. %d 整数（常用）
# age = 18
# name = 'bingbing'
# hobby = 'badminton'
# print('我的名字:%s，年龄:%d，爱好:%s'% (name,age,hobby))  # 输出结果为 我的名字:bingbing，年龄:18 等等
#
# # c. $4d 整数
# # 数字设置位数，不足前面补空白
# a = 1234
# b = 123
# print('焦梓钰的日工资是%3d，韩思瑜的日工资是%4d'%(b,a))
# print('%8d'%a)   # 输出结果共八位 1234前补了四个空白
# print('%08d'%a)  # 输出结果共八位 00001234
#
# # d. %f 浮点数（常用）
# s = 1.23
# print('%f'%s)  # 输出结果1.230000 默认小数点后六位 若输入为数过多，以第六位四舍五入
#
# #  e.%.4f 浮点数 （注意要加点）
# # 数字设置小数位数
# b = 2.34567
# print('%.3f'%b) # 输出结果为 2.346 四舍五入原则 浮点数多了会自动用0补小数位数
#
# # 3.2 f格式化
# # 格式：f"{表达式}"
# name = 'bingbing'
# age = 18
# print(f'我的名字是{name},我今年{age}岁了')  #输出结果为 我的名字是bingbing,我今年18岁了
#
# # 笔记总结
# # 1.好像f格式化比占位符简单一点
# # 2.对于占位符 %s字符串 %d整数（需要前面补位就加数字） %f小数（小数自动补或四舍五入至六位，需要精确就前加数字）
# # 3.字符串在print里一定加’‘，不然会当作变量名
#
# # 练习时刻
# num1 = 176.3
# num2 = 158.0
# print(f'韩思瑜身高是{num1},韩思彤的身高是{num2}')
# print('韩思瑜身高是%.1f，韩思彤的身高是%.1f'%(num1,num2))
#
# num3 = 3.14159265358979
# print('圆周率前七位是%.7f'%num3)
#
# name = 'hansiyv'
# name2 = 'lichenshuo'
# num4 = 639.00
# num5 = 634.000000000
# print('%s的高考成绩是%.2f,%s的高考成绩是%.4f'%(name2,num5,name,num4))
# print("%s和%s的高考总分为(%.2f + %.2f)"%(name,name2,num4,num5))
# print(num4+num5)
#
# num6 = 30
# num7 = 10
# print(f"我洗漱需要花费{num7}分钟，姐姐化妆需要花费{num6}分钟")
# print('姐姐化妆需要花费%d分钟，我洗漱需要花费%d分钟'%(num6,num7))
#
# hobby = 'strike Qinpeihao'
# character = "hansiyv"
# tool = 'dagoubang'
# way = 'hold'
# print('%s %s %s %s'%(character,way,tool,hobby))