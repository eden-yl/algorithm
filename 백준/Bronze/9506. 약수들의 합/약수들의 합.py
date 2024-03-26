def getDivisorList(n):
    li=[]
    for i in range(1, int(n**(1/2))+1):
        if n%i==0:
            li.append(i)
            if i**2 != n:
                li.append(n//i)
    li.sort()
    li.remove(n)
    return li

while True:
    n=int(input())
    if n==-1:
        break
    li = getDivisorList(n)
    s=sum(li)
    if s==n:
        strList = []
        for i in li:
            strList.append(str(i))
        st=" + ".join(strList)
        print(str(n)+" = "+st) 
    else:
        print(str(n)+" is NOT perfect.")
