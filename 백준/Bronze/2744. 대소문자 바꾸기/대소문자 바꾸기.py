li=list(input())
result=""
for i in li:
    if i.islower():
        result += i.upper()
    else:
        result += i.lower()
print(result)