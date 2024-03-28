T=int(input())
for i in range(T):
    N=int(input())
    dic={}
    for i in range(N):
        school, alcohol=map(str, input().split())
        dic[school]=int(alcohol)
    print(max(dic,key=dic.get)) 