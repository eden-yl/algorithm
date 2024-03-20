N=int(input())
dic={}
for i in range(N):
    title, score=map(str, input().split())
    dic[title]=score
print(min(dic, key=dic.get))