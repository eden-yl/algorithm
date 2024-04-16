n = input()
p = 10
q = 0
if len(n) < 10:
        print(n)
else :
    for _ in range(len(n) + 1):
        if _ == p:
            print(n[q:p])
            q = p
            if p + 10 > len(n):
                p = len(n)
            else:
                p += 10