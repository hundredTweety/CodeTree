P1, P1_t = map(str, input().split())
P2, P2_t = map(str, input().split())
P3, P3_t = map(str, input().split())

cold = [P1, int(P1_t), P2, int(P2_t), P3, int(P3_t)]
Emer=[0]*4

for i in range(0,6,2):
    if cold[i] == "Y" and cold[i+1] >= 37:
        Emer[0] +=1
    
    if cold[i] == "N" and cold[i+1] >= 37:
        Emer[1] +=1

    if cold[i] == "Y" and cold[i+1] < 37:
        Emer[2] +=1

    if cold[i] == "N" and cold[i+1] < 37:
        Emer[3] +=1

if Emer[0] >=2:
    print("E")

else:
    print("N")