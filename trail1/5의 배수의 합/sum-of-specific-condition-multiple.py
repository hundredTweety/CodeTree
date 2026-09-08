A, B = map(int, input().split())
total = 0
if A>B:
    max=A
    min=B
else: 
    max=B
    min=A

for i in range(min, max+1):
    if i%5 ==0:
        total += i
print(total)