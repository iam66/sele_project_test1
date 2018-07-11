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


#再定义一个类
class speaker():
    topic=' '
    name=' '
    def __init__(self,t,n):
        self.topic=t
        self.name=n
    def speak(self):
        print('我叫%s，我演讲的主题是%s。'%(self.name,self.topic))


#多重继承
class  son(speaker,people):
    born = ' '
    def __init__(self,n,a,b,w,t):
        people.__init__(self,n,a,w)
        speaker.__init__(self,t,n)
        self.born = b
    def speak(self):
        print('我叫%s，今年%d岁，来自%s ,我演讲的主题是%s。'%(self.name,self.age,self.born,self.topic))
        
