class Aircondition():
    def __init__(self,name,degree,color,price,typestyle):
        self.name=name
        self.degree=degree
        self.color=color
        self.price=price
        self.typestyle=typestyle
        print('名称:',name,'温度:',degree,'颜色:',color,'价格:',price,'类型:',typestyle)

    def cool(self,name,degree):
        degree-=1
        print(name,'空调降温后当前温度为:',degree)

    def hot(self,name,degree):
        degree+=1
        print(name,'空调升温后当前温度为:',degree)

air=Aircondition('Haier',25,'Pink',2555,'挂式')
air.cool('海尔',20)
air.hot('Midea',21)
        
        
