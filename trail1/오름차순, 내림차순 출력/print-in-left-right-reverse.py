N = int(input())
cnt = 1
num = N

for i in range(N):
    for j in range(N):
        if i %2==0:
            if cnt > N:
                cnt = 1
            print(cnt, end = "")
            cnt += 1

        else:
            if num == 0:
                num = N
            print(num, end = "")
            num -= 1

    print()
