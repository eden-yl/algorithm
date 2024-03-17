N=int(input())
cute=0
result=""
for i in range(N):
    flag=int(input())
    if flag==1 :
        cute += 1
    else :
        cute -= 1
if(cute>0) :
    result="Junhee is cute!"
else :
    result="Junhee is not cute!"
print(result)