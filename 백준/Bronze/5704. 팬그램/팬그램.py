import sys
while 1:
    s = str(sys.stdin.readline().strip())
    if s =='*':
        break
    answer = 0
    for i in range(26):
        if chr(97+i) not in s:
            answer +=1
    if answer==0:
        print('Y')
    else:
        print('N')