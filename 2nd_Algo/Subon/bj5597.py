import sys

student = []

for N in range(30):
    student.append(N+1)

for i in range(28):
    n = int(sys.stdin.readline())
    student.remove(n)

for i in range(len(student)):
    print(student[i])
