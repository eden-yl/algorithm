N=int(input())
for i in range(N):
    string=input()
    upper=string[0:1].upper()
    rest=string[1:]
    print(upper+rest)