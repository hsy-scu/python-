# # 1.for循环（迭代循环）
# # 基本格式
# # for 临时变量 in 可迭代对象:
# #     循环体
# # #注意冒号和缩进,可迭代对象就是要去遍历取值的整体，现在只需记住字符串就是一种可迭代对象
# i = 'helloworld'
# for h in i:  # h是临时变量，可以随便写，通常写i
#     print(h)
#
# # 2.range函数
# # 用来记录循环次数，相当于一个计数器
# for i in range(1,6):  # 输出从1到5的数，左闭右开
#     print(i)
# for i in range(5):  # 输出循环次数，从0到4
#     print(i)
# for i in range(1,6):
#     print("永远十八岁")  # 输出5次字符串，直接写数字也能输出相应次循环
#
# # 典型例题
# # 计算从1加到100的值
# s = 0  # 保存计算结果
# for i in range(1,101):
#     s += i
# print("计算结果为%d"%s)
# # 相比之下，for循环要比while循环更简便一点
#
# # 3.break和continue关键字
# # 都是在循环中使用的关键字
# # 3.1 break（每一条件满足时，退出循环）
# i = 1
# while i <= 10:
#     print(f'焦梓钰在吃第{i}碗饭')
#     if i == 9:
#         print('焦梓钰吃饱了不吃了')
#         break
#     i += 1
# # 3.2 continue（退出本次循环，下一次循环继续执行）
# i = 1
# while i <= 10:
#     print(f"焦梓钰在吃第{i}碗饭")
#     if i == 4:
#         print(f'在吃第{i}碗饭的时候，焦梓钰吃到了虫子不吃了')
#         i += 1
#         continue
#     i += 1
#
# for i in range(5):
#     if i == 3:
#         break
#     print(i)
#
# # 一个典型问题 continue是否包含本项问题
# for i in range(5):
#     print(i)
#     if i == 3:
#         print('程序故障，停止此循环')
#         continue
# # 本循环中，print写在if条件前，意味先有print,在有而后的if continue中断，这个时候输出结果为0 1 2 3 程序故障，停止此循环 4。包含3
# for i in range(5):
#     if i == 3:
#         print('程序故障，停止此循环')
#         continue
#     print(i)
# # 本循环中，print写在最后，根据程序从上至下运行原则，到3之后出现continue，而后才有print，此时输出结果为0 1 2 程序故障，停止此循环 4
#
# i = 1
# while i <= 10:
#     if i == 3:
#         print(f'在吃第{i}坨屎的时候噎住了，吐了出来')
#         i += 1
#         continue
#     print(f'秦培豪吃到了第{i}坨屎')
#     i += 1
#
# for i in range(1,11):
#     if i == 3:
#         print('在吃到第3坨屎的时候噎住了,吐了出来')
#         i += 1
#         continue
#     print(f'秦培豪吃到了第{i}坨屎')
#
# time = 9
# mood = "happy"
# state = 'not good'
# breakfast = 'have eaten'
# if mood == 'happy':
#     print("I wanna study in deyuan today",end="-->")
#     if breakfast == 'have eaten':
#         if 8 <= time < 9:
#             print('write and recite English vocabulary after ariving')
#         elif 9 <= time <= 10:
#             if state == "not good":
#                 print('look through videos online to contain state after ariving')
#             else:
#                 print('learn challenging advanced math without hasitation after ariving')
#         else:
#             print('no need studying if you are late')
#     else:
#         print('eat breakfast first after ariving',end='-->')
#         if 8 <= time < 9:
#             print('write and recite English vocabulary after having breakfast')
#         elif 9 <= time <= 10:
#             if state == "not good":
#                 print('look through videos online to contain state after having breakfast')
#             else:
#                 print('learn challenging advanced math without hasitation after having breakfast')
#         else:
#             print('no need studying if you are late')
# else:
#     print('it is better to have a rest today if you are unhappy')
#
# i = 1
# while i <= 10:
#     print('Li keyan is my daughter')
#     j = 1
#     while j <= 1:
#         print('I am the dad of Li keyan')
#         j += 1
#     i += 1
#
