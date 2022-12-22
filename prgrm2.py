eng=("enter 1 for english")
hin=("enter 2 for hindi")
kan=("enter 3 for kannada")
choice=int(input("enter the choice"))

if choice==1:
    print("you has choosen language for english")

elif choice==2:
    print("you has choosen language for hindi")

elif choice==3:
    print("you has choosen language for kannada")

if choice==4 or 5 or 7 or 8 or 9:
    print("entered wrong choice")
