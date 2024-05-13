N = int(input())
scores = list(map(int, input().split()))

# 세준이의 최고점을 찾음
max_score = max(scores)

# 각 점수를 새로운 점수로 변환하여 총합을 구함
new_sum = sum(score / max_score * 100 for score in scores)

# 평균을 구하고 출력
print(new_sum / N)
