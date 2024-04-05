T=int(input())
for i in range(T):
    li=list(map(int, input().split()))
    li.sort()
    li.remove(li[0])
    li.remove(li[len(li)-1])
    su=sum(li)
    if max(li) - min(li) >= 4:
        print("KIN")
        continue
    print(su)