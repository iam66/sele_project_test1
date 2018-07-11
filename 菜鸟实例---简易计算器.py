def add(x,y):
    return x+y
def sbustract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y

print('请选择运算：')
print('1、加法')
print('2、减法')
print('3、乘法')
print('4、除法')

choose = int(input('请输入您的选择（1/2/3/4）：'))
if choose ==1 or choose ==2 or choose ==3 or choose==4:
    num1=int(input('请输入第一个数字：'))
    num2=int(input('请输入第二个数字：'))
    if choose ==1:
        print(num1,'+',num2,'=',add(num1,num2))
    elif choose ==2:
        print(num1,'-',num2,'=',substract(num1,num2))
    elif choose ==3:
        print(num1,'x',num2,'=',multiply(num1,num2))
    elif choose ==4:
        print(num1,'/',num2,'=',divide(num1,num2))
else:
    print('您的输入有误')
