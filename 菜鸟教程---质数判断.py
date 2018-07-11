num= int(input('请输入一个自然数：\n'))
if num%1==0 and num%num==0:
    print('{0}是质数'.format(num))
else:
    print('{0}不是质数'.format(num))
