N=int(input())
li=list(map(int, input().split()))
M=max(li)
newLi=[]
for i in range(N):
    newLi.append(li[i]/M*100)
print(sum(newLi)/len(newLi))