year=input('请输入年份：')
month=input('请输入月份：')
year = int(year)
month=int(month)
if month==1 or month==3 or month ==5 or month==7 or month==8 or month==10 or month==12:
    print(month,'有31天')
elif month==4 or month ==6 or month==9 or month ==11:
    print(month,'有30天')
elif month==2:
    if (year %4==0 and year %100!=0) or year %400==0:
        print(month,'有29天')
    else:
        print(month,'有28天')
else:
    print('输入错误')
