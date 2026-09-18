N = int(input())
cnt = N
for i in range(2*N):
    if i %2 !=0:
        print("* "* ((i+1)//2))

    else:
        print("* "* cnt)
        cnt -= 1
