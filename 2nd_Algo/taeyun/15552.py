import sys

# 입력 최적화를 위해 sys.stdin.readline() 사용
T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    A, B = map(int, sys.stdin.readline().rstrip().split())
    print(A + B)
