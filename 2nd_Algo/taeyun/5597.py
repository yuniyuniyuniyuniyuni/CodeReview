import sys

submitted = set()
for _ in range(28):
    submitted.add(int(sys.stdin.readline().rstrip()))

for i in range(1, 31):
    if i not in submitted:
        print(i)
        break

for j in range(i + 1, 31):
    if j not in submitted:
        print(j)
        break
