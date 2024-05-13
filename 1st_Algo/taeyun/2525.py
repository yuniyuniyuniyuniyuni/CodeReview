# 현재 시각과 요리하는 데 필요한 시간 입력 받기
hour, minute = map(int, input().split())
cooking_time = int(input())

# 요리 종료 시간 계산
end_minute = (minute + cooking_time) % 60
end_hour = (hour + (minute + cooking_time) // 60) % 24

# 결과 출력
print(end_hour, end_minute)
