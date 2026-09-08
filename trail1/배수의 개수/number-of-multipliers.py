count1 = 0
count2 = 0 
for i in range(10):
    num= int(input())
    if num %3 ==0 :
        count1 += 1
    if num % 5 ==0:
        count2 += 1

print(f"{count1} {count2}")
