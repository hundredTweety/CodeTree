A, B = map(int, input().split())
count = 0
total = 0
for i in range(A, B+1):
    if i % 5 ==0 or i % 7 ==0:
        total+=i
        count +=1

print(f"{total} {total/count:.1f}")