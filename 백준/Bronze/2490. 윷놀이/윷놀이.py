for i in range(3):
    li=list(map(int,input().split()))
    count=0
    for j in li:
        if j==1:
            count += 1
    if count==0:
        print("D")
    elif count==1:
        print("C")
    elif count==2:
        print("B")
    elif count==3:
        print("A")
    elif count==4:
        print("E")