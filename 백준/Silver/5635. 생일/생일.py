import sys
input = sys.stdin.readline

result = []
for _ in range(int(input())):
    n,d,m,y = input().rstrip().split()
    d,m,y = map(int,(d,m,y))
    result.append((y,m,d,n))
result.sort()
print(result[-1][3])
print(result[0][3])