total = 0
count = 0
while True:
    age=int(input())

    if 20<=age<30:
        total +=age
        count +=1
    else:
        break
print(f"{total/count:.2f}")