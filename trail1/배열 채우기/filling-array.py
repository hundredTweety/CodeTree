arr = []
N = list(map(int, input().split()))

for i in N:

    if i == 0:
        break

    else:
        arr.append(i)
    
for j in arr[::-1]:
    print(j, end =" ")



