import time
def mstring (a,b):
    result=""
    for i in range(a):
        result=result+b
    return result

a=int(input("enter a number"))
b=input("enter a string")
if a <0:
    print("please enter a non negative number")
    time.sleep(5)
    exit()
else:
    ans=mstring(a,b)
    print(ans)
