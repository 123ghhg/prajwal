def check(n1,n2):
    if n1==10 or n2==10:
        return "true"
    elif n1+n2==10:
        return "true"
    else :
        return "false"

a=int(input("enter a value"))
b=int(input("enter a value"))
ans=check(a,b)
print(ans)
