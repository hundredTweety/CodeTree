N = int(input())
i=1
while i <= N:
    if i %3 ==0 or i%6 == 0 or i%9 == 0:
        print(0, end = " ")
    elif '3' in str(i) or '6' in str(i)or '9' in str(i):
        print(0, end = " ")
    else:
        print(i, end = " ")

    i+=1
