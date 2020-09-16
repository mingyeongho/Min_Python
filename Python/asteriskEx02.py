def asterisk_test(a, **kargs) :
    print(a,kargs)
    print(type(kargs))

asterisk_test(1,b=2,c=3,d=4,e=5)