N=int(input())
count=False
for i in range(2, N):
    if N%i == 0:
        count = True

if count ==True:
    print("C")

else:
    print("P")
