x=list(map(int, input().split()))
y=input()
x.sort()
for i in range(0,3):
    if y[i]=='A':
        print(x[0],end=" ")
    elif y[i]=='B':
        print(x[1],end=" ")
    elif y[i]=='C':
        print(x[2],end=" ")