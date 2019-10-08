s={1,2,3,1,2}
print(s)
s.add(4)
print(s)
s.remove(2)
print(s)
s.clear()
print("khali=",s)
fruit=frozenset(['orange','owla'])
print(fruit)
#fruit.add('tomato')
#empty set
animal={}
print(animal)
print(type(animal)) #this is dictionary
city=set()
print(type(city))
city.add('gkp')
print(city)


#operation on set
a={1,2,3,4,5}
b={1,4,3,5,8}

print(53 in a)

#union
print(a|b)

#intersection
print(a&b)

#diffrence
print(a-b)

#symmetric diff
print(a^b)  #not contain in a and b

print(len(a))

g=a.copy()
print(g)

