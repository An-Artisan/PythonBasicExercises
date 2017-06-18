class Person:
    # 以__开头的属性和方法为私有方法和私有属性
    __name = "刘强"
    def getName(self):
        return self.__name
p = Person()
print(p.getName())
# python实际上是伪私有机制，可以用 _类名__属性名，直接访问私有变量
print(p._Person__name)