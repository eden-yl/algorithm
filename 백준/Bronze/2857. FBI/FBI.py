li=[]
result=[]
for i in range(5):
    agent=input()
    li.append(agent)
for i in li:
    if 'FBI' in i:
        result.append(str(li.index(i)+1))
if len(result)==0:
    print('HE GOT AWAY!')
else:
    print(' '.join(result))