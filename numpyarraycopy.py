from numpy import *
arr=array([2,8,9,6,4])
print(max(arr))
print(min(arr))
print(sqrt(arr))
print(log(arr))
print(arr)

print("aliasing")
arr2=arr
print(arr2)

print(concatenate([arr,arr2]))
print("arr=",id(arr))
print("arr2=",id(arr2))

#what if u want diffrent address
print("shallow copy")
arr3=arr.view()
print(arr)
print(arr3)
print("arr=",id(arr))
print("arr3=",id(arr3))

arr3[0]=5000
print(arr3)
print(arr)

#what if u want diffrent address and not affecting with each other
print("deep copy")
arr4=arr.copy()
print(arr)
print(arr4)
print("arr=",id(arr))
print("arr4=",id(arr4))

arr4[0]=9544
print(arr4)
print(arr)