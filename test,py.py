# -*- coding: utf-8 -*-
# Auther : SHL
# Date : 2023-05-14 21:25
# File : test,py.py

# try:
#     num1 = int(input("输入一个除数"))
#     num2 = int(input("输入一个被除数"))
#     print(num1/num2)
# # except ZeroDivisionError:
# #     print("被除数不能为0")
# # except ValueError:
# #     print("输入的需要是数值型整数")
# except:
#     print("这是一个通用型异常")
# finally:
#     print("无论发没发生异常，都执行")
# x = 10
# if x>5:
#     raise  Exception("这是抛出的异常")


class MyException (Exception):
    def __init__(self,value1,value2):
        self.value1 = value1
        self.value2 = value2

raise MyException("value1","value2")