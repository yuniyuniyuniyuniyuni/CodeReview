N = int(input())

for i in range(1, N + 1):
    # 공백을 추가하여 오른쪽 정렬을 구현
    print(" " * (N - i) + "*" * i)
