N = int(input())

# 위쪽 + 가운데
for i in range(N):
    print("  " * i + "* " * (2 * (N - i) - 1))

# 아래쪽
for i in range(N - 2, -1, -1):
    print("  " * i + "* " * (2 * (N - i) - 1))