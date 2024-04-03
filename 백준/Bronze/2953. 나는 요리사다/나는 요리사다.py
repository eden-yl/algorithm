result=[]
for i in range(5):
    li=list(map(int,input().split()))
    result.append(sum(li))
print(str(result.index(max(result))+1) + " " + str(max(result)))