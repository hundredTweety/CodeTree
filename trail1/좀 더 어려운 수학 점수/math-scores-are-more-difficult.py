A_math, A_Eng = map(int, input().split())
B_math, B_Eng = map(int, input().split())

if B_math > A_math:
    print("B")
elif A_math > B_math:
    print("A")

elif A_math == B_math:
    if A_Eng > B_Eng:
        print("A")
    else:
        print("B")
