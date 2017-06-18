class Base1 :
    def __init__(self):
        self.name = "张三"
    def getName(self):
        print("我的名字是：",self.name)
    def hello(self):
        print("HelloWorld")
class Base2(Base1) :
    def __init__(self):
        # super访问父类的属性以及方法
        super().__init__()
class Base3(Base1):
    def __init__(self):
        # super访问父类的属性以及方法
        super(Base3, self).__init__()
b = Base2()
b.getName()
c = Base3()
c.hello()