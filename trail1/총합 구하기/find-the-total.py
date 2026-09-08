A,B=map(int, input().split())

if A>B:
    min = B
    max =A
else:
    min = A
    max =B
total = 0
for i in range(min, max+1):
    if i %6 ==0 and i %8!=0:
        total += i

print(total)