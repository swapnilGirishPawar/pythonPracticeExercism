from Exercism.Basic import lasagna


class test:
    hp = 200

    def __init__(self, atkl, atkh):
        self.atkl = atkl
        self.atkh = atkh

    def getAtk(self):
        print("attack is ", self.atkl, self.atkh)

    def getHp(self):
        print("hp is ", self.hp)


test1 = test(40, 90)
test1.getAtk()
test1.getHp()

l = test(55, 86)
l.getAtk()
l.getHp()
