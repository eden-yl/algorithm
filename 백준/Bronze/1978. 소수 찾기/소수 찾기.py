def isPrime(num):
    if num<=1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num%i==0:
            return False
    return True    

n=int(input())
li=list(input().split())
cnt=0
for i in li:
    num=int(i)
    if isPrime(num):
        cnt+=1
print(cnt)