
i=10

def msg():
    i=globals()['i']
    print("Global value of i=",i)
    i = 5
    global j # to make local varable to global variable
    j=5
    print("inside=",i)

msg()
print("outside=",i)
print("outside j=",j)