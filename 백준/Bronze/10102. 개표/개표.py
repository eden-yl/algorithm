V=int(input())
li=list(input())
result=0
for i in li:
    if i=="A":
        result += 1
    elif i=="B":
        result -= 1
if result>0:
    print("A")
elif result<0:
    print("B")
else:
    print("Tie")