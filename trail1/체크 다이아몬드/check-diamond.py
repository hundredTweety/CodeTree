N = int(input())

for i in range(N):
    print(" "* (N-i-1)+ "* "*(i+1))

for j in range(N):
    print(" "*(j+1) + "* "*(N-j-1))