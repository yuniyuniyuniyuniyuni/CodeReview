import sys

a = []
count = 1

for i in range(10):
    n = int(sys.stdin.readline())
    a.append(n%42)

a.sort()

for i in range(9):
    if a[i] == a[i+1]:
        pass
    else:
        count += 1

print(count)
