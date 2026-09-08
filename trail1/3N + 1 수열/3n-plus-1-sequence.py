count = 0
N = int(input())
while True:
    if N==1:
        break
    
    if N%2 ==0:
        N = N/2
        count += 1
    else:
        N = (N*3)+1
        count += 1

    
print(count)
