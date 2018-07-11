#定义父类
class parents:
    #父类方法
    def myMethod(self):
        print('定义父类方法')

#定义子类
class child(parents):
    def myMethod(self):
        print('子类重写方法')

#子类实例：  c=child()
#子类调用重写方法   c.myMethod()
