import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(2000)
i=1
def msg():
    global i
    print("hi",i)
    i=i+1
    msg()

msg()

