def make_shirt(size='large',logo='i love python'):
    print("The size of T-shirt is "+size.title()+" and the logo is "+logo.title())
    return make_shirt

shirt=make_shirt()

shirt2=make_shirt(size='medium')

shirt3=make_shirt(logo='i love you')
