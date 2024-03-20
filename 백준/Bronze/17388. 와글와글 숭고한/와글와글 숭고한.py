li=list(map(int, input().split()))
if sum(li)>=100:
    print("OK")
else:
    if li[0] == min(li):
        print("Soongsil")
    elif li[1] == min(li):
        print("Korea")
    elif li[2] == min(li):
        print("Hanyang")