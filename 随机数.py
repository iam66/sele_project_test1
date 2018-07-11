import random
answer=random.randint(1,100)
num=int(input('请输入一个数字：'))
while num!=answer:
    if  num>answer:
        print('大啦！')
        num=int(input('请重新输入：'))
    elif num<answer:
        print('小啦！')
        num =int(input('请重新输入：'))
print('答对了')
