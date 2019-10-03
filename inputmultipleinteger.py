'''name,age=input("enter name and age").split()
print(name)
#age=age+10
print(age)

a,b,c,d,e=[int(i)for i in input("enter two no").split()]
print("Number of list is: ",a,b,c,d,e)
total=a+b+c+d+e
print(total)

lst=list(input("enter the list item"))
print(lst)

l=eval(input("enter the list item"))
print(l)

for i in l:
    print(i)'''

l1=list()
print(l1)
print(type(l1))

r=tuple()
print(r)
print(type(r))

l3=[4,4,4,4,4,55,6,7,7,8,8,
    666,7,8,99,9]
print(l3)

l4=[1,2,13]
l5=[1,2,3,66]
print(l4==l5)
print(l4>l5)

print(3 in l4)

l7=[3,4,5]
print(l7*3)