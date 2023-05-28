# -*- coding: utf-8 -*-
# Auther : SHL
# Date : 2023-05-15 20:22
# File : game.py

class Game:
    def __init__(self,hp,power):
        self.hp=hp
        self.power =power


    def fight(self,enemy_hp,enemy_power):
        final_hp =self.hp-enemy_power
        enemy_final_hp = enemy_hp -self.power
        if  final_hp > enemy_final_hp:
                print("我赢了")
        elif final_hp<enemy_final_hp:
            print("敌人赢啦")
        else:
            print("平局")

class HouYi(Game):
    ##如果再子类中重新定义__init__,那么父类的__init__将会被覆盖
    def __init__(self):
    ##super 是用来解决多重继承问题的，直接用类名调用父类方法在使用单继承的时候没问题，但是如果使用多继承，会涉及到查找顺序（MRO）、重复调用（钻石继承）等种种问题。总之前人留下的经验就是：保持一致性。要不全部用类名调用父类，要不就全部用 super，不要一半一半。
        super().__init__(1000,200)
        self.defense = 99

    def houyi_fight(self,enemy_hp,enemy_power):
        while True:
            self.hp = self.hp+self.defense - enemy_power
            enemy_hp = enemy_hp - self.power
            print(self.hp)
            print(enemy_hp)
            if self.hp <= 0:
                print("我输了")
                break
            elif enemy_hp <= 0:
                print("敌人输啦")
                break



hp =1000
power = 200
# 继承游戏类game
huoyi =HouYi()
huoyi.houyi_fight(hp,power)



# hp =1000
# power = 200
# game =Game(hp,power)
# game.fight(1000,100)