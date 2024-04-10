T,S=map(int, input().split())
if T<=11:
    print(280)
elif T>=12 and T<=16 and S==0:
    print(320)
elif S==1:
    print(280)
elif T>16:
    print(280)