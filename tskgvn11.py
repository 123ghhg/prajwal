a=[1,2,3,4,5,6,7,8,9,10]
count=0
count1=0
for i in range (len(a)):
    if a[i]%2==0:
        count=count + 1
    if a[i]%2!=0:
        count1=count1 + 1
print("the even numbers are",count)
print("the odd numbers are",count1)
