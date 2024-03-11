T=int(input())
for i in range(T):
    count,string=map(str, input().split())
    result=[]
    for j in list(string):
        result.append(j*int(count))
    print(''.join(result))