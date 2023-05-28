# -*- coding: utf-8 -*-
# Auther : SHL
# Date : 2023-05-14 22:20
# File : 实例引用.py
class Person:
  #$  __init__ 是创建类的实例时候，调用构造函数
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender =gender

    def set_att(self,value):
        self.value ="fit"

    def eat(self):
        print(f"name :{self.name},age:{self.age},gender:{self.gender }      我在吃.")
    def drink(self):
        print(f"name :{self.name},age:{self.age},gender:{self.gender}       我在喝.")
    def run(self):
        print(f"name :{self.name},age:{self.age},gender:{self.gender}       我在跑.")

xiaoming=Person("xiaoming",10,'male')
xiaohong=Person("xiaoming",10,'male')

print(xiaoming.name)
xiaoming.run()

# print(xiaohong.name)
# xiaohong.drink()
xiaoming.set_att("fit")
print(xiaoming.value)