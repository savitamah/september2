from numpy import *
arr=array([7,8,9,6,4.5])
print(max(arr))
print(min(arr))
print(arr)

print(arr.size)

print(arr.shape)

print(arr.dtype)
'''
There are six ways to create an array using numpy

1.array()
2. linspace
3.logspace
4.arange
5.zeros
6.ones
'''

arr2=linspace(1,20,4)
print(arr2)
print(arr2.size)

arr3=logspace(1,20)
print(arr3)
print(arr3.size)

arr4=arange(1,50,5)
print(arr4)
print(arr4.size)

arr5=zeros(5,int)
print(arr5)

arr6=ones(5,int)
print(arr6)

arr7=arr6+5
print(arr7)

arr8=arr7+arr6
print(arr8)

print(sum(arr6))