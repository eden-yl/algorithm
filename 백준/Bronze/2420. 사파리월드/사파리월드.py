N,M=map(int, input().split())
if N>=M:
    print(abs(N-M))
elif N<=M:
    print(abs(M-N))