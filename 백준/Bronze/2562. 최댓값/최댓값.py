li=[]
sorted=[]
for i in range(9):
    num=int(input())
    li.append(num)
    sorted.append(num)
sorted.sort(reverse=True)
print(sorted[0])
print(li.index(sorted[0])+1)