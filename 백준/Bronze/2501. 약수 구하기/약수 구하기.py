def divisor(n):
    result=[]
    for i in range(1, int(n**(1/2))+1):
        if n%i==0:
            result.append(i)
            if i < n//i:
                result.append(n//i)
        result.sort()
    return result

N,K=map(int, input().split())
result=divisor(N)
if len(result)<K:
    print(0)
else:
    print(result[K-1])