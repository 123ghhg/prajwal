def absolute(x):
    if x <21:
        ans=n-21
        print(x,"less than 21")
        return ans
    else:
        ans=n-21
        ansl=ans*ans
        print(x,"more than 21")
        print("the doubled value is",ansl)
        return ans

print("printing the absolute value of n =")
n=int(input("enter the value of n"))
ansl=absolute(n)
print("the difference b/w ",n,"& 21 is:",abs(ansl))

        
