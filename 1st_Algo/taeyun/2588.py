# (1)의 위치에 들어갈 세 자리 수
num1 = int(input())
# (2)의 위치에 들어갈 세 자리 수
num2 = int(input())

# 각 위치에 들어갈 값을 계산
value3 = num1 * (num2 % 10)
value4 = num1 * ((num2 // 10) % 10)
value5 = num1 * ((num2 // 100) % 10)
value6 = num1 * num2

# 결과 출력
print(value3)
print(value4)
print(value5)
print(value6)
