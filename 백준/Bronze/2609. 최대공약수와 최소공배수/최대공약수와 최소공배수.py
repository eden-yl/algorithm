a,b=map(int, input().split())

def gcd(n,m):
    if m==0:
        return n
    else:
        return gcd(m,n%m)

def lcm(n,m):
    return n//gcd(n,m)*m

print(gcd(a,b))
print(lcm(a,b))