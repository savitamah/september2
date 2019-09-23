'''
We can pass value inside function by four methods
1. postional arguments
2. keyword argument
3  variable length argument

'''


def student(name,age):
    print("name=",name)
    #age=age+100
    print("age=", age)


student("Abc",55)
#postional arguments
name,age=input("enter name and age").split(',')
student(name,age)
# keyword argument
student(age=age,name=name)

def student1(name,age=18):
    print("name=",name)
    print("age=", age)

student1("Mohan")
student1("Rohan",55)