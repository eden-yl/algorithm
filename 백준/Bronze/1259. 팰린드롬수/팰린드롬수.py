while True:    
    num=input()
    if int(num)==0:
        break
    rev=num[::-1]
    if num==rev:
        print("yes")
    else:
        print("no")