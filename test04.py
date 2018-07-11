toppings=['']
#第一种方法，使用break
while toppings:
    topping = input("Please enter the toppings:")
    if topping =='quit':
        break
    else:
        print("We will add the "+topping+" in your pizza.")

'''第二种方法：使用变量active控制循环语句
active=True
while active:
    topping = input("Please enter the toppings:")
    if topping =='quit':
        active=False
    else:
        print("We will add the "+topping+" in your pizza.")'''
