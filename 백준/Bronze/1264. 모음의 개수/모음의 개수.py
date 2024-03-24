while True:
    count=0
    sentence=input()
    if sentence == '#':
        break
    for i in sentence.lower():
        if i == 'a':
            count += 1
        elif i == 'e':
            count += 1
        elif i == 'i':
            count += 1
        elif i == 'o':
            count += 1
        elif i == 'u':
            count += 1
    print(count)