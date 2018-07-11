error_num=0
while True:
    username=input('请输入用户名：')
    password=input('请输入密码：')
    if username =='seven'and password=='123':
        print('登录成功！')
        break
    else:
        print('登录失败！')
        error_num +=1 
        if error_num ==3:
            exit()
        else:
           continue
