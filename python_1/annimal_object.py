"""
比如创建一个类（Animal）【动物类】，类里有属性（名称，颜色，年龄，性别），类方法（会叫，会跑）

创建子类【狗】，继承【动物类】，
复写父类的__init__方法，继承父类的属性，
添加一个新的属性，毛发=长毛，
添加一个新的方法， 会看家，
复写父类的【会叫】的方法，改成【汪汪叫】
调用 name== ‘main’：
创建一个猫猫实例
调用捉老鼠的方法
打印【猫猫的姓名，颜色，年龄，性别，毛发，捉到了老鼠】。
创建一个狗狗实例
调用【会看家】的方法
打印【狗的姓名，颜色，年龄，性别，毛发】
"""


class Animal():
    name = "动物"
    color = "颜色"
    age = 5
    gender = '公母'

    def __init__(self, name, color, age, gender):
        self.name = name
        self.color = color
        self.age = age
        self.gender = gender

    def calling(self):
        print("会叫")

    def running(self):
        print("会跑")


"""
创建子类【猫】，继承【动物类】，

复写父类的__init__方法，继承父类的属性，

添加一个新的属性，毛发=短毛，

添加一个新的方法， 会捉老鼠，

复写父类的‘【会叫】的方法，改成喵喵叫
"""


class Cat(Animal):
    hair = "短毛"

    def __init__(self, name, color, age, gender, hair):
        super().__init__(name, color, age, gender)
        self.hair = hair

    def skill(self):
        print("会捉老鼠")

    def calling(self):
        print("它会喵喵叫")


if __name__ == '__main__':
    c1 = Cat("英国短尾猫", "白色", 1, "母的", "短毛")
    print(c1.name, c1.color, c1.age, c1.gender, c1.hair)
    c1.skill()
