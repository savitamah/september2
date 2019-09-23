def add(x,y):
    z=x+y
    print("Sum=",z)

add(4,5)

def add1(x,y,p):
    z=x+y+p
    print("Sum=",z)

add1(4,5,5)

def sum1(a,*b):
    print(a)
    print(b)
    c=a
    for i in b:
        c=c+i
    print("C=",c)

sum1(1,2,3,4,6,66,77,88,66)


def sum2(*b):
    print(b)
    c=0
    for i in b:
        c=c+i
    print("C=",c)

sum2(1,2,3,4,6,66,77,88,66)


def customer(name,*data):
    print(name)
    print(data)

customer('Ram','Gkp',55,374457234,27307,'mi')

# kyyword varable length argument
def customer1(name,**data):
    print(name)
    print(data)
    for i,j in data.items():
        print(i,j)

customer1('Ram',age=55,city='ndls',phone=5464)

customer1('Ram',age=55,phone=5464,city='ndls')