M=int(input())

if 1<=M<=7:
    if M %2 !=0:
        print(31)
    elif M==2:
        print(28)
    else:
        print(30)

elif 8<=M<=12:
    if M%2 ==0:
        print(31)
    else:
        print(30)