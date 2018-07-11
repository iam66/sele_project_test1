def test_var_args(f_arg,*args):
    print("first normal arg:"+f_arg)
    for arg in args:
        print("another arg through *args:",arg)
