arr = []
N = list(map(int, input().split()))
count = 0
total = 0

for i in N:
    if i == 0:
        break

    else:
        if i % 2 == 0:
            count += 1
            total += i

print(count, total)