# 1.定义一个类
class people:
    # 2.定义基本属性
    name=' '
    age=0
    # 3.定义一个私有属性，私有属性在类外部无法直接访问
    __weight=0
    # 4.定义构造方法
    def __init__(self,n,a,w):
        self.name=n
        self.age=a
        self.__weight=w
    # 5.定义方法
    def speak(self):
        print('%s说：我今年%d岁，我%dkg。'%(self.name,self.age,self.__weight))

#调用：p=people('Jack',18,50)
#          p.speak()




# 单继承
class student(people):
    #定义自己的基本属性
    grade=' '
    #定义自己的构造方法
    def __init__(self,n,a,w,g):
        #调用父类的构造方法
        people.__init__(self,n,a,w)
        self.grade=g
    #覆写父类的方法
        def speak(self):
            print('%s 说：我今年%d岁，上%d年级'%(self.name,self.age,self.grade))
