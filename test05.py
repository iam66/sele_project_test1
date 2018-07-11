action=True
while action:
    age=int(input("Please enter your age:"))
    if 0<age<3:
        print("You're "+str(age)+" years old,the price is free")
    elif 3<=age<12 :
        print("You're "+str(age)+" years old,the price is $10")
    elif age>=12 :
        print("You're "+str(age)+" years old,the price is $15")
    else:
        action=False
