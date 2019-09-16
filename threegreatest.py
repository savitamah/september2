a=int(input("Enter first Number"))
b=int(input("enter second number"))
c=int(input("enter third number"))

if a>b:
    if a>c:
        print("a is greatest")
    else:
        print("c is greatest")
elif b>c:
     print("b is greatest")
else:
    print("c is greatest")