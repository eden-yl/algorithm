N=int(input())
rest=0
for i in range(N):
    student,apple=map(int, input().split())
    rest += apple%student
print(rest)