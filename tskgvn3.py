a=int(input("enter a number"))
str=input("enter a string")

if a > len(str):
    print("the entered number is larger than the lenght of string")
    exit()

else:
    front=str[:a]
    back=str[a+1:]
    print(front+back)
