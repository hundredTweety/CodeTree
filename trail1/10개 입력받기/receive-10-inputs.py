arr =[]
score = list(map(int, input().split()))
total = 0
for i in score:
    if i == 0:
        break

    else:
        arr.append(i)
        total += i

print(total, f"{total/(len(arr)):.1f}")

    