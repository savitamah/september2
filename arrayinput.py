from array import *

a=array('i',[])
n=int (input("enter the size of an array"))
for i in range(n):
    x=int(input("enter the elements of an arrray"))
    a.append(x)

print(a)

search=int (input("enter the item to search"))

for i in range(len(a)):
    if a[i]==search:
        print("Item found at location=",i)

loc=a.index(search)
print(loc)