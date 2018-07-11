bonus=0
l=float(input('请输入当月利润：'))
if l <=100000:
	bonus=l*0.1
	print('应发奖金总数为：',bonus)
elif l>100000 and l<=200000:
	bonus=100000*0.1+(l-100000)*0.075
	print('应发奖金总数为：',bonus)
elif l>200000 and l<=400000:
	bonus=(l-200000)*0.05
	print('应发奖金总数为：',bonus)
elif 1>400000 and l<=600000:
	bonus=(l-400000)*0.03
	print('应发奖金总数为：',bonus)
elif l>600000 and l<=1000000:
	bonus=(l-600000)*0.015
	print('应发奖金总数为：',bonus)
elif l>1000000:
	bonus=(l-1000000)*0.01
	print('应发奖金总数为：',bonus)
else:
	print('输入错误！')

