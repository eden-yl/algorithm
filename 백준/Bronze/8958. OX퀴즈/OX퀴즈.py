n=int(input())

def calculate(answer):
    # OOXXOXXOOO
    result = 0
    total = 0
    li = list(answer)
    for i in li:
        if i=='O':
            result +=1
            total += result
        else:
            result = 0
    return total

for i in range(1,n+1):
    answer = input()
    total = calculate(answer)
    print(total)