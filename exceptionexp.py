try:
    a=int(input("Enter first Number"))
    b=int(input("enter second number"))
    c=a/b
    print("div=",c)
    l=[2,5,6]
    print(l[0])



except ZeroDivisionError as e:
    print("B can not be zero",e)

except ValueError as e:
    print("You have input a character not an integer",e)

except Exception as e:
    print("somthing went wrong")

finally:
    print("thank you")