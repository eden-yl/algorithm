n = int(input())
for i in range(1,n+1):
    li = input().split()
    result = 0
    for j in li:
        if li.index(j)==0:
            number = float(j)
        else:
            exp = j
            result = number
            if j=='@':
                number = number*3
                result = number
            if j=='%':
                number = number+5
                result = number
            if j=='#':
                number = number-7
                result = number
    formatted_number = f"{result:.2f}"
    print(formatted_number)