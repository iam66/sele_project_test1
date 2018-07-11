#While循环
import random
secret = random.randint(1,10)

temp=input('不妨猜一下小甲鱼现在心里想的是哪个数字：\n')
guess = int(temp)
while guess !=secret:
        if guess >secret:
                        print('兄弟，大了大了')
        else:
                        print('太小啦')
        temp=input('哎呀，猜错了，请重新输入吧：')
        guess = int(temp)
        if guess == secret:
               print('卧槽，你是小甲鱼肚子里的蛔虫吗？')
               print('哼，猜对了也没有奖励')

print ('游戏结束，不玩啦')




'''temp=input('不妨猜一下小甲鱼现在心里想的是哪个数字：\n')
guess = int(temp)
if guess ==8:
	print('卧槽，你是小甲鱼肚子里的蛔虫吗？')
	print('哼，猜中了也没有奖励')
else:
	if guess >8:
		print('兄弟，大了大了')
	else:
		print('太小啦')
print ('游戏结束，不玩啦')'''
