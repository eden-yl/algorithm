import sys
N=int(sys.stdin.readline().rstrip())
sum=0
for i in range(N):
    s=int(sys.stdin.readline().rstrip())
    sum += s
print(sum-(N-1))