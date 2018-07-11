import random
times=3
secret =random.randint(1,10)
print('--------------我爱鱼c工作室-----------------')
guess=0
print("不妨猜一下小甲鱼现在心里想的是哪个数字：",end=" ")
while guess!=secret and times>0:
    temp=input()
    guess=int(temp)
    times=times-1
    if guess ==secret:
        print("wocao，你是小甲鱼心里的蛔虫吗")
        print("哼，猜中了也没有奖励")
    else:
        if guess>secret:
            print("大了大了")
        else:
            print('小了')
        if times>0:
            print('再试一次吧：',end=' ')
        else:
            print('机会用光咯')
print("game over")
