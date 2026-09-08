N = int(input())

total = 0

for i in range(1, N+1):
    num = int(input())
    if num %2 != 0 and num %3 ==0:
        total += num
print(total)