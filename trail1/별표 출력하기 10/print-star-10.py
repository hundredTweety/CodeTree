N = int(input())
cnt = N
for i in range(2*N):
    
    if i %2 == 0:
        print("* "*(i//2+1))
    else:
        print("* "*(cnt))
        cnt -= 1