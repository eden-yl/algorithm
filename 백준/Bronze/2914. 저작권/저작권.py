import math
A, I = map(int, input().split())
x = 0
while True : 
    if math.ceil(x/A)==I :
        break
    x += 1
print(x)