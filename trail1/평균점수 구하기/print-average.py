score = list(map(float, input().split()))
total = 0
for i in range(len(score)):
    total += score[i]

print(f"{total/len(score):.1f}")