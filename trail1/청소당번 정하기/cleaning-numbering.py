classR=0
floor=0
bath=0

n = int(input())

for i in range(1, n+1):

    if (i%2==0 and i%12 ==0) or (i%3==0 and i%12==0) :
        bath +=1
    elif i% 2 ==0 and i%3 ==0:
        floor +=1

    elif i % 2 ==0:
        classR +=1
    elif i % 3 ==0:
        floor +=1
    elif i %12 == 0:
        bath += 1
print(classR, floor, bath)