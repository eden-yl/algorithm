import sys
input=sys.stdin.readline

def countScore(n):
    if n==0: return 0
    return (1 + n) * n // 2

n=int(input())
result=input().replace(" ", "").split('0')

score=0
for i in result:
    score += countScore(i.count('1'))

print(score)