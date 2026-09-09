N=int(input())
for i in range(N):
    for j in range(N-i):
        for z in range(N-i):
            print("*", end= "")
        
        print(" ", end= "")
        
    print()
