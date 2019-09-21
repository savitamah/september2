from array import *
#import array

arr1=array('i',[4,5,6,8,5])

print(arr1)


arr2=array('f',[4,5,6,8,5.0])

print(arr2)

print(arr1.typecode)

print(arr1.buffer_info())

for i in range(len(arr1)):
    print(arr1[i])

for j in arr1:
    print(j)

print("revesre")

#print(arr1.reverse())

arr3=arr1
print(arr3)

arr4=arr1+arr3 #merge
print(arr4)

arr1[0]=5000
print(arr1)


