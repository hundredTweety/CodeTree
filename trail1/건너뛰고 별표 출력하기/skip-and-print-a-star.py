N= int(input())

for i in range(1,N+1):
    for j in range(i):
        print("*", end="")
    print("\n")


for i in range(1, N):
    for j in range(N-i, 0, -1):
        print("*", end="")
    print("\n")

