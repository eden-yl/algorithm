M=int(input())
N=int(input())

def isPrime(num):
    if num<=1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num%i==0:
            return False
    return True

li=[]
for i in range(M, N+1):
    if isPrime(int(i)):
        li.append(int(i))

if len(li)==0:
    print(-1)
else:
    print(sum(li))
    print(min(li))