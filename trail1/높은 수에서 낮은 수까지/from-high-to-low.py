A, B =map(int,input().split())

if A<B:
    min = A
    max = B
else:
    min = B
    max = A
    

for i in range(max, min-1, -1):
    print(i, end = " ")
    i-= i

