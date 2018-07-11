nianling=int(input("请输入您的年龄"))
xingbie= input ("请输入你的性别")

age=50

if nianling < age:
   if xingbie == "男":
     print ("先生，您真年轻")
   if xingbie == "女":
       print ("小姐，您真年轻")


if nianling > age:
    if xingbie == "男":
        print("先生，您真成熟")
    if xingbie == "女":
        print("小姐，您真成熟")
