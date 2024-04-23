n=int(input())
for i in range(n):
    c,v=map(int, input().split())
    result=int(c/v)
    print("You get " + str(result) + " piece(s) and your dad gets " + str(c-result*v) + " piece(s).")