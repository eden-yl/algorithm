li=list(map(int, input().split()))
li.sort()
strLi=[]
for i in li:
    strLi.append(str(i))
print(" ".join(strLi))