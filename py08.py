# # 1.字符串编码（本质上就是二进制与语言文字的一一对应关系）
# # Unicode: 所有字符都是2个字符，好处：字符与数字之间的转化速度更快  坏处：占用空间大
# # UTF-8 : 精准，对不同的字符用不同的长度表示  好处：节省空间  坏处：字符与数字转换速度慢，每次都要计算字符需要用多少个字节表示
# # 定义
# # 字符串编码（encode()）:将其他编码的字符串转换成Unicode编码
# # 字符串解码（decode()）:将Unicode编码转换为其他编码的字符串
# # 注意： encode 和 decode 后面的括号表示编码的类型，也就是转换格式，达到别的效果
# # 举例
# a = "hello"
# print(a,type(a))  # 输出结果为 hello <class 'str'>
# a1 = a.encode()   # 编码
# print('编码后：',a1)   # 输出结果为 编码后： b'hello'
# print(type(a1),a1)  #  输出结果为 <class 'bytes'> b'hello'   bytes以字节为单位处理
# a2 = a1.decode()  # 解码
# print(a2,type(a2))  # 输出结果为 hello <class 'str'>
# # 注意：只需要知道bytes与字符串之间的相互转换
#
# b = 'sixstar'
# print(b,type(b))   # 输出结果为 sixstar <class 'str'>
# b1 = b.encode("utf-8")  # 编码
# print(b1,type(b1))   # 输出结果为 b'sixstar' <class 'bytes'>
# b2 = b1.decode('utf-8')  # 解码
# print(b2,type(b2))   # 输出结果为 b'sixstar' <class 'str>
#
# # 2.字符串的常见操作
#
# # 2.1 字符串运算符
#
# # 2.11 + 表示字符串拼接
# print(10+10)  # 此处的+为数值运算符，输出结果为20
# print("10"+"10")  # 此处的+为字符串与算符，输出结果为1010
# #也可以这样拼接
# print("10","10",sep="")
#
# # 2.12 * 表示重复输出
# print('好好学习，天天向上\n'*5)   # 就是输出了5遍 好好学习天天向上 换行
# print('$\t'*8)   # 输出了8遍$ 制表符空四格
#
# # 2.13 成员运算符（检查字符串中是否包含某些字符
# # in : 如果包含的话，返回为True,包含返回False
# # not in : 如果包含的话，返回为False，不包含返回为True
# c = "bingbing"
# print('bin'in c)   # 返回为True
# print('a'not in c)  # 返回为True
# print('binb'in c)   # 返回为False
#
# # 2.2 下标\索引（通过下标能快速找到相应的数据）
# # 格式：字符串[下标值]
# # python 中下标从0开始（从左往右），-1开始（从右往左）
# name = "bingbing"
# print(name[0])  # 输出为 b
# print(name[1])   #输出为 i
# print(name[-1])   # 输出为 g
#
# # 2.3 切片（对操作对象只截取一部分的操作）
# # 基本格式：[开始位置:结束位置:步长]   左开右闭
# # 从左往右顺序从0开始
# h = 'abcdefgkl'
# print(h[0:2])   # 输出结果为ab
# print(h[3:7])   # 输出结果为defg
# print(h[3:])    # 输出结果为efgkl，输出第三位以后的包括第三位
# print(h[:3])   # 输出结果为abc ，输出第三位以前的不包括第三位 左开右闭原则
# # 从右往左顺序从-1开始
# m = 'zxcvbnm'
# print(m[-5:-1])   # 输出结果为cvbn
# print(m[:-2])   # 输出结果为zxcvb
# # 补充步长（截取间隔）（步长没设定时默认为1，为负时改变方向）
# print(m[-1:-5:-1])  # 输出结果为mnbv
# print(m[0:7:2])   # 输出结果为zcbm,空了1格来取
#
# # 3.字符串其他常见操作
#
# # 3.1 查找find(查找某个子字符串是否包含在字符串内，若在则返回位置，不在就返回-1)
# # 基本格式：变量名.find(子字符串,开始时候位置,结束时候位置)  （此处开始和结束的位置同样左开右闭，可省略）
# n = 'bingbing'
# print(n.find('ing'))    # 输出结果为1
# print(n.find('b',0,3))   # 输出结果为0 表示第一个就是b
# print(n.find('b',3))   # 输出结果为4，表示从下标3往后搜索b，b下标为4
# print(n.find('bing',0,6))   # 输出结果为0 只输出第一位所在下标
# print(n.find('b',3,4))   # 左闭右开 输出-1
#
# # 3.2 查找index（查找某个子字符串是否包含在字符串内，若在则返回位置，不在就报错）
# # 基本格式：变量名.index(子字符串,开始位置下标,结束位置下标)
# b = '我命由我不由天'
# print(b.index('命',1,5))    # 输出1
# # 其实就把find和index当成一样的东西就行
#
# # 3.3 count(返回某个字符串在整个字符串中出现的次数)
# # 基本格式：变量名.count(子字符串,开始位置下标,结束位置下标)
# c = 'bingbing'
# print(c.count('b'))   # 输出为2，表示b出现2次
# print(c.count('i',1,4))   # 输出为1
#
# # 3.4 startswith（判断某字符串是否以某字符开头）
# # 基本格式：变量名.startswith(子字符串,开始位置下标,结束位置下标)




