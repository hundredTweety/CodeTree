a, b, c = map(int, input().split())

num = [a, b, c]

max = num[0]

for i in range(len(num)):
    if num[i] > max:
        max= num[i]

print(max)