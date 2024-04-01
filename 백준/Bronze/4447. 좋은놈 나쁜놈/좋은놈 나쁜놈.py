n=int(input())
for i in range(n):
    name=input()
    li=list(name.split())
    gCnt=0
    bCnt=0
    for j in list(name):
        wordLi=j
        if j.lower()=='g':
            gCnt += 1
        elif j.lower()=='b':
            bCnt += 1
    if gCnt>bCnt:
        print(name + " is GOOD")
    elif gCnt<bCnt:
        print(name + " is A BADDY")
    else:
        print(name + " is NEUTRAL")