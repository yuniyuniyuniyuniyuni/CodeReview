print("\\    /\\")
print(" )  ( ')")
print("(  /  )")
print(" \\(__)|")

2884

# 현재 설정된 알람 시간 입력 받기
H, M = map(int, input().split())

# 45분을 뺀 시간 계산
M -= 45

# 만약 분이 음수가 된다면 시간을 조정
if M < 0:
    H -= 1
    M += 60

# 만약 시간이 음수가 된다면 시간을 24로 조정
if H < 0:
    H += 24

# 결과 출력
print(H, M)