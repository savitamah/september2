def rec(n):
    if n==0 or n==1:
        return 1
    else:
        return n*rec(n-1)


s=rec(5)
print(s)