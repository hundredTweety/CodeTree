N= int(input())
count = 0
for i in range(2,N):
    if N%i == 0:
        count +=1

if count >=1:
    print("C")
else:
    print("N")