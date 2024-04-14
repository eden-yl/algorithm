n=int(input())
for i in range(n):
    p=int(input())
    dic={}
    for j in range(p):
        price,player=map(str, input().split())
        dic[player]=int(price)
    print(max(dic,key=dic.get))