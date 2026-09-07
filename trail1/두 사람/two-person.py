P1_a, P1_s = map(str, input().split())
P2_a, P2_s = map(str, input().split())

if (int(P1_a) >=19 and P1_s == "M") or int(P2_a) >=19 and P2_s == "M":
    print(1)

else:
    print(0)

