#!/usr/bin/python
# -*- coding: UTF-8 -*-

# print("这是第一个程序")
# print("Hello, World!")
# print("Hello, Python!")

# print("为a赋值")
a = 2
# print("a =", a)
# #
# print("运算")
# b = 2
# c = a + b
# print("c =", c)
#
# print("条件语句")
# if a == 1:
#     print("a =", 1)
# else:
#     print("a!=", 1)
#
# print("循环语句")
# while a < 10:
#     print("a =", a)
#     a = a + 1
# #
# print("循环语句 + 条件语句")
# a = 1
# while a < 20:
#     print("a =", a, )
#     if a % 2 == 0:
#         print("a是偶数")
#     else:
#         print("a是奇数")
#     a = a + 1
#
# print("函数")
# def printme(str):
#     print(str)
#     return
# printme("我是通过函数打印的")
#
print("I/O")
fo = open("test.txt", "w")
fo.write("I'm from python io !\n")
fo.close()

