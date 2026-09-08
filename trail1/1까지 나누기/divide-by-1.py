N=int(input())
count = 0
for i in range(1,N+1):
    N = N//i
    count +=1
    if N <=1:
        break

print(count)

