def asterisk_test(a, *args) :
    print(a,args)
    print(type(args))

asterisk_test(1,2,3,4,5,6)