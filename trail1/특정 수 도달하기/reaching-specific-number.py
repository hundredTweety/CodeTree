num = list(map(int, input().split()))
sum_ = 0
count_ =0
for i in range(len(num)):
    if num[i] >=250:
        break
    
    else:
        sum_ += num[i]
        count_ +=1
print(sum_ , round(sum_/count_,1))
