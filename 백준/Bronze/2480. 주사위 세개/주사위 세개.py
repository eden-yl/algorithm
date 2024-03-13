a,b,c=map(int, input().split())
result=0
if a==b and b==c:
    result=10000+a*1000
elif a==b and b != c:
    result=1000+a*100
elif a==c and a != b:
    result=1000+a*100
elif b==c and a != b:
    result=1000+b*100
elif a != b and b != c and a != c:
    result=max(a,b,c)*100
print(result)