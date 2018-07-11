print("How old are you ?",)
#age=raw_input()【raw_input()是py2的用法，py3只保留了input()】
age=input()
print("How tall are you ?",)
#height=raw_input()
height=input()
print("How much do you weight ?",)
#weight=raw_input()
weight=input()

print("So,you're %r old,%r tall and %r heavy."%(age,height,weight))
