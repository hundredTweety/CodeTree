while True:
    w, h, str_ = map(str, input().split())
    w=int(w)
    h=int(h)
    print(w*h)
    if str_ == "C":
        break