N =int(input())
total = 0
count = 0

for i in range(N):
    num= int(input())

    total +=num
    count+=1
print(total, f"{total/count:.1f}")