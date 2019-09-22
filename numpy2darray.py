from numpy import *

arr=array([
           [5,6,9],
           [8,7,3],
           [1,2,25]
])
print(arr[0][0])
print(arr)

print(arr.dtype)

print(arr.shape)

print(arr.size)

# convert 1-d array from 2-d array
arr2=arr.flatten()
print(arr2)

arr3=array([1,2,3,4,5,6,7,8,9,10,11,12])
arr4=arr3.reshape(3,4)
print(arr4)

a=array([
           [1,2],
           [4,5],

])


b=array([
           [5,6],
           [8,7]
])
print(a)
print(b)

print(matrix(a))
print(matrix(b))

c=a+b
print(c)



d=a-b
print(d)

x=matrix(arr)
print(diagonal(x))
print(x.min())

print(x.max())

s=matrix('1 2 3; 2 3 4; 5 6 7')
print(s)
s2=matrix('1 1 1; 2 2 2; 3 3 3')
m=s+s2
print(m)
m2=s*s2
print(m2)

k=matrix(a)
l=matrix(b)
print(k*l)

