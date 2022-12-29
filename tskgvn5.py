import math
def getsum(n1,n2):
    n3=n1 + n2
    return n3
def getsumsq(n1,n2):
    n3=n1 + n2
    n4=math.pow(n3,2)
    return n4

a=int(input("enter the 1st value"))
b=int(input("enter the 2nd value"))
if a != b:
    print("the 2 values are defferent")
    ans=getsum(a, b)
    print("the answer of ",a,"+",b,"is", ans)
else:
    print("the 2 numbers are same & so printing the square of the sum")
    ans=getsumsq(a, b)
    print("the sum of ",a,"+",b,"is",a+b,"and the sqaure of the sum is",ans)
    
