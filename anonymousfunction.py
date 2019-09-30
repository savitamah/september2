from functools import reduce


def add(a,b):
    return a+b

print(add(4,6))


'''
lambda function takes any no of arguments but have only one statements

'''

s=lambda a,b:a+b
print(s(3,6))


def find_even(n):
    return n%2==0

print(find_even(10))

l=[45,55,66,22,33,58,88,99]
even=list(filter(lambda n:n%2==0,l))
print(even)

double_element=list(map(lambda n:2*n,even))

print(double_element)

f=reduce(lambda a,b:a+b,double_element)
print(f)