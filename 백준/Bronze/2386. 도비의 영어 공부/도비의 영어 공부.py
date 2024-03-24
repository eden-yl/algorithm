while True:
    count=0
    letter, blank, sentence=map(str, input().partition(" "))
    if letter == '#':
        break
    for i in sentence.lower():
        if i == letter:
            count += 1
    print(letter + " " + str(count))