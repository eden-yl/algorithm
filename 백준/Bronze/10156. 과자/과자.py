K, N, M = map(int, input().split())
result=int(K*N-M)
if result<0:
    result=0
print(result)