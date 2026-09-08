count = 0
while True:
    n=int(input())
    if n %2==0:
        n = int(n/2)
        count +=1
        print(n)
        if count ==3:
            break