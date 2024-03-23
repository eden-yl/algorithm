N=int(input())
result=""
for i in range(N):
    r,e,c=map(int, input().split())
    if e-c>r:
        result="advertise"
    elif e-c<r:
        result="do not advertise"
    else:
        result="does not matter"
    print(result)