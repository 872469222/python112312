# -*- coding: utf-8 -*-
# Auther : SHL
# Date : 2023-05-14 22:07
# File : testclass1.py

class Person():
    name = "aaaaaa"

    def ger_name(self):
        return self.name

print(Person.name)
p =Person()
print(p.name)
print(p.ger_name())


# p.name = "lili"
p.name = "xiaoming"

Person.name="lili"
# p.name = "xiaoming"
print(p.name)

p1 =Person()
print(p1.name)