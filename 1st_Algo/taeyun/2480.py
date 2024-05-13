# 세 개의 주사위 눈 입력 받기
dice = list(map(int, input().split()))

# 세 개의 주사위 눈 중 가장 큰 값 계산
max_dice = max(dice)

# 모든 주사위 눈이 같은 경우
if dice[0] == dice[1] == dice[2]:
    prize = 10000 + dice[0] * 1000
# 두 개의 주사위 눈이 같은 경우
elif dice[0] == dice[1] or dice[0] == dice[2] or dice[1] == dice[2]:
    # 두 개의 눈이 같은 경우, 그 눈을 상금으로 계산
    if dice[0] == dice[1]:
        prize = 1000 + dice[0] * 100
    elif dice[0] == dice[2]:
        prize = 1000 + dice[0] * 100
    else:
        prize = 1000 + dice[1] * 100
# 모든 주사위 눈이 다른 경우
else:
    prize = max_dice * 100

# 상금 출력
print(prize)
