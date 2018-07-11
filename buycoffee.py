price=5.0
totalprice=0.0
cup=input('请输入购买咖啡的杯数：')
if int(cup)==1:
    print (price)
if int(cup)>1:
    totalprice=(price*0.5*(int(cup)-1))+price
    print(totalprice)
